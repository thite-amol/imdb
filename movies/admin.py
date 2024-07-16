from django.contrib import admin

# Register your models here.
from movies.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)
