from django.db import models
from django.http import request

# Create your models here.


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400, null=True)
    popularity = models.FloatField(default=0)
    imdb_score = models.FloatField(default=0)
    director = models.CharField(max_length=400, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
