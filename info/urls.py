__author__ = 'AIZOH'
from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    path(r'', views.index, name='index'),

]