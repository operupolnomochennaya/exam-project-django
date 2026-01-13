from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Форма для создания и редактирования отзывов
    """
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.RadioSelect(choices=[
                (1, '1 ★'),
                (2, '2 ★★'),
                (3, '3 ★★★'),
                (4, '4 ★★★★'),
                (5, '5 ★★★★★'),
            ])
        }
        labels = {
            'rating': _('Рейтинг'),
            'text': _('Текст отзыва'),
        }