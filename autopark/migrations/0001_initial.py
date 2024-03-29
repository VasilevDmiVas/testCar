# Generated by Django 5.0.1 on 2024-01-26 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=10)),
                ('is_electric', models.BooleanField(default=False)),
                ('year', models.IntegerField()),
                ('car_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autopark.carbrand')),
                ('car_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autopark.cartype')),
            ],
        ),
    ]
