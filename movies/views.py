from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name is not None:
            qs = qs.filter(name__icontains=name)

        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            qs = qs.filter(genre__name__icontains=genre)

        director = self.request.query_params.get('director', None)
        if director is not None:
            qs = qs.filter(director__icontains=director)

        return qs
