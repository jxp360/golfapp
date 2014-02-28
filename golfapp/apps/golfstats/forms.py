from django import forms

from golfapp.apps.golfstats.models import Golfer

class GolferForm(forms.ModelForm):
    class Meta:
        model = Golfer 
