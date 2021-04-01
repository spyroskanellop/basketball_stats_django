from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect
from run.models import Teams
from .forms import TeamsForm, PlayersForm, ScoresForm


# Create your views here.
def home(request):
    return HttpResponse('Hello from home')

def team(request):
    if request.method == 'POST':
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
    form = TeamsForm()
    if request.method == 'POST':
        form = TeamsForm(request.POST)
        if form.is_valid():
            print('saved')
            form.save()
        else:
            print('not saved')
    else:
        print('not inside post')
    context = {'form': form}

    return render(request, "teams_form.html", context)

def team_list(request):
    context = {'team_list':Teams.objects.all()}
    return render(request, "teams_list.html", context)

def team_del(request):
    return render(request, "teams_list.html")

# def player_form(request):
#     form = PlayersForm()
#     return render(request, "players_form.html", {'form':form})
#

def admin(request):
    return render(request, 'admin.html')
