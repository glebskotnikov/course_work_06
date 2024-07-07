from django.core.mail import send_mail

from config import settings


def send_mailings():
    send_mail(
        'тема письма',
        'тело письма',
        'glskotnikov@yandex.ru',
        ['skotnikov.nsk@gmail.com']
    )
