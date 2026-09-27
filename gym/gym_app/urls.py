from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('participants',views.create_participant),
]
