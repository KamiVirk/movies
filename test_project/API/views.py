from base.models import Movie, Review
from .serializers import MovieSerializer, MovieRateSerializer, ProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import Profile

class MovieApi(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class MovieReview(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = MovieRateSerializer
    permission_classes = [IsAuthenticated]


class UserProfile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
