from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from run.models import Teams, Players, TeamStats, PlayerStats, AverageTeamStats
from .forms import TeamsForm, PlayersForm, ScoresForm, TeamStatsForm, PlayerStatsForm, AverageTeamStatsForm
from itertools import chain

def home(request):
    return render(request, 'admin.html')

def admin(request):
    return render(request, 'admin.html')

def createTeam(request):
    form = TeamsForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        print('saved')
        form.save()
        return HttpResponseRedirect('showTeams')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "add_team_form.html", context)

def updateTeam(request, id):
    team = Teams.objects.get(pk=id)
    form = TeamsForm(instance=team)
    print(form)
    if request.method == 'POST':
        form = TeamsForm(request.POST, instance=team)
        if form.is_valid():
            print('saved')
            form.save()
            return HttpResponseRedirect('/../../team/showTeams')
        else:
            print('not updated')

    context = {'form': form}
    return render(request, "add_team_form.html", context)

def viewTeam(request):
    context = {'team_list':Teams.objects.all()}
    return render(request, "teams_list.html", context)

def deleteTeam(request, id):
    team = Teams.objects.get(pk=id)
    team.delete()
    return HttpResponseRedirect('/../../team/showTeams')

def createPlayer2(request):
    form = PlayersForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('saved')
        return HttpResponseRedirect('/../player/showPlayers')
    else:
        print('not saved')
    context = {'form': form}

    return render(request, "add_player_form.html", context)


def viewPlayer(request):
    # context= {'player_list':Players.objects.all()}

    player_list = Players.objects.all()
    team_list = Teams.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(player_list, 10)
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)

    return render(request, "players_list.html", {'players': players, 'team_list': team_list})

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
    return render(request, "add_player_form.html", context)

def deletePlayer(request, id):
    player = Players.objects.get(pk=id)
    player.delete()
    return HttpResponseRedirect('/../../player/showPlayers')

def goToScore(request):
    context={}

    return render(request, "court.html", context)

def chooseGame(request):
    context={}

    return render(request, "games_board.html", context)

def teamStats(request, id):
    try:
        teamStats = TeamStats.objects.get(teamID_id=id)
        # print from teamstats table info with teamID_id = id
        context = {'teamStats': teamStats}
    except Exception as e:
        print(e)
        context = {}
    return render(request, "team_stats_list.html", context)

def updateTeamStats(request, id):
    try:
        teamStats = TeamStats.objects.get(pk=id)
        form = TeamStatsForm(request.POST or None, instance=teamStats)
    except Exception as e:
        print(e)
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

        print('saved')
        instance.save()
        form.save()
        return HttpResponseRedirect('../../../')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "team_stats_form.html", context)

def createTeamStats(request):

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

        print('saved')
        instance.save()
        form.save()
        return HttpResponseRedirect('../../../')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "team_stats_form.html", context)

def createAvgTeamStats(request):
    teamStats = TeamStats.objects.all()
    games = 0
    assists = 0
    fieldGoals = 0
    defensiveRebounds = 0
    offensiveRebounds = 0
    steals = 0
    turnovers = 0
    blocks = 0
    points = 0

    for x in teamStats:
        assists += x.assists
        fieldGoals += x.field_goals
        defensiveRebounds += x.defensive_rebounds
        offensiveRebounds += x.offensive_rebounds
        turnovers += x.turnovers
        steals += x.steals
        blocks += x.blocks
        points += x.points
        games += x.games

    averageTeamStats = AverageTeamStats()
    averageTeamStats.assists = assists
    averageTeamStats.games = games
    averageTeamStats.total_rebounds = 0
    averageTeamStats.steals = steals
    averageTeamStats.field_goals = fieldGoals
    averageTeamStats.blocks = blocks
    averageTeamStats.defensive_rebounds = defensiveRebounds
    averageTeamStats.offensive_rebounds = offensiveRebounds
    averageTeamStats.field_goal_attempts = 0
    averageTeamStats.field_goal_percentage = 0
    averageTeamStats.free_throw_attempts = 0
    averageTeamStats.free_throw_percentage = 0
    averageTeamStats.free_throws = 0
    averageTeamStats.personal_fouls = 0
    averageTeamStats.points = points
    averageTeamStats.three_point_field_goal = 0
    averageTeamStats.three_point_field_goal_attempts = 0
    averageTeamStats.three_point_field_goal_percentage = 0
    averageTeamStats.turnovers = turnovers
    averageTeamStats.two_point_field_goal = 0
    averageTeamStats.two_point_field_goal_attempts = 0
    averageTeamStats.two_point_field_goal_percentage = 0

    averageTeamStats.save()

    context = {'assists': assists/10, 'fieldGoals': fieldGoals/10, 'defensiveRebounds': defensiveRebounds/10, 'offensiveRebounds': offensiveRebounds/10, 'turnovers': turnovers/10,  'steals': steals/10,  'blocks': blocks/10,  'points': points/10 }
    return render(request,"average_team_stats.html", context)

