from django.shortcuts import render
from django.views.generic import ListView
from nossacidade.models import Categoria, Reclamacao

# Create your views here.

class CategoriaView(ListView):
    model = Categoria
    template_name = "nossacidade/categoria_list.html"
    context_object_name = "categoria"
    paginate_by = 10

class ReclamacaoView(ListView):
    model = Categoria
    template_name = "nossacidade/reclamacao_list.html"
    context_object_name = "reclamacao"
    paginate_by = 10

