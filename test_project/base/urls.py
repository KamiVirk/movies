from django.urls import path
from . import views


urlpatterns = [
    path('', views.movielist, name='movie-list'),
    path('detail/<int:pk>/', views.MovieDetailView, name='movie-detail'),
    path('details/<int:pk>/rate', views.RateView.as_view(), name='rate-movie'),
    path('add-movie/', views.MovieCreateView.as_view(), name='add-movie'),
    path('detail/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('detail/<int:pk>/rate/', views.RateView.as_view(), name='rate-movie'),
    path('detail/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
]
   