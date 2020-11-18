from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'popularity',
                  'imdb_score', 'director', 'genre')

    def create(self, validated_data):
        genre_validated_data = validated_data.pop('genre')
        movie = Movie.objects.create(**validated_data)

        for i in genre_validated_data:
            genre, created = Genre.objects.get_or_create(name=i['name'])
            movie.add(genre)
        movie.save()

        return movie
