# Generated by Django 4.2.5 on 2024-07-07 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0003_remove_message_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='start_datetime',
        ),
    ]
