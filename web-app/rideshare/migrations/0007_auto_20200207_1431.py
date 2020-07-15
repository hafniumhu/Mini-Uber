# Generated by Django 3.0.2 on 2020-02-07 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0006_auto_20200202_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_ride',
            name='num_passenger',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Number of Passengers'),
        ),
    ]
