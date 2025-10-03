# FilmesApp/midleware.py

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Adicionamos as URLs de redefinição de senha à lista de exceções
        self.exempt_urls = {
            str(reverse_lazy('FilmesApp:login')),
            str(reverse_lazy('FilmesApp:registro')),
            str(reverse_lazy('FilmesApp:logout')),
            # --- ADICIONADO ---
            str(reverse_lazy('FilmesApp:password_reset')),
            str(reverse_lazy('FilmesApp:password_reset_done')),
            str(reverse_lazy('FilmesApp:password_reset_complete')),
            # A URL de confirmação é mais complexa, então usaremos um prefixo
        }

        self.exempt_prefix = (
            '/static/',
            '/admin/',
            # --- ADICIONADO ---
            # Permite qualquer URL que comece com /reset/ (ex: /reset/<uidb64>/<token>/)
            '/reset/',
        )

    def __call__(self, request):
        path = request.path

        # Se o usuário já está logado, permite o acesso a qualquer página
        if request.user.is_authenticated:
            return self.get_response(request)
        
        # Se não está logado, verifica se a página está na lista de exceções
        if path in self.exempt_urls or any(path.startswith(p) for p in self.exempt_prefix):
            return self.get_response(request)
        
        # Se não estiver logado e a página não for uma exceção, redireciona para o login
        return redirect(f"{reverse_lazy(settings.LOGIN_URL)}?next={path}")