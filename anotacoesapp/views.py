from django.shortcuts import render

def index(request):
    return render(request, 'anotacoes/index.html')

def minhasanotacoes(request):
    return render(request, 'anotacoes/minhasanotacoes.html')