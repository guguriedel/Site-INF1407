#from django.http import HttpResponse
from django.shortcuts import render
from FilmesApp.models import Filme
from django.views.generic.base import View

class FilmeView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        contexto = {'filmes': filmes,}
        return render(request, 'FilmesApp/listaFilmes.html', contexto)
    
def home(request):
    return render(request, 'FilmesApp/home.html')


def listafilmes(request):
    return render(request, 'FilmesApp/listaFilmes.html')