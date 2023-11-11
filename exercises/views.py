from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise
from .forms import ExerciseForm
from django.views.generic import ListView


class CreateExercise(CreateView):
    model = Exercise
    success_url = reverse_lazy('exercise:list_exercise')
    template_name = 'exercises/create_exercise.html'
    form_class = ExerciseForm


class UpdateExercise(UpdateView):
    model = Exercise
    success_url = reverse_lazy('exercise:list_exercise')
    template_name = 'exercises/update_exercise.html'
    form_class = ExerciseForm


class ListExercise(ListView):
    model = Exercise
    template_name = 'exercises/list_exercise.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["exercises"] = Exercise.objects.all()

        return context


class DeleteExercise(DeleteView):
    model = Exercise
    success_url = reverse_lazy('exercise:list_exercise')
    template_name = 'exercises/delete_exercise.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["exercises"] = Exercise.objects.all()

        return context
