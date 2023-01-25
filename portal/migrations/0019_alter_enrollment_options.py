# Generated by Django 4.1.4 on 2023-01-25 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "portal",
            "0018_rename_mentor_application_deadlines_semester_mentor_application_deadline",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="enrollment",
            options={
                "get_latest_by": ["semester"],
                "ordering": ["semester", "user__first_name"],
            },
        ),
    ]