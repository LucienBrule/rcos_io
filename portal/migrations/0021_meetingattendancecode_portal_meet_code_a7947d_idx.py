# Generated by Django 4.1.4 on 2023-01-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0020_alter_user_graduation_year"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="meetingattendancecode",
            index=models.Index(fields=["code"], name="portal_meet_code_a7947d_idx"),
        ),
    ]