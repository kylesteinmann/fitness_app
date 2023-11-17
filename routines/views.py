from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Routine
from .forms import RoutineForm
from django.urls import reverse_lazy


class CreateRoutineView(CreateView):
    model = Routine
    template_name = 'routines/create_routine.html'
    form_class = RoutineForm
    success_url = reverse_lazy('routine:list_routine')


class UpdateRoutine(UpdateView):
    model = Routine
    success_url = reverse_lazy('routine:list_routine')
    template_name = 'routines/update_routine.html'
    form_class = RoutineForm


class ListRoutine(ListView):
    model = Routine
    template_name = 'routines/list_routine.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()

        return context


class DeleteRoutine(DeleteView):
    model = Routine
    success_url = reverse_lazy('routine:list_routine')
    template_name = 'exercises/delete_exercise.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()

        return context
