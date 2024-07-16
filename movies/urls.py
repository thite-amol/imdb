from django.urls import path

from movies.views import MovieCreateView, MovieRUDView, MoviesListView

urlpatterns = [
    path("movies/", MoviesListView.as_view(), name="All Movies"),
    path("movie", MovieCreateView.as_view(), name="Movie"),
    path("movie/<int:pk>/", MovieRUDView.as_view(), name="Delete Movie"),
]
