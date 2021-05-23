# Generated by Django 3.1.7 on 2021-05-22 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AverageTeamStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(110)])),
                ('field_goals', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5000)])),
                ('field_goal_attempts', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('field_goal_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('three_point_field_goal', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('three_point_field_goal_attempts', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('three_point_field_goal_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('two_point_field_goal', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('two_point_field_goal_attempts', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('two_point_field_goal_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('free_throws', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('free_throw_attempts', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('free_throw_percentage', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('offensive_rebounds', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('defensive_rebounds', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('total_rebounds', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('assists', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('steals', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('turnovers', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('blocks', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('personal_fouls', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
                ('points', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)])),
            ],
        ),
    ]
