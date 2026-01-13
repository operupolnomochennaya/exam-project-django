from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Movie

class MovieForm(forms.ModelForm):
    """
    Форма для создания и редактирования фильмов
    """
    class Meta:
        model = Movie
        fields = [
            'title',
            'director',
            'release_year',
            'genre',
            'description',
            'poster'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'release_year': forms.NumberInput(attrs={'min': 1888}),
        }
        labels = {
            'title': _('Название фильма'),
            'director': _('Режиссёр'),
            'release_year': _('Год выпуска'),
            'genre': _('Жанр'),
            'description': _('Описание'),
            'poster': _('Постер'),
        }