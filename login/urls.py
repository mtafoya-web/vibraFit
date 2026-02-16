from django.urls import path
from . import views

#Define the URLconf for the polls app
urlpatterns = [
    path("", views.index, name="index"),
]