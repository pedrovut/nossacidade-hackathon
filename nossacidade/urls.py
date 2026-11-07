from django.urls import path
from nossacidade.views import (
    InicioView,

    ReclamacaoView,
    ReclamacaoDetailView,
    ReclamacaoCreateView,
    ReclamacaoUpdateView,
    ReclamacaoDeleteView,
)

app_name = "nossacidade"

urlpatterns = [
    path('', InicioView.as_view(), name="inicio"),

    path("relatos/", ReclamacaoView.as_view(), name="reclamacao_list"),
    path("relatos/<int:pk>/", ReclamacaoDetailView.as_view(),name="reclamacao_detail"),

    path("relatos/novo/", ReclamacaoCreateView.as_view(), name="reclamacao_create"),
    path("relatos/<int:pk>/editar/", ReclamacaoUpdateView.as_view(), name="reclamacao_update"),
    path("relatos/<int:pk>/deletar/", ReclamacaoDeleteView.as_view(), name="reclamacao_delete"),

]