import sys
import os
import re
import pandas as pd
import django
from pathlib import Path
REPO_DIR = Path(__file__).resolve().parent.parent
sys.path.append('{}/src'.format(REPO_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marqodjango.settings')
django.setup()

from webapp.models import Movie, Genre

print('Loading dataset...')
movies_df = pd.read_csv('{}/movies.csv'.format(REPO_DIR))
links_df = pd.read_csv('{}/links.csv'.format(REPO_DIR))

merged_df = pd.merge(movies_df, links_df, on='movieId', how='inner')
print('Dataset successfully loaded...')

for movie in merged_df.itertuples(index=False):
    title = re.compile(r'(?:\((\d{4})\))?\s*$').sub('', movie.title).strip()
    year = re.compile(r'(?:\((\d{4})\))?\s*$').search(movie.title).group(1)
    if year is None:
        continue

    genres = movie.genres.split('|')

    new_movie = Movie(title=title, year=year)

    try:
        # link = links_df.loc[links_df['movieId'] == movie['movieId']]
        new_movie.imdb_id = movie.imdbId
        new_movie.tmdb_id = int(movie.tmdbId)
        new_movie.save()
    except ValueError:
        continue

    if not genres[0] == '(no genres listed)':
        for genre in genres:
            try:
                genre_model = Genre.objects.get(name=genre)
            except Genre.DoesNotExist:
                genre_model = Genre(name=genre)
                genre_model.save()
            new_movie.genres.add(genre_model)

    new_movie.save()

    print('{} - {} was successfully added'.format(movie.movieId, title))

print('Dataset import was successful!')
