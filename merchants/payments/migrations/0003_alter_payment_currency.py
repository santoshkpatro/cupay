# Generated by Django 4.1.7 on 2023-02-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_rename_charges_payment_service_charges_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="currency",
            field=models.CharField(
                choices=[("INR", "INR"), ("USD", "USD")], max_length=3
            ),
        ),
    ]
