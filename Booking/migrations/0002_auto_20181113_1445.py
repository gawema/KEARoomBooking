# Generated by Django 2.1.1 on 2018-11-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='startDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]