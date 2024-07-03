from django.contrib import admin
from django.urls import path,include
from Login_app import views

urlpatterns = [
   path('',views.index),
   path('signup/',views.signup),
]
