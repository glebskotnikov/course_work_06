# Generated by Django 4.2.5 on 2024-07-07 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0002_alter_mailing_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='mailing',
        ),
    ]