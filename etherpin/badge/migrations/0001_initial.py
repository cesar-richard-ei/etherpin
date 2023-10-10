# Generated by Django 4.2.6 on 2023-10-09 09:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Badge",
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
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="badges")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="BadgeOwnership",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="BadgePlacement",
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
                ("x", models.PositiveSmallIntegerField(default=0)),
                ("y", models.PositiveSmallIntegerField(default=0)),
                ("size", models.PositiveSmallIntegerField(default=100)),
                (
                    "rotation",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(360)],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "badge_ownership",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="badge.badgeownership",
                    ),
                ),
            ],
        ),
    ]
