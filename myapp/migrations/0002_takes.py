# Generated by Django 5.0.3 on 2024-03-09 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Takes",
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
                (
                    "courses",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.student"
                    ),
                ),
            ],
        ),
    ]
