# FilmesApp/views.py

from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Filme
from .forms import FilmeModel2Form # Você nomeou sua classe de formulário como FilmeModel2Form
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# View para LISTAR os filmes (mantém como Class-Based View)
class FilmeView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        contexto = {'filmes': filmes}
        return render(request, 'FilmesApp/listaFilmes.html', contexto)

# View para a PÁGINA INICIAL
def home(request):
    return render(request, 'FilmesApp/home.html')

def homeSec(request):
    #renderiza a pagina de seguranca
    return render(request, 'seguranca/base.html')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request, 'seguranca/registro.html', context)

# View para CRIAR um novo filme (CORRIGIDO)
# Trocamos 'def' por 'class' e ajustamos o nome
class CriarFilmeView(View):
    def get(self, request, *args, **kwargs):
        formulario = FilmeModel2Form()
        # Renomeei a chave do contexto para 'form' para ser mais claro
        contexto = {'form': formulario}
        return render(request, 'FilmesApp/criaFilme.html', contexto)

    def post(self, request, *args, **kwargs):
        formulario = FilmeModel2Form(request.POST)
        if formulario.is_valid():
            formulario.save()
            # A linha filme.save() não é necessária, form.save() já salva.
            return HttpResponseRedirect(reverse_lazy('FilmesApp:lista-filmes'))
        else:
            # Se o formulário for inválido, precisamos renderizar a página novamente com os erros
            contexto = {'form': formulario}
            return render(request, 'FilmesApp/criaFilme.html', contexto)

