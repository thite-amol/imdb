from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MoviesSerializer

# Create your views here.


class MovieCreateView(viewsets.generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    partial = True


class MoviesListView(viewsets.generics.ListAPIView):
    queryset = Movie.objects.all().order_by("name")
    serializer_class = MoviesSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get("name", None)
        if name is not None:
            qs = qs.filter(name__icontains=name)

        genre = self.request.query_params.get("genre", None)
        if genre is not None:
            qs = qs.filter(genre__name__icontains=genre)

        director = self.request.query_params.get("director", None)
        if director is not None:
            qs = qs.filter(director__icontains=director)

        return qs


class MovieRUDView(viewsets.generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    partial = True

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))
