from re import search
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("randompage", views.randompage, name="randompage"),
    path("error", views.error, name= "error"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("editpage", views.edit, name="editpage"),
    path("<str:name>", views.template, name="template")

]
