from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from run import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.goHome, name='home'),

    path('team/addTeam', views.createTeam, name='team_insert'),
    path('team/showTeams', views.viewTeam, name='team_list'),
    path('team/showStats/<int:id>', views.teamStats, name='team_stats'),
    path('update_team/<int:id>/', views.updateTeam, name='team_update'),
    path('delete_team/<int:id>/', views.deleteTeam, name='team_delete'),

    path('player/form', views.createPlayer2, name='player_insert2'),
    path('player/showPlayers', views.viewPlayer, name='player_list'),
    path('updatePlayer/<int:id>/', views.updatePlayer, name='player_update'),
    path('deletePlayer/<int:id>/', views.deletePlayer, name='player_delete'),
    path('player/showStats/<int:id>', views.showPlayerStats, name='player_stats'),
    path('player/addStats', views.createPlayerStats, name='player_stats_insert'),
    path('player/updateStats/<int:id>/', views.updatePlayerStats, name='player_stats_update'),

    path('player/setScore', views.goToScore, name='court'),
    path('game/setGame', views.chooseGame, name='choose_game'),

    path('team/averageStats', views.createAvgTeamStats, name='average_team_stats'),
    path('player/averageStats', views.createAvgPlayerStats, name='average_player_stats'),

    path('team/addStats', views.createTeamStats, name='team_stats_insert'),
    path('team/updateStats/<int:id>/', views.updateTeamStats, name='team_stats_update'),

    path('charts', views.TeamChartView.as_view(), name='charts'),
    path('3point', views.Point3ChartView.as_view(), name='3_point_chart'),
    path('2point', views.Point2ChartView.as_view(), name='2_point_chart'),
    path('free_throw2', views.FreeThrowChartView2.as_view(), name='free_throw_chart'),
    path('def_reb', views.DefensiveReboundChartView.as_view(), name='def_reb'),
    path('off_reb', views.OffensiveReboundChartView.as_view(), name='off_reb'),
    path('assists', views.AssistsChartView.as_view(), name='assists'),
    path('steals', views.StealsChartView.as_view(), name='steals'),
    path('turnovers', views.TurnoversChartView.as_view(), name='turnovers'),
    path('points', views.PointsChartView.as_view(), name='points'),

    path('3pointplayer', views.Point3ChartPlayerView.as_view(), name='3_point_chart_player'),

    path('2pointplayer', views.Point2ChartPlayerView.as_view(), name='2_point_chart_player'),
    path('freethrowplayer', views.FreeThrowChartPlayerView.as_view(), name='free_throw_chart_player'),
    path('assistsplayer', views.AssistsChartPlayerView.as_view(), name='assists_player'),
    path('off_reb_player', views.OffRebChartPlayerView.as_view(), name='off_reb_player'),
    path('def_reb_player', views.DefRebChartPlayerView.as_view(), name='def_reb_player'),
    path('steals_player', views.StealsChartPlayerView.as_view(), name='steals_player'),
    path('turnovers_player', views.TurnoversChartPlayerView.as_view(), name='turnovers_player'),
    path('points_player', views.PointsChartPlayerView.as_view(), name='points_player'),

]