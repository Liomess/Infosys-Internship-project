# Generated by Django 4.2.9 on 2024-04-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_cart_customization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default=None, max_length=225),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cash', 'Cash On Delivery')], default='debit_card', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
