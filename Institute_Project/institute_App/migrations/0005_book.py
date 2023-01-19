# Generated by Django 4.1.4 on 2023-01-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("institute_App", "0004_club"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("Book_Name", models.CharField(max_length=40)),
                ("Author_Name", models.CharField(max_length=40)),
                ("Price", models.CharField(max_length=40)),
                ("Time_Period", models.CharField(max_length=40)),
            ],
            options={
                "db_table": "book",
            },
        ),
    ]
