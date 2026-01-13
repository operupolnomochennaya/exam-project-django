from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('movie__title', 'user__username', 'text')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('movie', 'user', 'rating')
        }),
        (_('Отзыв'), {
            'fields': ('text',)
        }),
        (_('Метаданные'), {
            'fields': ('created_at', 'updated_at')
        }),
    )