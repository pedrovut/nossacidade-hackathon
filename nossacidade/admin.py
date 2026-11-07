from django.contrib import admin

from nossacidade.models import Categoria, Reclamacao

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "gravidade", "urgencia")
    search_fields = ("nome")

class ReclamacaoAdmin(admin.ModelAdmin):
    list_display = (
        "autor", "categoria",
        "descricao", "imagem",
        "endereco", "latitude",
        "longitude", "data_relato",
        "upvotes", "status",
    )

    search_fields = ("autor__username", "categoria__nome", "descricao")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Reclamacao, ReclamacaoAdmin)
