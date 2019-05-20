from django.urls import path, include

from . import views

urlpatterns = [
    path('hello',views.index),
    path('',views.login),
]