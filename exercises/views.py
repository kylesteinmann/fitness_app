from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise
from .forms import ExerciseForm
from django.views.generic import ListView


class CreateExercise(CreateView):
    model = Exercise
    success_url = reverse_lazy('exercise:list_exercise')
    template_name = 'create_exercise.html'
    form_class = ExerciseForm


class UpdateExercise(UpdateView):
    model = Exercise
    success_url = reverse_lazy('exercise:list_exercise')
    template_name = 'update_exercise.html'
    form_class = ExerciseForm


class ListExercise(ListView):
    model = Exercise
    template_name = 'list_exercise.html'
