from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    SEND_FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена'), ('canceled', 'Отменена'), ('error', 'Ошибка'),]

    name = models.CharField(max_length=50, verbose_name='название рассылки', **NULLABLE)
    send_date_time = models.DateTimeField(default=timezone.now, verbose_name='дата и время рассылки')
    send_frequency = models.CharField(max_length=10, choices=SEND_FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created', verbose_name='статус рассылки')
    attempts = models.IntegerField(default=0, verbose_name='попытки рассылки')

    clients = models.ManyToManyField('clients.Client', related_name='mailings')
    message = models.ForeignKey('mailings.Message', on_delete=models.CASCADE, related_name='message', verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f"{self.get_send_frequency_display()} рассылка в {self.send_date_time}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
