from rest_framework import generics, permissions

from .models import Manga
from .serializers import MangaSerializer

# Create your views here.


class MangaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "pk"


class MangaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
