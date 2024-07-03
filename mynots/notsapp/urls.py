from django.contrib import admin
from django.urls import path
from django.urls import include
from notsapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('backend/',views.backend,name='backend'),
   path('frontend',views.frontend,name='frontend'),
   path('both/',views.both,name='both'),
   path('signup/',views.signup,name='signup'),
   path('signin/',views.signin,name='signin'),
   path('videos/',views.videos,name='videos'),
   path('programing/',views.programing,name='programing'),
   path('OTP/',views.OTP,name='OTP'),
]