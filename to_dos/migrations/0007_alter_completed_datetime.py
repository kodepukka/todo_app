# Generated by Django 4.1.5 on 2023-01-30 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_dos', '0006_completed_delete_com'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
