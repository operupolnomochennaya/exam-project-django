from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel
from movies.models import Movie


class Collection(TimeStampedModel):
    """
    Модель подборки фильмов
    """
    title = models.CharField(
        _('Название подборки'),
        max_length=255
    )
    description = models.TextField(
        _('Описание подборки'),
        blank=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='collections',
        verbose_name=_('Создатель')
    )
    movies = models.ManyToManyField(
        Movie,
        related_name='collections',
        verbose_name=_('Фильмы'),
        blank=True
    )
    is_public = models.BooleanField(
        _('Публичная подборка'),
        default=True,
        help_text=_('Если отмечено, подборка будет видна всем пользователям')
    )

    class Meta:
        verbose_name = _('Подборка фильмов')
        verbose_name_plural = _('Подборки фильмов')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def movie_count(self):
        """
        Возвращает количество фильмов в подборке
        """
        return self.movies.count()