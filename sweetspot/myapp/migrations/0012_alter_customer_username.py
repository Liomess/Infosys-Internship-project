# Generated by Django 4.2.9 on 2024-04-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]