# Generated by Django 4.1.7 on 2023-02-19 15:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("merchants", "0004_collaborator"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Collaborator",
        ),
    ]
