# Generated by Django 5.0.3 on 2024-04-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_alter_bankaccount_accountnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='Balance',
            field=models.IntegerField(),
        ),
    ]
