from django import forms
from nossacidade.models import Categoria, Reclamacao

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            "nome", "gravidade", "urgencia",
        ]

class ReclamacaoForm(forms.ModelForm):
    class Meta:
        model = Reclamacao
        fields = [
            "categoria",
            "descricao", "imagem",
            "endereco", "latitude",
            "longitude",
        ]

