from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from run.models import Teams, Players, TeamStats, PlayerStats, AverageTeamStats, AveragePlayerStats
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
        print(request.POST)
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
        # print(teamStats.teamID)
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
        return HttpResponseRedirect('../../showTeams')
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
        return HttpResponseRedirect('../../showTeams')
    else:
        print(form.errors)
        print('not saved')
    context = {'form': form}
    return render(request, "team_stats_form.html", context)

def createAvgTeamStats(request):
    teamStats = TeamStats.objects.all()
    averageTeamStats = AverageTeamStats.objects.all()

    if averageTeamStats:
        averageTeamStats.delete()
        print('delete all')
    games = 0
    assists = 0
    fieldGoals = 0
    defensiveRebounds = 0
    offensiveRebounds = 0
    steals = 0
    turnovers = 0
    blocks = 0
    points = 0
    counter = 0

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
        counter += 1

    print(counter)
    print(points)
    averageTeamStats = AverageTeamStats()
    averageTeamStats.assists = assists/counter
    averageTeamStats.games = games/counter
    averageTeamStats.total_rebounds = 0
    averageTeamStats.steals = steals/counter
    averageTeamStats.field_goals = fieldGoals
    averageTeamStats.blocks = blocks/counter
    averageTeamStats.defensive_rebounds = defensiveRebounds/counter
    averageTeamStats.offensive_rebounds = offensiveRebounds/counter
    averageTeamStats.field_goal_attempts = 0
    averageTeamStats.field_goal_percentage = 0
    averageTeamStats.free_throw_attempts = 0
    averageTeamStats.free_throw_percentage = 0
    averageTeamStats.free_throws = 0
    averageTeamStats.personal_fouls = 0
    averageTeamStats.points = points/counter
    averageTeamStats.three_point_field_goal = 0
    averageTeamStats.three_point_field_goal_attempts = 0
    averageTeamStats.three_point_field_goal_percentage = 0
    averageTeamStats.turnovers = turnovers/counter
    averageTeamStats.two_point_field_goal = 0
    averageTeamStats.two_point_field_goal_attempts = 0
    averageTeamStats.two_point_field_goal_percentage = 0

    averageTeamStats.save()
    return HttpResponseRedirect('../')

def createAvgPlayerStats(request):
    playerStats = PlayerStats.objects.all()
    averagePlayerStats = AveragePlayerStats.objects.all()
    if not playerStats:
        averagePlayerStats.delete()
    games = 0
    assists = 0
    fieldGoals = 0
    defensiveRebounds = 0
    offensiveRebounds = 0
    steals = 0
    turnovers = 0
    blocks = 0
    points = 0
    counter = 0

    for x in playerStats:
        assists += x.assists
        fieldGoals += x.field_goals
        defensiveRebounds += x.defensive_rebounds
        offensiveRebounds += x.offensive_rebounds
        turnovers += x.turnovers
        steals += x.steals
        blocks += x.blocks
        points += x.points
        games += x.games
        counter += 1

    averagePlayerStats = AveragePlayerStats()
    averagePlayerStats.assists = assists/counter
    averagePlayerStats.games = games/counter
    averagePlayerStats.total_rebounds = 0
    averagePlayerStats.steals = steals/counter
    averagePlayerStats.field_goals = fieldGoals/counter
    averagePlayerStats.blocks = blocks/counter
    averagePlayerStats.defensive_rebounds = defensiveRebounds/counter
    averagePlayerStats.offensive_rebounds = offensiveRebounds/counter
    averagePlayerStats.field_goal_attempts = 0
    averagePlayerStats.field_goal_percentage = 0
    averagePlayerStats.free_throw_attempts = 0
    averagePlayerStats.free_throw_percentage = 0
    averagePlayerStats.free_throws = 0
    averagePlayerStats.personal_fouls = 0
    averagePlayerStats.points = points/counter
    averagePlayerStats.three_point_field_goal = 0
    averagePlayerStats.three_point_field_goal_attempts = 0
    averagePlayerStats.three_point_field_goal_percentage = 0
    averagePlayerStats.turnovers = turnovers/counter
    averagePlayerStats.two_point_field_goal = 0
    averagePlayerStats.two_point_field_goal_attempts = 0
    averagePlayerStats.two_point_field_goal_percentage = 0

    averagePlayerStats.save()

    return HttpResponseRedirect('../')

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
        return HttpResponseRedirect('../../showPlayers')
    else:
        print('not saved')
    context = {'form': form}
    return render(request, "player_stats_form.html", context)

