# FilmesApp/urls.py

from django.urls import path
from FilmesApp import views

app_name = 'FilmesApp'

urlpatterns = [
    path('', views.home, name='home-filmes'),
    path("lista/", views.FilmeView.as_view(), name='lista-filmes'),
    
    # ADICIONE ESTA LINHA
    path('filme/novo/', views.criar_filme, name='criar_filme'),
]