from django.shortcuts import render
from django.views.generic import CreateView
from .models import Routine
from .forms import RoutineForm
from django.urls import reverse_lazy


class CreateRoutineView(CreateView):
    model = Routine
    template_name = 'routines/create_routine.html'
    form_class = RoutineForm
    success_url = reverse_lazy('routine:create_routine')
