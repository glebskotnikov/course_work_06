from django.core.management import call_command
from django.apps import AppConfig


class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    # def ready(self):
    #     call_command('crontab', 'add')
