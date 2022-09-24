from django.contrib import admin
from .models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'get_genres']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'view_movie_count']

    def view_movie_count(self, obj):
        return obj.movie_set.all().count()

    view_movie_count.short_description = 'Movie Count'


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
