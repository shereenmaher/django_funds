from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index),
    path('result/',views.show),
    path('temp/',views.temp),
    path('', views.index),
    path('/new', views.new),

]
