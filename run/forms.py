from django.forms import ModelForm, forms
from .models import Teams, Players, Scores

class TeamsForm(ModelForm):
    class Meta:
        model = Teams
        fields = "__all__"

class PlayersForm(ModelForm):
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

class ScoresForm(ModelForm):
    class Meta:
        model = Scores
        fields = "__all__"