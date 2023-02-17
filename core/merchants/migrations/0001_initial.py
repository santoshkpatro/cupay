# Generated by Django 4.1.7 on 2023-02-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Merchant",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "merchant_id",
                    models.CharField(blank=True, max_length=50, unique=True),
                ),
                ("company_name", models.CharField(max_length=300)),
                ("company_description", models.TextField(blank=True, null=True)),
                ("company_logo", models.ImageField(upload_to="merchants/logos/")),
                ("is_registered", models.BooleanField()),
                ("business_country", models.CharField(max_length=3)),
                ("business_description", models.TextField(blank=True, null=True)),
                ("is_verified", models.BooleanField(default=False)),
                ("virtual_balance_curreny", models.CharField(max_length=3)),
                (
                    "virtual_balance",
                    models.DecimalField(decimal_places=4, default=0, max_digits=12),
                ),
                (
                    "live_merchant_access_key",
                    models.UUIDField(blank=True, null=True, unique=True),
                ),
                ("live_merchant_access_id", models.UUIDField(blank=True, null=True)),
                (
                    "test_merchant_access_key",
                    models.UUIDField(blank=True, null=True, unique=True),
                ),
                ("test_merchant_access_id", models.UUIDField(blank=True, null=True)),
            ],
            options={
                "db_table": "merchants",
            },
        ),
    ]
