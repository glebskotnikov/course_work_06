from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
