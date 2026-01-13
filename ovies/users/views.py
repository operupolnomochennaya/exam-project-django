from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('movies:movie_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(self.request, _('Регистрация прошла успешно!'))
        return response


@login_required
def profile_view(request):
    """
    Представление профиля пользователя
    """
    user_movies = request.user.movies.all()
    user_reviews = request.user.reviews.all()
    user_collections = request.user.collections.all()

    context = {
        'user_movies': user_movies,
        'user_reviews': user_reviews,
        'user_collections': user_collections,
    }

    return render(request, 'users/profile.html', context)