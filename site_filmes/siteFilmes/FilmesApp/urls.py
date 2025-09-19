# FilmesApp/urls.py

from django.urls import path
from FilmesApp import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'FilmesApp'

# o atualiza contato tem que ter o pk do contato

urlpatterns = [
    path('', views.home, name='home-filmes'),
    path('base/', views.homeSec, name='base-filmes'), #rota para a pagina de seguranca
    path("lista/", views.FilmeView.as_view(), name='lista-filmes'),
   # CORRETO: Chamando a CLASSE que criamos e usando .as_view()
    path('filme/novo/', views.CriarFilmeView.as_view(), name='criar_filme'),

    # Rota para a página secreta
    path('secreta/', views.pagina_secreta, name='pagina_secreta'),

    # Rota para a página de Login
    path('login/', auth_views.LoginView.as_view(template_name='seguranca/login.html'), name='login'),
    
    # Rota para a ação de Logout
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('pagina_secreta')), name='logout'),

    # Rota para a página de Registro de novo usuário
    path('registro/', views.registro, name='registro'),
]