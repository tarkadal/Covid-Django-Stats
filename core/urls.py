from django.contrib import admin
from django.urls import path
import core.views as views
from core.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('england/', views.covid_england, name='covid_england'),
    path('england/<str:area>/', views.covid_england, name='covid_england'),
]