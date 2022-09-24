import sys
import os
import django
import marqo
from pathlib import Path
from django.conf import settings

REPO_DIR = Path(__file__).resolve().parent.parent
sys.path.append('{}/src'.format(REPO_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marqodjango.settings')
django.setup()

from webapp.models import Movie, Genre
mq = marqo.Client(url=settings.MARQO_URL)

documents = []
movies = Movie.objects.all()

for movie in movies:
    documents.extend([{
        'id': movie.pk,
        'title': movie.title,
        'genres': movie.get_genres(),
        'year': movie.year
    }])
    print('{} - {} was added.'.format(movie.pk, movie.title))

mq.index('movies-index').add_documents(documents, device='cpu', processes=8, batch_size=100)
