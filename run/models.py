from django.core.validators import MaxValueValidator
from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.team_name

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

    number = models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField("dob(dd/mm/year)", auto_now_add=False, auto_now=False, blank=True, null=True)
    height = models.CharField(max_length=20, default=0)
    weight = models.IntegerField(validators=[MaxValueValidator(400)], default=0)
    position = models.CharField(max_length=20, null=True, choices=POSITION)
    dominant_hand = models.CharField(max_length=20, null=True, choices=DOMINANT_HAND)
    nationality = models.CharField(max_length=50)
    experience = models.IntegerField(validators=[MaxValueValidator(30)], default=0)
    teamID = models.ForeignKey(Teams, null=True, on_delete=models.CASCADE)

    # return the value when object is called
    def __str__(self):
        return str(self.id)

class Scores(models.Model):
    xCoor = models.FloatField()
    yCoor = models.FloatField()
    isGoal = models.BooleanField()
    playerID = models.ManyToManyField(Players)

class TeamStats(models.Model):
    games = models.IntegerField(validators=[MaxValueValidator(110)], default=0)

    field_goals = models.IntegerField(validators=[MaxValueValidator(5000)], default=0)
    field_goal_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    three_point_field_goal = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    three_point_field_goal_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    three_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    two_point_field_goal = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    two_point_field_goal_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    two_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    free_throws = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    free_throw_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    offensive_rebounds = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    defensive_rebounds = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    total_rebounds = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)

    assists = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    steals = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    turnovers = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    blocks = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    personal_fouls = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    points = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)

    teamID = models.ForeignKey(Teams, null=True, on_delete=models.CASCADE)

class PlayerStats(models.Model):
    games = models.IntegerField(validators=[MaxValueValidator(110)], default=0)
    minutes_played = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goal_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    three_point_field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_point_field_goal_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    two_point_field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_point_field_goal_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    free_throws = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    free_throw_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    offensive_rebounds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    defensive_rebounds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_rebounds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    assists = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    steals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    turnovers = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    blocks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    personal_fouls = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    points = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    playerID = models.ForeignKey(Players, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.playerID

class AverageTeamStats(models.Model):
    games = models.IntegerField(validators=[MaxValueValidator(110)], default=0)
    field_goals = models.IntegerField(validators=[MaxValueValidator(5000)], default=0)
    field_goal_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_point_field_goal = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    three_point_field_goal_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    three_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_point_field_goal = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    two_point_field_goal_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    two_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    free_throws = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    free_throw_attempts = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    offensive_rebounds = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    defensive_rebounds = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    total_rebounds = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    assists = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    steals = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    turnovers = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    blocks = models.IntegerField(validators=[MaxValueValidator(1000)], default=0)
    personal_fouls = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)
    points = models.IntegerField(validators=[MaxValueValidator(10000)], default=0)

class AveragePlayerStats(models.Model):
    games = models.IntegerField(validators=[MaxValueValidator(110)], default=0)
    field_goals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goal_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_point_field_goal = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_point_field_goal_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    three_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_point_field_goal = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_point_field_goal_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    two_point_field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    free_throws = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    free_throw_attempts = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    offensive_rebounds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    defensive_rebounds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_rebounds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    assists = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    steals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    turnovers = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    blocks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    personal_fouls = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    points = models.DecimalField(max_digits=5, decimal_places=2, null=True)

