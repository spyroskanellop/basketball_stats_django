from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from run import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('team/addTeam', views.createTeam, name='team_insert'),
    path('team/showTeams', views.team_list, name='team_list'),
    path('update_team/<int:id>/', views.updateTeam, name='team_update'),
    path('delete_team/<int:id>/', views.deleteTeam, name='team_delete'),

    path('player/addPlayer', views.player_form, name='player_insert'),
    path('player/showPlayers', views.player_list, name='player_list'),
    path('updatePlayer/<int:id>/', views.updatePlayer, name='player_update'),
    path('deletePlayer/<int:id>/', views.deletePlayer, name='player_delete'),

    path('player/setScore', views.goToScore, name='court'),
]
