from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.search, name="search"),
    path("wiki/<str:name>", views.content, name="content"),
    path("add", views.add_page, name="add"),
    path("edit", views.edit, name="edit"),
    path("save", views.save, name="saveEdit"),
    path("random", views.randomPage, name="rando")
]
