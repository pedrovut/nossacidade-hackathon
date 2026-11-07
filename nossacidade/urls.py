from django.urls import path
from nossacidade.views import CategoriaView, ReclamacaoView

app_name = "nossacidade"

urlpatterns = [
    path("relatos/", ReclamacaoView.as_view(), name="reclamacao_list")
    
]