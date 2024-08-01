# Generated by Django 4.2.5 on 2024-07-07 22:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_remove_mailing_end_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='send_time',
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='mailings.message', verbose_name='сообщение'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='send_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время рассылки'),
        ),
    ]
