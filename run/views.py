from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect
from run.models import Teams, Players
from .forms import TeamsForm, PlayersForm, ScoresForm


# Create your views here.
def home(request):
    return render(request, 'admin.html')

def admin(request):
    return render(request, 'admin.html')

# def team(request):
#     if request.method == 'POST':
#         form = TeamsForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/view')
#             except:
#                 pass
#     else:
#         form = TeamsForm()
#     return render(request, 'teams_form.html', {'form':form})

def createTeam(request):
    form = TeamsForm()
    if request.method == 'POST':
        form = TeamsForm(request.POST)
        if form.is_valid():
            print('saved')
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
    return render(request, "teams_form.html", context)


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
