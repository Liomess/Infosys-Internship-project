# Generated by Django 4.2.9 on 2024-05-01 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_customer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cake_customization',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cash', 'Cash On Delivery'), ('unknown', 'Unknown')], default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='cake_customization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cakecustomization'),
        ),
    ]
