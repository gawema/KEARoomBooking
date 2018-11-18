# Generated by Django 2.1.1 on 2018-11-18 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_auto_20181116_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='emailID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
    ]
