from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre


class Movie(models.Model):
    thumbnail = models.ImageField(default='default.png', upload_to='thumbnails')
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    s_description = models.TextField(null=True, blank=True)
    movie_genre = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    video_url = models.URLField(max_length=200)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})


RATE_CHOICE = [
    (1, '1 - Trash'),
    (2, '2 - Terrible'),
    (3, '3 - Horrible'),
    (4, '4 - Bad'),
    (5, '5 - Ok'),
    (6, '6 - Watchable'),
    (7, '7 - Good'),
    (8, '8 - Very Good'),
    (9, '9 - Perfect'),
    (10, '10 - Master Piece')
]


class Review(models.Model):
    r_host = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICE)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.r_host.username
