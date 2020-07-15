# Generated by Django 3.0.1 on 2019-12-27 02:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191227_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='pok_type',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(to='main.Type'),
        ),
        migrations.AlterField(
            model_name='completed',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 2, 19, 5, 421526)),
        ),
        migrations.AlterField(
            model_name='game_info',
            name='date_start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 2, 19, 5, 420433)),
        ),
    ]