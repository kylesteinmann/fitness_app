from django.urls import path

from . import views

app_name = 'exercise'

urlpatterns = [
    path('create_exercise/', views.CreateExercise.as_view(), name='create_exercise'),
    path('update_exercise/<int:pk>/', views.UpdateExercise.as_view(), name='update_exercise'),
    path('list_exercise', views.ListExercise.as_view(), name='list_exercise'),
    path('delete_exercise/<int:pk>/', views.DeleteExercise.as_view(), name='delete_exercise'),
    
    path('create_routine/', views.CreateRoutineView.as_view(), name='create_routine'),
    path('update_routine/<int:pk>/', views.UpdateRoutine.as_view(), name='update_routine'),
    path('list_routine', views.ListRoutine.as_view(), name='list_routine'),
    path('delete_routine/<int:pk>/', views.DeleteRoutine.as_view(), name='delete_routine'),

   
    
]
