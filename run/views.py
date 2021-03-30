from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect
from run.forms import TeamsForm, PlayersForm


# Create your views here.
def home(request):
    return HttpResponse('Hello from home')

def team(request):
    if request.method == "POST":
        form = TeamsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = TeamsForm()
    return render(request, 'teams_form.html', {'form':form})

def team_form(request):
    if request.method == "GET":
        form = TeamsForm()
        return render(request, "teams_form.html", {'form': form})
    else :
        form = TeamsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/team/showTeams')

def team_list(request):
    return render(request, "teams_list.html")

def team_del(request):
    return render(request, "teams_list.html")

def player_form(request):
    form = PlayersForm()
    return render(request, "players_form.html", {'form':form})


def admin(request):
    return render(request, 'admin.html')
