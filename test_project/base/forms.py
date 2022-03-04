from django import forms
from .models import Movie, Review, RATE_CHOICE

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 's_description', 'description', 'video_url', 'movie_genre', 'thumbnail')

class ReviewForm(forms.ModelForm):
    
    rate = forms.ChoiceField(choices=RATE_CHOICE, widget=forms.Select(), required=True)

    class Meta:
        model = Review
        fields = ('rate',);