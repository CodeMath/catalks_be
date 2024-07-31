# Generated by Django 5.0.7 on 2024-07-31 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatParticipationModel",
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
                ("room_id", models.UUIDField()),
                ("user_id", models.UUIDField()),
                ("joined_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