def createPlayerStats(request):
    form = PlayerStatsForm(request.POST or None)
    if form.is_valid():
        fieldGoals = form.cleaned_data.get('field_goals')
        fieldGoalsAttempts = form.cleaned_data.get('field_goal_attempts')

        point3Goals = form.cleaned_data.get('three_point_field_goals')
        point3GoalAttempts = form.cleaned_data.get('three_point_field_goal_attempts')

        point2Goals = form.cleaned_data.get('two_point_field_goals')
        point2GoalAttempts = form.cleaned_data.get('two_point_field_goal_attempts')

        freeThrow = form.cleaned_data.get('free_throws')
        freeThrowAttempts = form.cleaned_data.get('free_throw_attempts')

        defensiveRebounds = form.cleaned_data.get('defensive_rebounds')
        offensiveRebounds = form.cleaned_data.get('offensive_rebounds')

        instance = form.save(commit=False)
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

        print('saved')
        instance.save()
        form.save()
        return HttpResponseRedirect('../../')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "player_stats_form.html", context)


def updatePlayerStats(request, id):
    try:
        playerStats = PlayerStats.objects.get(playerID=id)
        # print from teamstats table info with teamID_id = id
        context = {'playerStats': playerStats}
    except Exception as e:
        print(e)
        context = {}
    return render(request, "player_stats_list.html", context)

def goHome(request):
    context={}

    return render(request, "home.html", context)


def goTest(request):
    form = PlayersForm(request.POST or None)
    if form.is_valid():
        print('saved')
        form.save()
        return HttpResponseRedirect('showTeams')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "checkbox.html", context)
#
# def goToButton(request):
#     context={}
#
#     return render(request, "button.html", context)
#
# def goDrag(request):
#     context = {}
#
#     return render(request, "drag.html", context)
#
#
# def goToDoughnut(request):
#     context={}
#
#     return render(request, "doughnut_chart.html", context)


class TeamChartView(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Players.objects.all()
        return context

# -------Team views!!!
class Point3ChartView(TemplateView):
    template_name = 'chart_3_point.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["qs"] = TeamStats.objects.all().filter(field_goal_percentage__gte=0.44)
        # context["qs"] = TeamStats.objects.all().filter(three_point_field_goal_percentage__gte=0.35)
        # context["qs"] = TeamStats.objects.all()[5:10]
        context["qs"] = TeamStats.objects.order_by('-three_point_field_goal_percentage')[:3]

        return context

class Point2ChartView(TemplateView):
    template_name = 'chart_2_point.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-two_point_field_goal_percentage')[:3]

        return context

# class FreeThrowChartView(TemplateView):
#     template_name = 'chart_free_throw_old.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs"] = TeamStats.objects.order_by('-free_throw_percentage')[:3]
#
#         return context

class FreeThrowChartView2(TemplateView):
    template_name = 'chart_free_throw.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-free_throw_percentage')[:3]
        return context

class DefensiveReboundChartView(TemplateView):
    template_name = 'chart_defensive_reb.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-defensive_rebounds')[:3]
        return context

class OffensiveReboundChartView(TemplateView):
    template_name = 'chart_offensive_reb.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-offensive_rebounds')[:3]
        return context

class AssistsChartView(TemplateView):
    template_name = 'chart_assists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = list(chain(TeamStats.objects.order_by('-assists')[:3], AverageTeamStats.objects.all()))
        return context

class TurnoversChartView(TemplateView):
    template_name = 'chart_turnovers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-turnovers')[:3]
        return context


class StealsChartView(TemplateView):
    template_name = 'chart_steals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-offensive_rebounds')[:3]
        return context

# --------------player views!!!
class Point3ChartPlayerView(TemplateView):
    template_name = 'chart_3_point_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["qs"] = list(chain(PlayerStats.objects.order_by('-three_point_field_goal_percentage')[:5], Players.objects.all()))
        context["qs"] = PlayerStats.objects.order_by('-three_point_field_goal_percentage')[:5]

        return context

class Point2ChartPlayerView(TemplateView):
    template_name = 'chart_2_point_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["qs"] = list(chain(PlayerStats.objects.order_by('-three_point_field_goal_percentage')[:5], Players.objects.all()))
        context["qs"] = PlayerStats.objects.order_by('-two_point_field_goal_percentage')[:5]

        return context

class FreeThrowChartPlayerView(TemplateView):
    template_name = 'chart_free_throw_player.html'

    # playerStats = PlayerStats.objects.get(playerID=46)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = PlayerStats.objects.order_by('-free_throw_percentage')[:5]

        return context
    
    
class AssistsChartPlayerView(TemplateView):
    template_name = 'chart_assists_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = PlayerStats.objects.order_by('-assists')[:5]

        return context