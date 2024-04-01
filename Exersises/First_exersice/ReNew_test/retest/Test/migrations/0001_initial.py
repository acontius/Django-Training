# Generated by Django 5.0.3 on 2024-04-01 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Balance', models.CharField(max_length=30)),
                ('accountNumber', models.IntegerField(max_length=11)),
                ('type', models.CharField(max_length=30)),
                ('dateCreate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CheckingAccount',
            fields=[
                ('bankaccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Test.bankaccount')),
                ('lastTransaction', models.DateField()),
            ],
            bases=('Test.bankaccount',),
        ),
        migrations.CreateModel(
            name='SavaingAccount',
            fields=[
                ('bankaccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Test.bankaccount')),
            ],
            bases=('Test.bankaccount',),
        ),
    ]
