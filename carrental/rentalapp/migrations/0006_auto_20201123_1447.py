# Generated by Django 3.1.2 on 2020-11-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0005_auto_20201123_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPELETED'), ('BOOKED', 'BOOKED'), ('AVAILABLE', 'AVAILABLE')], max_length=20),
        ),
    ]
