from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from run import views

urlpatterns = [
    path('team/addTeam', views.team_form),
    path('conf', views.admin),
    path('home', views.home),
    path('team/showTeams', views.team_list),
    path('player/addPlayer', views.player_form)
]
