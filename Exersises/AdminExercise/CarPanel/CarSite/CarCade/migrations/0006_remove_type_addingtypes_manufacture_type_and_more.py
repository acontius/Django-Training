# Generated by Django 5.0.3 on 2024-04-05 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarCade', '0005_rename_manufacturer_manufacture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='addingTypes',
        ),
        migrations.AddField(
            model_name='manufacture',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CarCade.type'),
        ),
        migrations.AlterField(
            model_name='car',
            name='carType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CarCade.type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(blank=True, help_text="Car's Type (e.g. SUV)", max_length=100, null=True),
        ),
    ]