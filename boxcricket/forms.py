from datetime import date

from django.forms import ModelForm, DateField

from boxcricket.models import Game


class GameForm(ModelForm):
    date = DateField(initial=date.today(), required=True)

    class Meta:
        model = Game
        fields = ['date']
