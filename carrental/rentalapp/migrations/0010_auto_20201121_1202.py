# Generated by Django 3.1.2 on 2020-11-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0009_auto_20201121_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
