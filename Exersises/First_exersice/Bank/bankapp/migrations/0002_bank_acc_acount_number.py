# Generated by Django 5.0.3 on 2024-03-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_acc',
            name='acount_number',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]