def delAverageTeamStats(id):
    averageTeamStats = AverageTeamStats.objects.get(pk=id)
    averageTeamStats.delete()

    return HttpResponseRedirect('home')

def delAveragePlayerStats(id):
    averagePlayerStats = AveragePlayerStats.objects.get(pk=id)
    averagePlayerStats.delete()
    return HttpResponseRedirect('home')

def showPlayerStats(request, id):
    try:
        playerStats = PlayerStats.objects.get(playerID=id)
        players = Players.objects.get(pk=id)
        # print from teamstats table info with teamID_id = id
        context = {'playerStats': playerStats, 'players': players}
    except Exception as e:
        print(e)
        context = {}
    return render(request, "player_stats_list.html", context)

def updatePlayerStats(request, id):
    try:
        playerStats = PlayerStats.objects.get(playerID=id)
        players = Players.objects.get(pk=id)
        print('inside try')
        print('players id ' + str(players.id))
        form = PlayerStatsForm(request.POST or None, instance=playerStats)
    except Exception as e:
        print(e)
        form = PlayerStatsForm(request.POST or None)
        print('inside catch')
        players = {}

    if form.is_valid():
        # games = form.cleaned_data.get('games')
        # minutes_played = form.cleaned_data.get('minutes_played')
        print('inside form')
        print('players id ' + str(players.id))

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
        return HttpResponseRedirect('../../showPlayers')
    else:
        print('not saved')
        print(form.errors)
    context = {'form': form, 'players': players}
    return render(request, "player_stats_form.html", context)
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
        context["qs"] = TeamStats.objects.order_by('-three_point_field_goal_percentage')[:3]

        return context

class Point2ChartView(TemplateView):
    template_name = 'chart_2_point.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = TeamStats.objects.order_by('-two_point_field_goal_percentage')[:3]

        return context

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

class PointsChartView(TemplateView):
    template_name = 'chart_points.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teamstats"] = TeamStats.objects.order_by('-points')[:3]
        context["teamstatsAverage"] = AverageTeamStats.objects.all()

        return context

# --------------player views!!!
class Point3ChartPlayerView(TemplateView):
    template_name = 'chart_3_point_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-three_point_field_goal_percentage')[:5]
        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class Point2ChartPlayerView(TemplateView):
    template_name = 'chart_2_point_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["qs"] = list(chain(PlayerStats.objects.order_by('-three_point_field_goal_percentage')[:5], Players.objects.all()))
        playerStats = PlayerStats.objects.order_by('-two_point_field_goal_percentage')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class FreeThrowChartPlayerView(TemplateView):
    template_name = 'chart_free_throw_player.html'

    # playerStats = PlayerStats.objects.get(playerID=46)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-free_throw_percentage')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context
    
    
class AssistsChartPlayerView(TemplateView):
    template_name = 'chart_assists_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-assists')[:5]
        averageplayerStats = AveragePlayerStats.objects.all()

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4, 'averageplayerstats': averageplayerStats})

        return context

class OffRebChartPlayerView(TemplateView):
    template_name = 'chart_offensive_reb_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-offensive_rebounds')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class DefRebChartPlayerView(TemplateView):
    template_name = 'chart_defensive_reb_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-defensive_rebounds')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class TotalRebChartPlayerView(TemplateView):
    template_name = 'chart_total_reb_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-total_rebounds')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class StealsChartPlayerView(TemplateView):
    template_name = 'chart_steals_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-steals')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class TurnoversChartPlayerView(TemplateView):
    template_name = 'chart_turnovers_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-turnovers')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class BlocksChartPlayerView(TemplateView):
    template_name = 'chart_blocks_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-total_rebounds')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class FoulsChartPlayerView(TemplateView):
    template_name = 'chart_fouls_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-personal_fouls')[:5]

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4})

        return context

class PointsChartPlayerView(TemplateView):
    template_name = 'chart_points_player.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playerStats = PlayerStats.objects.order_by('-points')[:5]
        averagePlayerStats = AveragePlayerStats.objects.all()

        player0 = Players.objects.get(id= playerStats[0].playerID.id)
        player1 = Players.objects.get(id=playerStats[1].playerID.id)
        player2 = Players.objects.get(id=playerStats[2].playerID.id)
        player3 = Players.objects.get(id=playerStats[3].playerID.id)
        player4 = Players.objects.get(id=playerStats[4].playerID.id)

        context.update({'playerstats': playerStats, 'player0': player0, 'player1': player1, 'player2': player2, 'player3': player3, 'player4': player4, 'averagePlayerStats': averagePlayerStats})

        return context