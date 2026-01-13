from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Collection


class MovieInline(admin.TabularInline):
    model = Collection.movies.through
    extra = 1


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'movie_count', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'description', 'creator__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'creator', 'is_public')
        }),
        (_('Метаданные'), {
            'fields': ('created_at', 'updated_at')
        }),
    )
    inlines = [MovieInline]

    def movie_count(self, obj):
        return obj.movies.count()

    movie_count.short_description = _('Количество фильмов')