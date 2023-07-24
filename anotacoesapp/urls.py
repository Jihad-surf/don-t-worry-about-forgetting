from django.urls import path
from anotacoesapp.views import index, minhasanotacoes

urlpatterns = [
    path('',index, name='index'),
    path('minhasanotacoes',minhasanotacoes, name='minhasanotacoes')
]
