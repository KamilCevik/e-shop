# Generated by Django 4.2.1 on 2023-06-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0015_alter_product_amount_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="amount",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
