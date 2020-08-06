from django.urls import path

from . import views

urlpatterns = [
    path("", views.api_overview, name="api-overview"),
    path("entries/", views.entries_list, name="entries-list"),
    path("entries/<str:title>", views.entry_detail, name="entry-detail"),
]
