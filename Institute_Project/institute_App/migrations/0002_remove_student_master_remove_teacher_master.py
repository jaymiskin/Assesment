# Generated by Django 4.1.4 on 2023-01-02 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("institute_App", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="Master",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="Master",
        ),
    ]