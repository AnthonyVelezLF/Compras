# Generated by Django 4.1 on 2022-08-04 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha_caducidad',
            field=models.DateField(default=datetime.date(2022, 8, 3)),
        ),
    ]
