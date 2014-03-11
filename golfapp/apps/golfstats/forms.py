from django import forms

from golfapp.apps.golfstats.models import Golfer, GolfCourse

class GolferForm(forms.ModelForm):
    class Meta:
        model = Golfer 

class GolfCourseForm(forms.ModelForm):
    class Meta:
        model = GolfCourse
