from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer

# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
