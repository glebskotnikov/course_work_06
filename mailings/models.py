from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    SEND_FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    send_time = models.TimeField(verbose_name='время рассылки')
    send_frequency = models.CharField(max_length=10, choices=SEND_FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=20, default='создана', verbose_name='статус')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    clients = models.ManyToManyField('clients.Client', related_name='mailings')

    def __str__(self):
        return f"{self.get_send_frequency_display()} рассылка в {self.send_time}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    mailing = models.ForeignKey('mailings.Mailing', on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=255, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
