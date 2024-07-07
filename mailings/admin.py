from django.contrib import admin

from mailings.models import Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('send_date_time', 'send_frequency', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
