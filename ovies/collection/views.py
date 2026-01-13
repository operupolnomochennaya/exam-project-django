from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Collection
from .forms import CollectionForm
from core.mixins import OwnerRequiredMixin


class CollectionListView(ListView):
    """
    Представление для списка подборок
    """
    model = Collection
    template_name = 'collections/collection_list.html'
    context_object_name = 'collections'
    paginate_by = 12

    def get_queryset(self):
        queryset = Collection.objects.filter(is_public=True).select_related('creator')
        return queryset


class CollectionDetailView(DetailView):
    """
    Представление для детального просмотра подборки
    """
    model = Collection
    template_name = 'collections/collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.object.movies.all()
        return context


class CollectionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Представление для создания подборки
    """
    model = Collection
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_message = _('Подборка успешно создана')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class CollectionUpdateView(OwnerRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Представление для редактирования подборки
    """
    model = Collection
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_message = _('Подборка успешно обновлена')


class CollectionDeleteView(OwnerRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Представление для удаления подборки
    """
    model = Collection
    template_name = 'collections/collection_confirm_delete.html'
    success_url = reverse_lazy('collections:collection_list')
    success_message = _('Подборка успешно удалена')