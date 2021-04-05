from django.db import models
from django.forms import CharField, DateInput, forms
from django.forms import ModelForm,Textarea


class Teams(models.Model):
    team_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.team_name

class Meta:
    db_table = "Teams"

class Players(models.Model):
    POSITION = (
        ('Point guard', 'Point guard'),
        ('Shooting guard', 'Shooting guard'),
        ('Small forward', 'Small forward'),
        ('Power forward', 'Power forward'),
        ('Center', 'Center'),
    )
    DOMINANT_HAND = (
        ('Right hand', 'Right hand'),
        ('Left hand', 'Left hand'),
    )

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField("dob(mm/dd/year)", auto_now_add=False, auto_now=False, blank=True, null=True)
    position = models.CharField(max_length=20, null=True, choices=POSITION)
    dominant_hand = models.CharField(max_length=20, null=True, choices=DOMINANT_HAND)
    nationality = models.CharField(max_length=20)
    teamID = models.ForeignKey(Teams, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

class Meta:
    db_table = "Players"

class Scores(models.Model):
    xCoor = models.FloatField()
    yCoor = models.FloatField()
    isGoal = models.BooleanField()
    playerID = models.ManyToManyField(Players)

class Meta:
    db_table = "Score"
