# FilmesApp/urls.py

from django.urls import path
from FilmesApp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name = 'FilmesApp'

# o atualiza contato tem que ter o pk do contato

urlpatterns = [
    path('', views.home, name='home-filmes'),
    path('base/', views.homeSec, name='base-filmes'), #rota para a pagina de seguranca
    path("lista/", views.FilmeView.as_view(), name='lista-filmes'),
   # CORRETO: Chamando a CLASSE que criamos e usando .as_view()
    path('filme/novo/', views.CriarFilmeView.as_view(), name='criar_filme'), 

    path('filme/<int:pk>/editar/', views.FilmeUpdateView.as_view(), name='editar_filme'),
    
    # URL para a página de DELEÇÃO de um filme específico
    path('filme/<int:pk>/deletar/', views.FilmeDeleteView.as_view(), name='deletar_filme'),

    path('registro/', views.registro, name='registro'),

    # Rota para a página secreta
    path('paginaSecreta/', views.pagina_secreta, name='pagina_secreta'),

    # Rota para a página de Login
    path('login/', auth_views.LoginView.as_view(template_name='seguranca/login.html'), name='login'),
    
    # Rota para a ação de Logout
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('FilmesApp:pagina_secreta')), name='logout'),

   path('mudar-senha/',
         auth_views.PasswordChangeView.as_view(
             template_name='FilmesApp/seguranca/password_change_form.html',
             success_url='/mudar-senha/concluido/'
         ),
         name='password_change'),
    path('mudar-senha/concluido/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='FilmesApp/seguranca/password_change_done.html'
         ),
         name='password_change_done'),

    # ROTAS PARA RESETAR A SENHA (USUÁRIO ESQUECEU)
       path('password-reset/',
         auth_views.PasswordResetView.as_view(
             # Este caminho deve corresponder à sua estrutura de pastas
             template_name='FilmesApp/seguranca/password_reset_form.html', 
             success_url=reverse_lazy('FilmesApp:password_reset_done')
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='FilmesApp/seguranca/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='FilmesApp/seguranca/password_reset_confirm.html',
             success_url=reverse_lazy('FilmesApp:password_reset_complete') # Adicione esta linha para o redirect
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='FilmesApp/seguranca/password_reset_complete.html'
         ),
         name='password_reset_complete'),

            path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='seguranca/password_change_form.html',
        success_url=reverse_lazy('FilmesApp:password_change_done')
    ), name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='seguranca/password_change_done.html'
    ), name='password_change_done'),

    # ... (suas urls existentes: home, lista, criar, editar, deletar, login, logout, registro, etc.)

    # --- ROTAS PARA REDEFINIÇÃO DE SENHA ---
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='seguranca/password_reset_form.html',
        email_template_name='seguranca/password_reset_email.html',
        subject_template_name='seguranca/password_reset_subject.txt',
        success_url=reverse_lazy('FilmesApp:password_reset_done'),
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='seguranca/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='seguranca/password_reset_confirm.html',
        success_url=reverse_lazy('FilmesApp:password_reset_complete')
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='seguranca/password_reset_complete.html'
    ), name='password_reset_complete'),
]