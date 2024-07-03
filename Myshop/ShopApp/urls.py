from django.contrib import admin
from django.urls import path,include
from ShopApp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('shop/',views.shop),
    path('contact/',views.contact),
]