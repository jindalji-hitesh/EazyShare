# Generated by Django 3.1.2 on 2020-11-21 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0005_bookings_lender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='lender',
        ),
    ]