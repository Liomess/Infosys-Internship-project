# Generated by Django 4.2.9 on 2024-04-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]
