from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView,
    TemplateView, UpdateView, DeleteView
)
from nossacidade.models import Reclamacao, Categoria
from nossacidade.forms import ReclamacaoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class InicioView(TemplateView):
    template_name = "nossacidade/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.request.GET.get('categoria')
        reclamacoes = Reclamacao.objects.all().order_by('-data_relato')
        
        if categoria_id:
            reclamacoes = reclamacoes.filter(categoria_id=categoria_id)
            context['categoria_ativa'] = int(categoria_id)
        else:
            context['categoria_ativa'] = None

        context['reclamacoes'] = reclamacoes
        context['categorias'] = Categoria.objects.all()
        
        pontos = []
        for r in reclamacoes:
            if r.latitude and r.longitude:
                pontos.append({
                    'id': r.id,
                    'titulo': r.titulo,
                    'lat': r.latitude,
                    'lng': r.longitude,
                    'prioridade': r.score_prioridade,
                    'url': reverse_lazy('nossacidade:reclamacao_detail', kwargs={'pk': r.id})
                })
        context['pontos'] = pontos
        
        # ESSA É A LINHA QUE FALTAVA: Injeta o formulário vazio na Home
        context['form'] = ReclamacaoForm() 
        
        return context

class PerfilView(TemplateView):
    template_name = "nossacidade/perfil.html"

# List e Detail views

class ReclamacaoView(ListView):
    model = Reclamacao
    template_name = "nossacidade/reclamacao_list.html"
    context_object_name = "reclamacao"
    paginate_by = 10

class ReclamacaoDetailView(DetailView):
    model = Reclamacao
    template_name = "nossacidade/reclamacao_detail.html"
    context_object_name = "reclamacao"

# Create views

class ReclamacaoCreateView(LoginRequiredMixin, CreateView):
    model = Reclamacao
    form_class = ReclamacaoForm
    template_name = "nossacidade/reclamacao_create.html"
    success_url = reverse_lazy("nossacidade:reclamacao_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Update views

class ReclamacaoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reclamacao
    form_class = ReclamacaoForm
    template_name = "nossacidade/reclamacao_update.html"
    context_object_name = "reclamacao"
    success_url = reverse_lazy("nossacidade:reclamacao_list")

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user or self.request.user.is_superuser

# Delete views

class ReclamacaoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reclamacao
    template_name = "nossacidade/reclamacao_delete.html"
    context_object_name = "reclamacao"
    success_url = reverse_lazy("nossacidade:reclamacao_list")

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user or self.request.user.is_superuser