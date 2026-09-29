from django.urls import path
from . import views

urlpatterns = [
    path('', views.createuser),
    path('viewuser',views.viewuser),
    path('deleteuser/<int:user_id>',views.delete_user),
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
    path('users', views.index),
]
