# Generated by Django 4.1.7 on 2023-02-17 01:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("merchants", "0002_alter_merchant_business_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="merchant",
            name="live_merchant_access_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="merchant",
            name="live_merchant_access_key",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="merchant",
            name="test_merchant_access_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="merchant",
            name="test_merchant_access_key",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="merchant",
            name="virtual_balance_curreny",
            field=models.CharField(
                choices=[("INR", "INR"), ("USD", "USD")], max_length=3
            ),
        ),
    ]