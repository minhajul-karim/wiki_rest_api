from django.urls import path

from . import views

urlpatterns = [
    path("wikis", views.index, name="index")
]
