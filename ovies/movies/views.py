from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .models import Movie
from .forms import MovieForm
from core.mixins import OwnerRequiredMixin


class MovieListView(ListView):
    """
    Представление для списка фильмов
    """
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 12

    def get_queryset(self):
        queryset = Movie.objects.select_related('genre', 'added_by')

        # Поиск
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(director__icontains=search_query) |
                Q(genre__name__icontains=search_query) |
                Q(release_year__icontains=search_query)
            )

        # Сортировка
        sort_by = self.request.GET.get('sort', '-created_at')
        if sort_by in ['title', 'release_year', 'created_at', '-title', '-release_year', '-created_at']:
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['sort_by'] = self.request.GET.get('sort', '-created_at')
        return context


class MovieDetailView(DetailView):
    """
    Представление для детального просмотра фильма
    """
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.select_related('user').order_by('-created_at')
        return context


class MovieCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Представление для создания нового фильма
    """
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_message = _('Фильм успешно добавлен')
    success_url = reverse_lazy('movies:movie_list')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class MovieUpdateView(OwnerRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Представление для редактирования фильма
    """
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_message = _('Фильм успешно обновлен')

    def get_success_url(self):
        return reverse_lazy('movies:movie_detail', kwargs={'pk': self.object.pk})


class MovieDeleteView(OwnerRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Представление для удаления фильма
    """
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movies:movie_list')
    success_message = _('Фильм успешно удален')