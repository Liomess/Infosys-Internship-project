# Generated by Django 4.2.9 on 2024-04-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_order_cake_customization_alter_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
