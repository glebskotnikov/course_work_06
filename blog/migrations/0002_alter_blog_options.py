# Generated by Django 4.2.5 on 2024-07-31 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "ordering": ["title"],
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]
