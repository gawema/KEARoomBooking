# Generated by Django 2.1.1 on 2018-10-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='campusName',
            field=models.CharField(max_length=50),
        ),
    ]