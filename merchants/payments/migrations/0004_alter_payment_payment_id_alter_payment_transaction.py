# Generated by Django 4.1.7 on 2023-02-21 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("transactions", "0004_alter_transaction_currency"),
        ("payments", "0003_alter_payment_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_id",
            field=models.CharField(
                blank=True, editable=False, max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="transaction",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="transactions.transaction",
            ),
        ),
    ]