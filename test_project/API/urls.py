from django.urls import path, include
from .views import MovieApi, MovieReview, UserProfile
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('review', MovieReview, basename='review')
router.register('movieapi', MovieApi, basename='movieapi')
router.register('profileapi', UserProfile, basename='profileapi')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
