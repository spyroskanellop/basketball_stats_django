from django import forms
from .models import Teams, Players, Scores, TeamStats, PlayerStats

# class TeamsForm(ModelForm):
#     class Meta:
#         model = Teams
#         fields = "__all__"
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
    # dominant_hand = forms.ChoiceField(choices=DOMINANT_HAND, widget=forms.Select(attrs={'class':'select-box'}))
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
    class Meta:
        model = TeamStats
        exclude=['field_goal_percentage', 'three_point_field_goal_percentage', 'two_point_field_goal_percentage', 'free_throw_percentage', 'total_rebounds']
        fields = "__all__"
        # fields = ['games',
        # 'score']
        labels = {
            'games': 'Games played',
            'fields_goals': 'field goals',
            'field_goal_attempts': 'field goal attempts',
            'three_point_field_goal': '3 point field goal',
            'three_point_field_goal_attempts': '3 point field goal attempts',
            'two_point_field_goal': '2 point field goal',
            'two_point_field_goal_attempts': '2 point field goal attempts',
            'free_throws': 'free throws',
            'free_throw_attempts': 'free throw attempts',
            'offensive_rebounds': 'offensive rebounds',
            'defensive_rebounds': 'defensive rebounds',
            'assists': 'assists',
            'steals': 'steals',
            'blocks': 'blocks',
            'turnovers': 'turnovers',
            'personal_fouls': 'personal_fouls',
            'points': 'points',
            'teamID': 'Team id(number)',
        }

    def clean_field_goals(self):
        field_goals = self.cleaned_data.get('field_goals')
         # check if input has numbers
        return field_goals


class PlayerStatsForm(forms.ModelForm):
    class Meta:
        model = PlayerStats
        exclude = ['field_goal_percentage', 'three_point_field_goal_percentage', 'two_point_field_goal_percentage',
                   'free_throw_percentage', 'total_rebounds']
        fields = "__all__"
        labels = {
            'games': 'Games played',
            'fields_goals': 'field goals',
            'field_goal_attempts': 'field goal attempts',
            'three_point_field_goal': '3 point field goal',
            'three_point_field_goal_attempts': '3 point field goal attempts',
            'two_point_field_goal': '2 point field goal',
            'two_point_field_goal_attempts': '2 point field goal attempts',
            'free_throws': 'free throws',
            'free_throw_attempts': 'free throw attempts',
            'offensive_rebounds': 'offensive rebounds',
            'defensive_rebounds': 'defensive rebounds',
            'assists': 'assists',
            'steals': 'steals',
            'blocks': 'blocks',
            'turnovers': 'turnovers',
            'personal_fouls': 'personal_fouls',
            'points': 'points',
            'teamID': 'Team id(number)',
        }