# Generated by Django 3.0.1 on 2019-12-27 02:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 12, 27, 2, 4, 54, 328062))),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=30)),
                ('opp_team', models.CharField(max_length=30)),
                ('points', models.IntegerField(default=-1)),
                ('opp_points', models.IntegerField(default=-1)),
                ('date_start_time', models.DateTimeField(default=datetime.datetime(2019, 12, 27, 2, 4, 54, 326863))),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Missing No', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Team_RPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('wp', models.FloatField(default=-1)),
                ('owp', models.FloatField(default=-1)),
                ('oowp', models.FloatField(default=-1)),
                ('bonus', models.FloatField(default=-1)),
                ('rpi', models.FloatField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='cur_year_rank',
        ),
        migrations.RemoveField(
            model_name='team',
            name='prev_year_rank',
        ),
        migrations.RemoveField(
            model_name='team',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='team',
            name='year',
        ),
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='pok_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Type'),
        ),
    ]
