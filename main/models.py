import datetime
from django.db import models

class Evolution(models.Model):
    name = models.CharField(max_length=15, default='BetterVersion')

class Game(models.Model):
    name = models.CharField(max_length=20, default='Game')
    gen = models.IntegerField(default = (-1))

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=15, default='Route 0')
    game = models.ForeignKey(Game,on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name + ', ' + self.name

class Type(models.Model):
    name = models.CharField(max_length=15, default='Type')

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=15, default='Missing No')
    numb = models.IntegerField(default = (-1))
    types = models.ManyToManyField(Type)
    locations = models.ManyToManyField(Location)
    evolution = models.ForeignKey(Evolution,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=30)
    conference = models.CharField(max_length=30)
    division = models.CharField(max_length=2)

    def __str__(self):
        return self.team_name

class Team_RPI(models.Model):
    #team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=30)
    wp = models.FloatField(default=(-1))
    owp = models.FloatField(default=(-1))
    oowp = models.FloatField(default=(-1))
    bonus = models.FloatField(default=(-1))
    rpi = models.FloatField(default=(-1))

    def __str__(self):
        return self.team_name

class Game_Info(models.Model):
    team = models.CharField(max_length=30)
    opp_team = models.CharField(max_length=30)
    points = models.IntegerField(default=(-1))
    opp_points = models.IntegerField(default=(-1))
    date_start_time = models.DateTimeField(default=datetime.datetime.now())
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return (self.team + " | " + self.opp_team)

class Completed(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    completed = models.BooleanField(default=False)
# Create your models here.


# Hashtag
