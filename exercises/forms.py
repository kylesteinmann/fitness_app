from django import forms
from .models import Exercise, Routine
from datetime import datetime


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'repetitions', 'sets',
                  'weight', 'incremental_weight']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'repetitions': forms.NumberInput(attrs={'class': 'form-control'}),
            'sets': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'incremental_weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'exercises']

    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
