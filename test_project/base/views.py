from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, CreateView

from base.decorators import staff_required
from .models import Movie, Category, Review
from django.db.models import Avg
from django.db.models import Q
from .forms import MovieForm, ReviewForm
from django.utils.decorators import method_decorator



def movielist(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''


    movie = Movie.objects.filter(Q(movie_genre__genre__icontains=q)|
    Q(name__icontains=q))
    category = Category.objects.all()
    context = {'movie': movie, 'category': category}
    return render(request, 'base/movie_list.html', context)


def MovieDetailView(request, pk):
    movie = Movie.objects.get(id=pk)
    rating = Review.objects.filter(movie=movie)
    rating_avg = rating.aggregate(Avg('rate'))

    context = {'movie': movie, 'rating_avg': rating_avg}
    return render(request, 'base/movie_detail.html', context)


class RateView(View):
    form_class = ReviewForm
    template_name = 'base/movie_rate.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, pk, *arg, **kwargs):
        rating = request.POST.get('rate')
        movie = Movie.objects.get(id=pk)
        print(movie) 
        rate = Review.objects.create(
            r_host = request.user,
            movie = movie,
            rate = rating
        )
        return redirect('movie-detail', pk=movie.id)       


@method_decorator(staff_required, name='dispatch')
class MovieCreateView(View):
    form_class = MovieForm
    template_name = 'base/movie_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        genre = Category.objects.all()
        return render(request, self.template_name, {'form': form, 'genre': genre})

    def post(self, request, *args, **kwargs):
        self.genre = request.POST.get('movie_genre')
        self.movie_genre, created = Category.objects.get_or_create(genre=self.genre)
        
        Movie.objects.create(
            host = request.user,
            movie_genre = self.movie_genre,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            thumbnail = request.FILES.get('thumbnail'),
            video_url = request.POST.get('video_url'),
            s_description = request.POST.get('s_description')
        )
        return redirect('movie-list')

 
@method_decorator(staff_required, name='dispatch')
class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'base/movie_update_form.html'
    fields = ['name', 's_description', 'description', 'video_url', 'movie_genre','thumbnail']
    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

@method_decorator(staff_required, name='dispatch')
class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/'

