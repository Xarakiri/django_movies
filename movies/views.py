from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Movie


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


class MovieDetailView(View):
    """Полное описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})

