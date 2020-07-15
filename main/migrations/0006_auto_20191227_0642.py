# Generated by Django 3.0.1 on 2019-12-27 06:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191227_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Game', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='completed',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 6, 42, 8, 737499)),
        ),
        migrations.AlterField(
            model_name='game_info',
            name='date_start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 6, 42, 8, 736242)),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(default='Type', max_length=15),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Route 0', max_length=15)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Game')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='locations',
            field=models.ManyToManyField(to='main.Location'),
        ),
    ]