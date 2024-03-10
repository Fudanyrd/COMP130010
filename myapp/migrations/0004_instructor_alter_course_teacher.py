# Generated by Django 5.0.3 on 2024-03-10 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_rename_courses_takes_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instructor",
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
                ("tid", models.CharField(max_length=20)),
                ("tname", models.CharField(max_length=50)),
                ("faculty", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.instructor"
            ),
        ),
    ]