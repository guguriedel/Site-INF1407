# FilmesApp/views.py

from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Filme
from .forms import FilmeModel2Form
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.db.models import Avg, Q, F




# View para LISTAR os filmes (mantém como Class-Based View)
class FilmeView(View):

    login_url = 'FilmesApp:login'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.filter(registrado_por=request.user)

        filmes = filmes.annotate(
            nota_media = Avg(
                'nome',
                filter=Q(nome=F('nome'), data_publicacao=F('data_publicacao'))
            )
        )

        nome_filme = request.GET.get('nome', None)
        genero = request.GET.get('genero', None)
        nota_str = request.GET.get('nota', None)

        #Por padrão ordena por dt de publish
        orderby = request.GET.get('orderby', '-data_publicacao')

        if nome_filme:
            filmes = filmes.filter(nome__icontains=nome_filme)

        if genero:
            filmes = filmes.filter(genero__icontains=genero)

        if nota_str:
            try:
                nota = float(nota_str)
                # Filtra por filmes com nota maior ou igual à fornecida
                filmes = filmes.filter(nota__gte=nota)
            except (ValueError, TypeError):
                # Ignora o filtro se a nota não for um número válido
                pass

        # Lista de campos permitidos para ordenação
        allowed_orderby_fields = ['nome', '-nome', 'nota', '-nota', 'duracao_em_horas', '-duracao_em_horas']
        if orderby in allowed_orderby_fields:
            filmes = filmes.order_by(orderby)
    

        contexto = {
            'filmes': filmes,
            'valores_filtro': request.GET # Passa os valores de filtro de volta para o template
        }
        return render(request, 'FilmesApp/listaFilmes.html', contexto)

class FilmeUpdateView(View):
    """
    Classe para atualizar os dados de um filme existente.
    """
    def get(self, request, pk, *args, **kwargs):
        """
        Exibe o formulário preenchido com os dados do filme a ser atualizado.
        """
        filme = get_object_or_404(Filme, pk=pk, regitrado_por=request.user ) # 1. Busca o Filme pelo ID (pk)
        form = FilmeModel2Form(instance=filme) # 2. Cria o formulário com os dados do filme
        
        contexto = {
            'form': form,
        }
        # 3. Renderiza o mesmo template usado para criar, mas agora com dados
        return render(request, 'FilmesApp/filme_form.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        """
        Salva as alterações enviadas pelo formulário.
        """
        filme = Filme.objects.get(pk=pk) # Busca o filme que está sendo editado
        form = FilmeModel2Form(request.POST, instance=filme) # Passa os dados novos E a instância original

        if form.is_valid():
            form.save() # Salva as alterações
            return HttpResponseRedirect(reverse_lazy('FilmesApp:lista-filmes'))
        else:
            # Se o formulário for inválido, exibe a página novamente com os erros
            contexto = {'form': form}
            return render(request, 'FilmesApp/filme_form.html', contexto)
        
# --- Classe para DELETAR um Filme ---
class FilmeDeleteView(View):
    """
    Classe para apagar um filme.
    """
    def get(self, request, pk, *args, **kwargs):
        """
        Exibe a página de confirmação de exclusão.
        """
        filme = Filme.objects.get(pk=pk) # 1. Busca o Filme pelo ID
        contexto = {'filme': filme}
        # 2. Renderiza a página de confirmação
        return render(request, 'FilmesApp/filme_confirm_delete.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        """
        Apaga o filme do banco de dados.
        """
        filme = Filme.objects.get(pk=pk) # 1. Busca o Filme
        filme.delete() # 2. Deleta o registro
        # 3. Redireciona para a lista de filmes
        return HttpResponseRedirect(reverse_lazy('FilmesApp:lista-filmes'))


# View para a PÁGINA INICIAL
def home(request):
    return render(request, 'FilmesApp/home.html')

@login_required(login_url='FilmesApp:login') # 2. APLIQUE O DECORADOR
def pagina_secreta(request):
    """Renderiza a página secreta que só pode ser acessada por usuários logados."""
    return render(request, 'seguranca/paginaSecreta.html')

def homeSec(request):
    #renderiza a pagina de seguranca
    return render(request, 'seguranca/base.html')

def registro(request):

    #Auto-Redirect
    if request.user.is_authenticated:
        return redirect('FilmesApp:lista-filmes')

    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        next_url = request.POST.get('next') or 'FilmesApp:lista-filmes'

        if formulario.is_valid():
            user = formulario.save()
            login(request, user)
            return redirect(next_url)
    else:
        formulario = UserCreationForm()
        next_url = request.GET.get('next', '')

    context = {'form': formulario, 
               'next': next_url}
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
            filme = formulario.save(commit=False)
            filme.registrado_por = request.user
            filme.save()

            return HttpResponseRedirect(reverse_lazy('FilmesApp:lista-filmes'))
        else:
            # Se o formulário for inválido, precisamos renderizar a página novamente com os erros
            contexto = {'form': formulario}
            return render(request, 'FilmesApp/criaFilme.html', contexto)

