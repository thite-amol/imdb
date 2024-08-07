from django.db import models

# Create your models here.


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

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

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
