import base64

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from run.models import Teams, Players
from .forms import TeamsForm, PlayersForm, ScoresForm, TeamStatsForm
from django.test.client import RequestFactory


# Create your views here.


def home(request):
    return render(request, 'admin.html')

def admin(request):
    return render(request, 'admin.html')

# def createTeam(request):
#     form = TeamsForm()
#     if request.method == 'POST':
#         form = TeamsForm(request.POST)
#             print(form.cleaned_data)
#         if form.is_valid():
#             print('saved')
#             form.save()
#             return HttpResponseRedirect('showTeams')
#         else:
#             print('not saved')
#     context = {'form': form}
#     return render(request, "teams_form.html", context)

def createTeam(request):
    form = TeamsForm(request.POST or None)
    if form.is_valid():
        # instance = form.save(commit=False)
        # instance.team_name = 'hi'

        # print(request.POST)
        # print(form.cleaned_data)
        # print(teamName)
        print('saved')
        # instance.save()
        form.save()
        return HttpResponseRedirect('showTeams')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "teams_form.html", context)

def updateTeam(request, id):
    team = Teams.objects.get(pk=id)
    form = TeamsForm(instance=team)
    if request.method == 'POST':
        form = TeamsForm(request.POST, instance=team)
        if form.is_valid():
            print('saved')
            form.save()
            return HttpResponseRedirect('/../../team/showTeams')
        else:
            print('not updated')

    context = {'form': form}
    # context = {'team_name': team.team_name}
    return render(request, "teams_form.html", context)

def team_view(request):
    team = Teams.objects.get(id=1)
    context= {"team_name": team.team_name}
    return render(request, "test.html", context)

def team_list(request):
    context = {'team_list':Teams.objects.all()}
    return render(request, "teams_list.html", context)

def deleteTeam(request, id):
    team = Teams.objects.get(pk=id)
    context = {'team':team}

    if request.method == "POST":
        team.delete()
        return HttpResponseRedirect('/../../team/showTeams')

    return render(request, "delete_team.html", context)

def player_form(request):
    form = PlayersForm()
    if request.method == 'POST':
        form = PlayersForm(request.POST)
        if form.is_valid:
            form.save()
            print('saved')
            return HttpResponseRedirect('showPlayers')
        else:
            print('not saved')

    return render(request, "players_form.html", {'form':form})


def player_list(request):
    context= {'player_list':Players.objects.all()}

    return render(request, "players_list.html", context)

def updatePlayer(request, id):
    player = Players.objects.get(pk=id)
    form = PlayersForm(instance=player)
    if request.method == "POST":
        form = PlayersForm(request.POST, instance=player)
        if form.is_valid:
            form.save()
            print("player saved")
            return HttpResponseRedirect('/../../player/showPlayers')
        else:
            print("not saved")
    context = {'form':form}
    return render(request, "players_form.html", context)

def deletePlayer(request, id):
    player = Players.objects.get(pk=id)
    context = {'player': player}
    print(player)

    if request.method == "POST":
        player.delete()
        print("player deleted")
        return HttpResponseRedirect('/../../player/showPlayers')

    return render(request, "delete_player.html", context)

def goToScore(request):
    context={}

    return render(request, "court.html", context)

def chooseGame(request):
    context={}

    return render(request, "games_board.html", context)

def teamStats(request, id):
    team = Teams.objects.get(pk=id)
    print(team.team_name)
    # context = {'team_stats':Teams.objects.get(id=id)}
    context = {'team': team}

    return render(request, "team_stats.html", context)

def teamStats_form(request):
    form = TeamStatsForm(request.POST or None)
    if form.is_valid():
        fieldGoals = form.cleaned_data.get('field_goals')
        fieldGoalsAttempts = form.cleaned_data.get('field_goal_attempts')

        point3Goals = form.cleaned_data.get('three_point_field_goal')
        point3GoalAttempts = form.cleaned_data.get('three_point_field_goal_attempts')

        point2Goals = form.cleaned_data.get('two_point_field_goal')
        point2GoalAttempts = form.cleaned_data.get('two_point_field_goal_attempts')

        freeThrow = form.cleaned_data.get('free_throws')
        freeThrowAttempts = form.cleaned_data.get('free_throw_attempts')

        defensiveRebounds = form.cleaned_data.get('defensive_rebounds')
        offensiveRebounds = form.cleaned_data.get('offensive_rebounds')

        instance = form.save(commit=False)
        # percentage = str(fieldGoals / fieldGoalsAttempts *100) + '%'
        percentage = fieldGoals/fieldGoalsAttempts *100
        point3Percentage = point3Goals/point3GoalAttempts *100
        point2Percentage = point2Goals / point2GoalAttempts * 100
        freeThrowPercentage = freeThrow/freeThrowAttempts *100
        totalRebounds = defensiveRebounds + offensiveRebounds

        instance.field_goal_percentage = percentage
        instance.three_point_field_goal_percentage = point3Percentage
        instance.two_point_field_goal_percentage = point2Percentage
        instance.free_throw_percentage = freeThrowPercentage
        instance.total_rebounds = totalRebounds

        # print(request.POST)
        # print(form.cleaned_data)
        # print(teamName)
        print('saved')
        instance.save()
        form.save()
        return HttpResponseRedirect('../../')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "team_stats_form.html", context)