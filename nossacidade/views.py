from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView,
    TemplateView, UpdateView, DeleteView
)
from nossacidade.models import Reclamacao
from nossacidade.forms import ReclamacaoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class InicioView(TemplateView):
    template_name = "nossacidade/inicio.html"

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