# Generated by Django 4.2.5 on 2024-07-21 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0010_mailing_owner_message_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ["name"],
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
        migrations.AlterModelOptions(
            name="message",
            options={
                "ordering": ["subject"],
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
            },
        ),
    ]