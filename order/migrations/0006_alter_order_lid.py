# Generated by Django 4.2.6 on 2023-10-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_order_lid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="lid",
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
