# Generated by Django 4.1.6 on 2023-02-01 15:31

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manga",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("chapters", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "added_on",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 2, 1, 21, 1, 21, 64531)
                    ),
                ),
            ],
        ),
    ]
