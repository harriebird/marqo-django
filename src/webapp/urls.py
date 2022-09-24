from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies_list, name='movies_list'),
    path('movies/page/<int:page>/', views.movies_list, name='movies_list'),
    path('movies/<int:movie_id>/', views.movie_details, name='movie_detail'),
    path('search/', views.search, name='search')
]
