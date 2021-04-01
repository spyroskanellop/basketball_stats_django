from django.forms import ModelForm
from .models import Teams, Players, Scores

class TeamsForm(ModelForm):
    class Meta:
        model = Teams
        fields = "__all__"

class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = "__all__"

class ScoresForm(ModelForm):
    class Meta:
        model = Scores
        fields = "__all__"