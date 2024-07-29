# Generated by Django 4.2.5 on 2024-07-26 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0013_alter_mailing_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ["name"],
                "permissions": [
                    ("can_view_mailings", "Can view mailings"),
                    ("can_change_status", "Can change mailing status"),
                ],
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
    ]