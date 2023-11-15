from django import forms
from .models import Routine
from exercises.models import Exercise


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'exercises']

    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
