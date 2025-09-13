#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'FilmesApp/home.html')


def segundaPagina(request):
    return render(request, 'FilmesApp/segundaPagina.html')