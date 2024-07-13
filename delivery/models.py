from django.db import models

from mailings.models import Mailing
from clients.models import Client

NULLABLE = {'blank': True, 'null': True}


class DeliveryAttempt(models.Model):
    STATUS_CHOICES = [('successful', 'Successful'), ('failed', 'Failed'), ]

    mailing = models.ForeignKey('mailings.Mailing', on_delete=models.CASCADE, verbose_name='рассылка')

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='статус попытки')
    server_response = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера')
    error_message = models.TextField(**NULLABLE, verbose_name='сообщение об ошибке')
