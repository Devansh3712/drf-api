from django.urls import path

from .views import *

urlpatterns = [
    path("", MangaListCreateAPIView.as_view(), name="manga-list"),
    path("<int:pk>", MangaRetrieveUpdateDestroyAPIView.as_view(), name="manga-detail"),
]
