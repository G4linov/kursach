# Generated by Django 3.2.16 on 2022-11-09 19:21

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0003_default_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 11, 19, 21, 9, 721578, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
        migrations.CreateModel(
            name="ShopUserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tagline", models.CharField(blank=True, max_length=128, verbose_name="теги")),
                ("aboutMe", models.TextField(blank=True, max_length=512, verbose_name="о себе")),
                (
                    "gender",
                    models.CharField(blank=True, choices=[("M", "М"), ("W", "Ж")], max_length=1, verbose_name="пол"),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
