# Generated by Django 4.2.13 on 2024-06-09 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserStats",
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
                ("completed_trainings_number", models.IntegerField(default=0)),
                ("completed_trainings_equation", models.IntegerField(default=0)),
                ("completed_trainings_unequal", models.IntegerField(default=0)),
                ("correct_answers", models.IntegerField(default=0)),
                ("incorrect_answers", models.IntegerField(default=0)),
                ("user_points", models.IntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]