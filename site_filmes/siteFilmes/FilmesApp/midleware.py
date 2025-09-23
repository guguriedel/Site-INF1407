from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings

class LoginRequiredMiddleware:
    #Redireciona Users para tela de login

    def __init__(self, get_response):
        self.get_response = get_response

        #rotas permitifas 
        self.exempt_urls = {
            str(reverse_lazy('FilmesApp:login')),
            str(reverse_lazy('FilmesApp:registro')),
            str(reverse_lazy('FilmesApp:logout')),
            '/admin/login',
        }

        self.exempt_prefix = (
            '/static/',
            '/admin/',
        )

    def __call__ (self, request):
        path = request.path

        if request.user.is_authenticated:
            return self.get_response(request)
        
        if path in self.exempt_urls or any(path.startswith(p) for p in self.exempt_prefix):
            return self.get_response(request)
        
        return redirect(f"{reverse_lazy(settings.LOGIN_URL)}?next={path}")