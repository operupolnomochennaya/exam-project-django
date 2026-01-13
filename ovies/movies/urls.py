from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
]