# Generated by Django 4.1.7 on 2023-02-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transactions", "0002_remove_transaction_amount_due"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_id",
            field=models.CharField(
                blank=True, editable=False, max_length=50, unique=True
            ),
        ),
    ]