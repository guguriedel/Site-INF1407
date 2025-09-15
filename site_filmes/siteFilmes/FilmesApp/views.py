# FilmesApp/views.py

from django.shortcuts import render, redirect
from .models import Filme
from .forms import FilmeModel2Form # Você nomeou sua classe de formulário como FilmeModel2Form
from django.views.generic.base import View

# View para LISTAR os filmes (mantém como Class-Based View)
class FilmeView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        contexto = {'filmes': filmes}
        return render(request, 'FilmesApp/listaFilmes.html', contexto)

# View para a PÁGINA INICIAL
def home(request):
    return render(request, 'FilmesApp/home.html')

# View para CRIAR um novo filme (como uma função separada)
def criar_filme(request):
    # Se o formulário foi enviado (método POST)
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = FilmeModel2Form(request.POST)
        # Verifica se os dados são válidos
        if form.is_valid():
            form.save() # Salva o novo filme no banco de dados
            return redirect('FilmesApp:lista-filmes') # Redireciona para a lista
    # Se a página foi apenas acessada (método GET)
    else:
        # Cria um formulário em branco
        form = FilmeModel2Form()

    # Renderiza o template com o formulário (seja ele novo ou com erros de validação)
    return render(request, 'FilmesApp/criaFilme.html', {'form': form})