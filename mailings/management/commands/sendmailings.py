from django.core.management.base import BaseCommand
from mailings.cron import process_mailings


class Command(BaseCommand):
    help = 'Send scheduled mailings'

    def handle(self, *args, **kwargs):
        process_mailings()
