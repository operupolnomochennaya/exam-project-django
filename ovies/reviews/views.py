from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from .models import Review
from .forms import ReviewForm
from movies.models import Movie
from core.mixins import OwnerRequiredMixin


class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Представление для создания отзыва
    """
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_message = _('Отзыв успешно добавлен')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = get_object_or_404(Movie, pk=self.kwargs['movie_pk'])
        return context

    def form_valid(self, form):
        movie = get_object_or_404(Movie, pk=self.kwargs['movie_pk'])
        form.instance.movie = movie
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movies:movie_detail', kwargs={'pk': self.kwargs['movie_pk']})


class ReviewUpdateView(OwnerRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Представление для редактирования отзыва
    """
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_message = _('Отзыв успешно обновлен')

    def get_success_url(self):
        return reverse_lazy('movies:movie_detail', kwargs={'pk': self.object.movie.pk})


class ReviewDeleteView(OwnerRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Представление для удаления отзыва
    """
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_message = _('Отзыв успешно удален')

    def get_success_url(self):
        return reverse_lazy('movies:movie_detail', kwargs={'pk': self.object.movie.pk})