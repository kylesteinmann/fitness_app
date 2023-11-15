from django.urls import path
from . import views


app_name = 'routine'

urlpatterns = [

    # path('', views.routines, name='routines'),
    # path('<int:pk>/update/', views.update_routine, name='update_routine'),
    path('create/', views.CreateRoutineView.as_view(), name='create_routine'),
    # path('<int:pk>/delete/', views.delete_routine, name='delete_routine'),
    # path('<int:pk>/detail/', views.detail_routine, name='detail_routine'),
]
