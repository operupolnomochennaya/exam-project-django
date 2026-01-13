from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Collection

class CollectionForm(forms.ModelForm):
    """
    Форма для создания и редактирования подборок
    """
    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'movies': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'title': _('Название подборки'),
            'description': _('Описание подборки'),
            'movies': _('Фильмы'),
            'is_public': _('Публичная подборка'),
        }