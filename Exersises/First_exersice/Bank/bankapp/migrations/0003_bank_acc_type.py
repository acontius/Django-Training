# Generated by Django 5.0.3 on 2024-03-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_bank_acc_acount_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_acc',
            name='type',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
