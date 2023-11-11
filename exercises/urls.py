from django.urls import path
from . import views

app_name = 'exercise'

urlpatterns = [
    path('create/', views.CreateExercise.as_view(), name='create_exercise'),
    path('update/<int:pk>/', views.UpdateExercise.as_view(), name='update_exercise'),
    path('', views.ListExercise.as_view(), name='list_exercise'),
]
