# Generated by Django 3.1.2 on 2020-11-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0010_auto_20201124_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
