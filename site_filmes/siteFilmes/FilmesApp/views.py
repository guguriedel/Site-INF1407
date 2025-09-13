from django.http import HttpResponse

def home(request):
    return HttpResponse('Teste página principal filmes')