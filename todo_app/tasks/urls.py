from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('update/<str:pk>/', views.update_task, name='update'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]
