from django.contrib import admin
from django.urls import path
import core.views as views

urlpatterns = [
    path('', views.index, name='index' ),
    path('<str:area>/', views.index, name='index' ),
]