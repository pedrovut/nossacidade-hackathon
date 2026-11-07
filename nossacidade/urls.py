from django.urls import path
from nossacidade.views import CategoriaView, ReclamacaoView, ReclamacaoDetailView

app_name = "nossacidade"

urlpatterns = [
    path("relatos/", ReclamacaoView.as_view(), name="reclamacao_list"),
    path("relatos/<int:pk>/", ReclamacaoDetailView.as_view(), name="reclamacao_detail")
]