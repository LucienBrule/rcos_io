# Generated by Django 4.1.4 on 2023-01-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0003_alter_user_managers"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="project",
            name="portal_proj_name_ae220a_idx",
        ),
        migrations.RemoveField(
            model_name="project",
            name="summary",
        ),
        migrations.AddIndex(
            model_name="project",
            index=models.Index(
                fields=["name", "description"], name="portal_proj_name_d81550_idx"
            ),
        ),
    ]
