from rest_framework import serializers
from base.models import Movie, Review
from users.models import Profile

class MovieSerializer(serializers.ModelSerializer):
    movie_genre = serializers.StringRelatedField(many=False)

    class Meta:
        model = Movie
        fields = ['name', 's_description', 'description', 'video_url', 'movie_genre', 'thumbnail']


class MovieRateSerializer(serializers.ModelSerializer):
    #movie = serializers.StringRelatedField(many=False, read_only=False)

    class Meta:
        model = Review
        fields = ['rate', 'movie', 'r_host']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image']