# Generated by Django 5.1.7 on 2025-03-31 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppping1', models.CharField(max_length=100)),
                ('toppping2', models.CharField(max_length=100)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaShop.size')),
            ],
        ),
    ]
