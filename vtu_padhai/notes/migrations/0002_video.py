# Generated by Django 4.2.3 on 2024-09-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                    "semester",
                    models.IntegerField(
                        choices=[
                            (1, "Semester 1"),
                            (2, "Semester 2"),
                            (3, "Semester 3"),
                            (4, "Semester 4"),
                            (5, "Semester 5"),
                            (6, "Semester 6"),
                            (7, "Semester 7"),
                            (8, "Semester 8"),
                        ]
                    ),
                ),
                ("youtube_id", models.CharField(max_length=100)),
            ],
        ),
    ]
