# Generated by Django 5.0.3 on 2024-03-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_created_at_order_uploaded_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="unit",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]