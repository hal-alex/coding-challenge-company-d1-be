# Generated by Django 4.2 on 2023-04-18 21:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Elevator",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("starting_floor", models.IntegerField()),
                ("ending_floor", models.IntegerField()),
                ("elevator_name", models.CharField(max_length=250)),
            ],
        ),
    ]