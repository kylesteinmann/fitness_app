from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise, Routine, RoutineExercise
from .forms import ExerciseForm, RoutineForm
from django.views.generic import ListView
from django.forms import inlineformset_factory

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

class CreateRoutineView(CreateView):
    model = Routine
    template_name = 'routines/create_routine.html'
    form_class = RoutineForm
    success_url = reverse_lazy('exercise:list_routine')

class UpdateRoutine(UpdateView):
    model = Routine
    success_url = reverse_lazy('exercise:list_routine')
    template_name = 'routines/update_routine.html'
    form_class = RoutineForm

class ListRoutine(ListView):
    model = Routine
    template_name = 'routines/list_routine.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()
        context["routine_exercises"] = RoutineExercise.objects.all()

        return context

class DeleteRoutine(DeleteView):
    model = Routine
    success_url = reverse_lazy('exercise:list_routine')
    template_name = 'routines/delete_routine.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()

        return context

