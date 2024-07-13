import os
import smtplib
from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

from delivery.models import DeliveryAttempt
from mailings.models import Mailing

import pytz


# функция отправки рассылки
def send_mailing(mailing):
    mailing.attempts += 1
    mailing.save()

    if mailing.attempts >= 10:
        mailing.status = 'canceled'
        mailing.save()

    try:
        send_mail(
            subject=mailing.message.subject,
            message=mailing.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.clients.all()],
            fail_silently=False,
        )
        DeliveryAttempt.objects.create(mailing=mailing, status="successful")
        return "completed"
    except BadHeaderError:
        print("Invalid header used. Mail was not sent.")
        DeliveryAttempt.objects.create(
            mailing=mailing,
            status="failed",
            error_message="Invalid header used. Mail was not sent.",
        )
        return "canceled"
    except smtplib.SMTPException as e:
        print("SMTPException occurred: ", str(e))
        DeliveryAttempt.objects.create(
            mailing=mailing, status="failed", error_message=str(e)
        )
        return "error"
    except Exception as e:
        print("An error occurred: ", str(e))
        DeliveryAttempt.objects.create(
            mailing=mailing, status="failed", error_message=str(e)
        )
        return "error"


# функция обработки запланированных рассылок
def process_mailings():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    list_of_statuses = ["created", "started", "error"]
    mailings = Mailing.objects.filter(send_date_time__lte=current_datetime).filter(
        status__in=list_of_statuses
    )

    timeframes = {"daily": 1, "weekly": 7, "monthly": 30}

    for mailing in mailings:
        last_attempt = (
            DeliveryAttempt.objects.filter(mailing=mailing)
            .order_by("-timestamp")
            .first()
        )
        timeframe = mailing.send_frequency

        if last_attempt is None:
            minutes_since_last_attempt = float('inf')
        else:
            minutes_since_last_attempt = (current_datetime - last_attempt.timestamp).total_seconds() / 60

        if mailing.status == 'error' and mailing.attempts < 5:
            mailing_status = send_mailing(mailing)
            mailing.status = mailing_status
            mailing.save()
        elif timeframe in timeframes and minutes_since_last_attempt >= timeframes[timeframe]:
            mailing_status = send_mailing(mailing)
            mailing.status = mailing_status
            mailing.save()
