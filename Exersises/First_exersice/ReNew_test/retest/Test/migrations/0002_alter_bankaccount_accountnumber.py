# Generated by Django 5.0.3 on 2024-04-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='accountNumber',
            field=models.CharField(max_length=11),
        ),
    ]