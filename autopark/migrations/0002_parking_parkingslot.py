# Generated by Django 5.0.1 on 2024-01-26 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField(default=True)),
                ('number', models.IntegerField()),
                ('car', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autopark.car')),
                ('parking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autopark.parking')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]