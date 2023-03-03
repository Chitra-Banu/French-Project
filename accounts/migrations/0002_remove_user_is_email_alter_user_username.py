# Generated by Django 4.1.7 on 2023-02-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_email",
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=10, unique=True, verbose_name="Roll NO"),
        ),
    ]
