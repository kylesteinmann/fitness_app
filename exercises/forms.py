from django import forms
from .models import Exercise
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
