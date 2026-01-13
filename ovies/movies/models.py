from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel


class Genre(models.Model):
    """
    Модель жанра фильма
    """
    name = models.CharField(
        _('Название жанра'),
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(TimeStampedModel):
    """
    Модель фильма
    """
    title = models.CharField(
        _('Название фильма'),
        max_length=255
    )
    director = models.CharField(
        _('Режиссёр'),
        max_length=255
    )
    release_year = models.PositiveIntegerField(
        _('Год выпуска'),
        db_index=True,
        validators=[MinValueValidator(1888), MaxValueValidator(2100)]
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Жанр')
    )
    description = models.TextField(
        _('Описание'),
        blank=True
    )
    poster = models.ImageField(
        _('Постер'),
        upload_to='movie_posters/',
        null=True,
        blank=True
    )
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='movies',
        verbose_name=_('Добавил пользователь')
    )

    class Meta:
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')
        ordering = ['-created_at']
        unique_together = ['title', 'director', 'release_year']

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    @property
    def average_rating(self):
        """
        Рассчитывает средний рейтинг фильма
        """
        from django.db.models import Avg
        result = self.reviews.aggregate(average=Avg('rating'))
        return result['average'] or 0

    @property
    def review_count(self):
        """
        Возвращает количество отзывов
        """
        return self.reviews.count()