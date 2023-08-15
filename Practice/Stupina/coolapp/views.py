from django.shortcuts import render, redirect
from .models import Film, Comments
from .forms import FilmForm, CommentsForm


def index(request):
    return render(request, 'coolapp/index.html', {'sitename': 'О фильмах'})


def films(request):
    return render(request, 'coolapp/films.html', {'films': Film.objects.all()})


def new(request, film_id=None):
    if film_id:
        film = Film.objects.get(id=film_id)
        if request.method == "POST":
            text = request.POST['comment']
            c = Comments(films_id=film, comment=text)
            c.save()
            return redirect(f'/{film.id}', film=film)

        else:
            try:
                comments = Comments.objects.filter(films_id=film_id)
                return render(request, 'coolapp/film_id.html',
                          {'film': film, 'comm': comments, 'com_form': CommentsForm(instance=Comments())})
            except Exception:
                return render(request, 'coolapp/no_exit.html')

    elif request.method == "POST":
        form = FilmForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            film = form.save()
            return redirect(f'/{film.id}', film=film)
    else:
        if request.user.is_superuser:
            film = Film()
            flag = True
            d = {'form': FilmForm(instance=film)}
        else:
            flag = False
            d = {}
        d = d | {'flag': flag}
        return render(request, 'coolapp/new.html', d)
