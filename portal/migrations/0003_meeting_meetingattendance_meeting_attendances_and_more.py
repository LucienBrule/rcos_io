# Generated by Django 4.1.3 on 2022-12-05 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0002_alter_user_options_alter_enrollment_credits_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="The optional title of the meeting",
                        max_length=100,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("small_group", "Small Group"),
                            ("large_group", "Large Group"),
                            ("workshop", "Workshop"),
                            ("mentor", "Mentor"),
                            ("coordinator", "Coordinator"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the meeting is visible to users",
                    ),
                ),
                (
                    "starts_at",
                    models.DateTimeField(help_text="When the meeting starts"),
                ),
                ("ends_at", models.DateTimeField(help_text="When the meeting ends")),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        help_text="Where the meeting takes place either physically or virtually",
                        max_length=500,
                    ),
                ),
                (
                    "description_markdown",
                    models.TextField(
                        blank=True,
                        help_text="Optional publicly displayed description for the meeting. Supports Markdown.",
                        max_length=10000,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MeetingAttendance",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "is_added_by_admin",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this attendance was added by an admin instead of by the user",
                    ),
                ),
                (
                    "meeting",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="portal.meeting"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="portal.user"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="meeting",
            name="attendances",
            field=models.ManyToManyField(
                related_name="meeting_attendances",
                through="portal.MeetingAttendance",
                to="portal.user",
            ),
        ),
        migrations.AddField(
            model_name="meeting",
            name="host",
            field=models.ForeignKey(
                blank=True,
                help_text="Optional host for the meeting (e.g. mentor hosting a workshop",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="portal.user",
            ),
        ),
        migrations.AddField(
            model_name="meeting",
            name="semester",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="meetings",
                to="portal.semester",
            ),
        ),
    ]
