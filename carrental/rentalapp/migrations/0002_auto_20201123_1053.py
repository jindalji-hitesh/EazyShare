# Generated by Django 3.1.3 on 2020-11-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(default='static/images/iitbhu.png', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pic',
            field=models.ImageField(default='static/images/iitbhu.png', upload_to='static/images'),
        ),
    ]