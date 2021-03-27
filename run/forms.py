from django import forms
from run.models import Teams, Players, Scores

class TeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = "__all__"

class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = "__all__"

class ScoresForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = "__all__"