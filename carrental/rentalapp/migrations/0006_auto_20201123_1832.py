# Generated by Django 3.1.3 on 2020-11-23 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0005_merge_20201123_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalapp.person'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='lender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rentalapp.person'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPELETED'), ('BOOKED', 'BOOKED'), ('AVAILABLE', 'AVAILABLE')], max_length=20),
        ),
    ]
