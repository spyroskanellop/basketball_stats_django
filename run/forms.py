from django import forms
from .models import Teams, Players, Scores, TeamStats, PlayerStats, AverageTeamStats

class DateInput(forms.DateInput):
    input_type = 'date'

class TeamsForm(forms.ModelForm):

    team_name = forms.CharField(label='Team name',
                               widget=forms.TextInput(attrs={'placeholder': 'Team name', 'class': 'text'}))
    class Meta:
        model = Teams
        fields = ['team_name']

    def clean_team_name(self):
        team_name = self.cleaned_data.get('team_name')
         # check if input has numbers
        return team_name

class PlayersForm(forms.ModelForm):
    POSITION = (
        ('Point guard', 'Point guard'),
        ('Shooting guard', 'Shooting guard'),
        ('Small forward', 'Small forward'),
        ('Power forward', 'Power forward'),
        ('Center', 'Center'),
    )
    DOMINANT_HAND = (
        ('Right hand', 'Right hand'),
        ('Left hand', 'Left hand'),
    )
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number', 'class': 'inputBox'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'inputBox'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'inputBox'}))
    dob = forms.DateField(widget=DateInput)
    height = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Height', 'class': 'inputBox'}))
    weight = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Weight', 'class': 'inputBox'}))
    position = forms.ChoiceField(choices=POSITION)
    dominant_hand = forms.ChoiceField(choices=DOMINANT_HAND)

    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nationality', 'class': 'inputBox'}))
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Experience', 'class': 'inputBox'}))

    teamID = forms.ModelChoiceField(queryset=Teams.objects.all(), widget=forms.Select(attrs={'class':'inputBox'}))
    class Meta:
        model = Players
        fields = "__all__"
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'dob': 'Date of birth(mm/dd/year)',
            'position': 'Position',
            'dominant_hand': 'Dominant hand',
            'nationality': 'Nationality',
            'teamID': 'Team id(number)',
        }

class ScoresForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = "__all__"

class TeamStatsForm(forms.ModelForm):

    games = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Games played', 'class': 'inputBox'}))

    field_goals = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Field goals', 'class': 'inputBox', 'step': 0.25}))
    field_goal_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Field goal attempts', 'class': 'inputBox', 'step': 0.25}))

    three_point_field_goal = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '3 Point Field goals', 'class': 'inputBox', 'step': 0.25}))
    three_point_field_goal_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '3 Point Field goal attempts', 'class': 'inputBox', 'step': 0.25}))

    two_point_field_goal = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '2 Point Field goals', 'class': 'inputBox', 'step': 0.25}))
    two_point_field_goal_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '2 Point Field goal attempts', 'class': 'inputBox', 'step': 0.25}))

    free_throws = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Free throws made', 'class': 'inputBox', 'step': 0.25}))
    free_throw_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Free throw attempts', 'class': 'inputBox', 'step': 0.25}))

    defensive_rebounds = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Defensive Rebounds', 'class': 'inputBox', 'step': 0.25}))
    offensive_rebounds = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Offensive Rebounds', 'class': 'inputBox', 'step': 0.25}))

    assists = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Assists', 'class': 'inputBox', 'step': 0.25}))
    steals = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Steals', 'class': 'inputBox', 'step': 0.25}))
    turnovers = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Turnovers', 'class': 'inputBox', 'step': 0.25}))
    blocks = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Blocks', 'class': 'inputBox', 'step': 0.25}))
    personal_fouls = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Personal fouls', 'class': 'inputBox', 'step': 0.25}))
    points = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Points', 'class': 'inputBox', 'step': 0.25}))

    teamID = forms.ModelChoiceField(queryset=Teams.objects.all(), widget=forms.Select(attrs={'class':'inputBox'}))

    class Meta:
        model = TeamStats
        exclude=['field_goal_percentage', 'three_point_field_goal_percentage', 'two_point_field_goal_percentage', 'free_throw_percentage', 'total_rebounds']

    def clean_field_goals(self):
        field_goals = self.cleaned_data.get('field_goals')
         # check if input has numbers
        return field_goals


class PlayerStatsForm(forms.ModelForm):

    games = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Games played', 'class': 'inputBox'}))

    field_goals = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Field goals', 'class': 'inputBox', 'step': 0.25}))
    field_goal_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Field goal attempts', 'class': 'inputBox', 'step': 0.25}))

    three_point_field_goals = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '3 Point Field goals', 'class': 'inputBox', 'step': 0.25}))
    three_point_field_goal_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '3 Point Field goal attempts', 'class': 'inputBox', 'step': 0.25}))

    two_point_field_goals = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '2 Point Field goals', 'class': 'inputBox', 'step': 0.25}))
    two_point_field_goal_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '2 Point Field goal attempts', 'class': 'inputBox', 'step': 0.25}))

    free_throws = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Free throws made', 'class': 'inputBox', 'step': 0.25}))
    free_throw_attempts = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Free throw attempts', 'class': 'inputBox', 'step': 0.25}))

    defensive_rebounds = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Defensive Rebounds', 'class': 'inputBox', 'step': 0.25}))
    offensive_rebounds = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Offensive Rebounds', 'class': 'inputBox', 'step': 0.25}))

    assists = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Assists', 'class': 'inputBox', 'step': 0.25}))
    steals = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Steals', 'class': 'inputBox', 'step': 0.25}))
    turnovers = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Turnovers', 'class': 'inputBox', 'step': 0.25}))
    blocks = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Blocks', 'class': 'inputBox', 'step': 0.25}))
    personal_fouls = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Personal fouls', 'class': 'inputBox', 'step': 0.25}))
    points = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Points', 'class': 'inputBox', 'step': 0.25}))
    minutes_played = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Minutes played', 'class': 'inputBox', 'step': 0.25}))

    playerID = forms.ModelChoiceField(queryset=Players.objects.all(), widget=forms.Select(attrs={'class':'inputBox'}))

    class Meta:
        model = PlayerStats
        exclude = ['field_goal_percentage', 'three_point_field_goal_percentage', 'two_point_field_goal_percentage',
                   'free_throw_percentage', 'total_rebounds']

class AverageTeamStatsForm(forms.ModelForm):
    class Meta:
        model = AverageTeamStats
        fields = ['field_goals', 'offensive_rebounds', 'defensive_rebounds',
                   'assists', 'steals', 'turnovers', 'blocks', 'points']