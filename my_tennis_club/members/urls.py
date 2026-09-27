from django.urls import path
from . import views

urlpatterns = [
    #url for members application
    path('members/', views.members, name='members'),
    path('members/details/<int:id>/',views.details,name='details'),
 
]