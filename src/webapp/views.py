from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import marqo
from django.conf import settings
from .models import Movie, Genre


def index(request):
    movie_objects = Movie.objects.all().order_by('-year', 'title')
    paginator = Paginator(movie_objects, per_page=40)
    data = paginator.page(1)
    return render(request, 'webapp/index.html', {'movies': data})


def movies_list(request, page=1):
    movie_objects = Movie.objects.all().order_by('-year', 'title')
    paginator = Paginator(movie_objects, per_page=40)
    data = paginator.page(page)
    return render(request, 'webapp/movie_list.html', {'movies': data})


def movie_details(request, movie_id=1):
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie:
        mq = marqo.Client(settings.MARQO_URL)
        suggested = mq.index('movies-index').search(q=movie.get_genres(), searchable_attributes=['genres'], limit=40)
        movie.suggested = suggested['hits']
    return render(request, 'webapp/movie_details.html', {'movie': movie})


def search(request):
    term = request.GET['term'] if 'term' in request.GET.keys() else ''
    if 'genre' in request.GET.keys():
        additional_filter = 'genres:{}'.format(request.GET['genre'])
    elif 'year' in request.GET.keys():
        additional_filter = 'year:{}'.format(request.GET['year'])
    else:
        additional_filter = None

    mq = marqo.Client(settings.MARQO_URL)
    results = mq.index('movies-index').search(q=term, filter_string=additional_filter, limit=40)
    return render(request, 'webapp/search.html', {'results': results})
