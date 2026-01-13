from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie_count')
    search_fields = ('name',)

    def movie_count(self, obj):
        return obj.movie_set.count()

    movie_count.short_description = _('Количество фильмов')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'director',
        'release_year',
        'genre',
        'added_by',
        'created_at',
        'average_rating_display'
    )
    list_filter = ('genre', 'release_year', 'created_at')
    search_fields = ('title', 'director', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (_('Основная информация'), {
            'fields': ('title', 'director', 'release_year', 'genre', 'poster')
        }),
        (_('Описание'), {
            'fields': ('description',)
        }),
        (_('Метаданные'), {
            'fields': ('added_by', 'created_at', 'updated_at')
        }),
    )

    def average_rating_display(self, obj):
        return f'{obj.average_rating:.1f}'

    average_rating_display.short_description = _('Средний рейтинг')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.added_by = request.user
        super().save_model(request, obj, form, change)