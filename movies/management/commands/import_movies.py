import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ...models import Genre, Movie


class Command(BaseCommand):
    help = "Import the movies data from the file"

    def handle(self, *args, **options):
        print("Importing movies")
        try:
            filepath = str(settings.MEDIA_ROOT) + "/movie-data.json"
            with open(filepath) as file:
                data = json.loads(file.read())
                movie_data = {}
                for movie_item in data:
                    movie_data["popularity"] = movie_item.get("99popularity")
                    movie_data["director"] = movie_item.get("director")
                    movie_data["imdb_score"] = movie_item.get("imdb_score")
                    movie_data["name"] = movie_item.get("name")
                    movie, created = Movie.objects.get_or_create(**movie_data)
                    genre_list = movie_item.get("genre")
                    # create genre for each genre in list and attach to current movie
                    for name in genre_list:
                        name = name.strip()
                        genre, created = Genre.objects.get_or_create(name=name)
                        movie.genre.add(genre)
                    movie.save()
            print("Imported movies")
        except Exception as inst:
            raise CommandError(inst)
