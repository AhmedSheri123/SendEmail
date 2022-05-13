from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path("", views.sender, name="sender")
]