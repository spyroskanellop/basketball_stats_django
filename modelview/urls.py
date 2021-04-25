from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from run import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('team/addTeam', views.createTeam, name='team_insert'),
    path('team/showTeams', views.viewTeam, name='team_list'),
    path('team/showStats/<int:id>', views.teamStats, name='team_stats'),
    path('update_team/<int:id>/', views.updateTeam, name='team_update'),
    path('delete_team/<int:id>/', views.deleteTeam, name='team_delete'),

    path('player/addPlayer', views.createPlayer, name='player_insert'),
    path('player/showPlayers', views.viewPlayer, name='player_list'),
    path('updatePlayer/<int:id>/', views.updatePlayer, name='player_update'),
    path('deletePlayer/<int:id>/', views.deletePlayer, name='player_delete'),
    path('player/showStats/<int:id>', views.updatePlayerStats, name='player_stats'),

    path('player/setScore', views.goToScore, name='court'),
    path('game/setGame', views.chooseGame, name='choose_game'),

    path('team/addStats', views.createTeamStats, name='team_stats_insert'),
    path('team/updateStats/<int:id>/', views.updateTeamStats, name='team_stats_update'),
    path('player/addStats', views.createPlayerStats, name='player_stats_insert'),

    path('charts', views.TeamChartView.as_view()),
]