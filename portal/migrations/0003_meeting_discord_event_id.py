# Generated by Django 4.1.4 on 2023-01-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0002_meeting_presentation_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="discord_event_id",
            field=models.CharField(blank=True, max_length=23),
        ),
    ]
