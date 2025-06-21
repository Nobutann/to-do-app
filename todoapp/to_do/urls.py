from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('uptade-task/<str:pk>/', views.updateTask, name="uptade-task"),
]