# Generated by Django 4.2.6 on 2023-12-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_image_product_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[("Lux", "Люкс"), ("Medium", "Медиум"), ("Simple", "Обчный")],
                max_length=8,
                null=True,
            ),
        ),
    ]
