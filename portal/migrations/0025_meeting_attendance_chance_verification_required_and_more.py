# Generated by Django 4.1.4 on 2023-01-27 19:21

from decimal import Decimal

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0024_project_logo_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="attendance_chance_verification_required",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.25"),
                help_text="The % chance that a student submitting attendance will have to be verified (as a decimal)",
                max_digits=3,
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="discord_event_id",
            field=models.CharField(
                blank=True,
                help_text="Automatically managed, do not touch!",
                max_length=23,
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="host",
            field=models.ForeignKey(
                blank=True,
                help_text="Optional host for the meeting (e.g. mentor hosting a workshop)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
