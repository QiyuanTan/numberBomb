# Generated by Django 4.2.2 on 2023-06-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainsite", "0005_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="number",
            name="in_progress",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]