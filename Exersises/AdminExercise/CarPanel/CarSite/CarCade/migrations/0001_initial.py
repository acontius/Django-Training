# Generated by Django 5.0.3 on 2024-04-04 12:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(choices=[('p', 'Petrol'), ('g', 'Gas'), ('e', 'Electronic')], default='p', help_text='What this car need to work', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(help_text="where are the manufature's branchs", max_length=300, null=True)),
                ('brand', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ns', 'not set'), ('f', 'SUV'), ('ha', 'Hatchback'), ('cp', 'Coupe'), ('nc', 'Convertible'), ('s', 'Sedan'), ('spc', 'Sports car'), ('p', 'Pickup'), ('m', 'MPV'), ('cc', 'City car'), ('ec', 'Electric cars'), ('fc', 'Family car'), ('hy', 'Hybrid'), ('lc', 'Luxury car'), ('mc', 'Microcar'), ('pc', 'Premium Compact'), ('sc', 'Supercar'), ('v', 'Van'), ('four', '4x4'), ('cu', 'CUV')], default='ns', help_text="Car's Type (e.g. SUV)", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('carId', models.UUIDField(default=uuid.uuid4, help_text='ID of the car', primary_key=True, serialize=False, unique=True)),
                ('carName', models.CharField(max_length=100)),
                ('date', models.DateField(help_text='The date of manufacture of this car')),
                ('capacity', models.IntegerField(help_text="The number of this car's capacity")),
                ('distance', models.IntegerField(help_text='Distance that this car travled')),
                ('inventory', models.IntegerField()),
                ('fuel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CarCade.fuel')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CarCade.manufacturer')),
                ('carType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CarCade.type')),
            ],
        ),
    ]
