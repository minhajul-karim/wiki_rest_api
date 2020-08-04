from django.urls import path

from . import views

urlpatterns = [
    path("entries", views.index, name="index"),
    path("entries/<str:title>", views.display_entry, name="display_entry"),
]
