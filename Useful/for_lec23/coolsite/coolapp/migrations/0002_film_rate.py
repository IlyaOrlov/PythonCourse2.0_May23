# Generated by Django 3.2.8 on 2021-10-14 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
