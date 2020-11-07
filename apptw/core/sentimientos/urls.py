from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('sentimientos/', views.Sentimientos_View.as_view(), name='Sentimientos'),

]
