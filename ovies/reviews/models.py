from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel
from movies.models import Movie


class Review(TimeStampedModel):
    """
    Модель отзыва и рейтинга фильма
    """
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Фильм')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Пользователь')
    )
    rating = models.PositiveSmallIntegerField(
        _('Рейтинг'),
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text=_('Оценка от 1 до 5')
    )
    text = models.TextField(
        _('Текст отзыва'),
        blank=True
    )

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
        ordering = ['-created_at']
        unique_together = ['movie', 'user']

    def __str__(self):
        return f'Отзыв {self.user.username} на {self.movie.title}'