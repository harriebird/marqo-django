from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    imdb_id = models.CharField(max_length=10)
    tmdb_id = models.CharField(max_length=8)

    def __str__(self):
        return self.title

    def get_genres(self):
        return ', '.join([str(p) for p in self.genres.all()])

    get_genres.short_description = 'Genre'
