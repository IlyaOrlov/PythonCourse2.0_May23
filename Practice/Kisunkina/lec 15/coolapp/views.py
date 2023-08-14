

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render
from .models import Film
from .templates.coolapp.forms import FilmForm
from django.shortcuts import redirect


def index(request):
    return render(request, 'coolapp/index.html')

def films(request):
    return render(request, 'coolapp/films.html',
                  {'films': Film.objects.all()})

# def new(request):
#     return render(request, 'coolapp/new.html', {'form': FilmForm()})

def new(request, film_id=None):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect(f'/{film.id}', film=film)
    if film_id:
        film = Film.objects.get(id=film_id)
    else:
        film = Film()
    return render(request, 'coolapp/new.html',
                  {'form': FilmForm(instance=film)})

def index(request):
    return render(request, 'coolapp/index.html', {'sitename': 'О хороших фильмах'})






