from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('movie/<int:movie_pk>/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
]