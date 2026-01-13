from django.urls import path
from . import views

app_name = 'collections'

urlpatterns = [
    path('', views.CollectionListView.as_view(), name='collection_list'),
    path('<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('create/', views.CollectionCreateView.as_view(), name='collection_create'),
    path('<int:pk>/update/', views.CollectionUpdateView.as_view(), name='collection_update'),
    path('<int:pk>/delete/', views.CollectionDeleteView.as_view(), name='collection_delete'),
]