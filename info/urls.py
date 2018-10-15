__author__ = 'AIZOH'
from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [

    path(r'register/', views.index, name='index'),
    path(r'', views.first, name='first'),
]