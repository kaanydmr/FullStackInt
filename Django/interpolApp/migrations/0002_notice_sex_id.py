# Generated by Django 5.0.8 on 2024-08-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interpolApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notice",
            name="sex_id",
            field=models.CharField(max_length=5, null=True),
        ),
    ]
