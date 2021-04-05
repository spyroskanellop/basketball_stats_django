from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from run import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/addTeam', views.createTeam, name='team_insert'),
    path('team/showTeams', views.team_list, name='team_list'),
    # path('team/updateTeam/'),
    path('update_team/<int:id>/', views.updateTeam, name='team_update'),
    path('delete_team/<int:id>/', views.deleteTeam, name='team_delete'),

    path('', views.home, name='home'),
    # path('player/addPlayer', views.player_form)
]
