# Generated by Django 4.2.9 on 2024-04-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]