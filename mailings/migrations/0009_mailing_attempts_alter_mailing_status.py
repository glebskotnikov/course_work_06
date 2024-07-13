# Generated by Django 4.2.5 on 2024-07-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0008_alter_mailing_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="attempts",
            field=models.IntegerField(default=0, verbose_name="попытки рассылки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Создана"),
                    ("started", "Запущена"),
                    ("completed", "Завершена"),
                    ("canceled", "Отменена"),
                    ("error", "Ошибка"),
                ],
                default="created",
                max_length=20,
                verbose_name="статус рассылки",
            ),
        ),
    ]