from django.urls import path
from . import views


app_name = 'routine'

urlpatterns = [


    path('create/', views.CreateRoutineView.as_view(), name='create_routine'),
    path('update/<int:pk>/', views.UpdateRoutine.as_view(), name='update_routine'),
    path('', views.ListRoutine.as_view(), name='list_routine'),
    path('delete/<int:pk>/', views.DeleteRoutine.as_view(), name='delete_routine'),

]
