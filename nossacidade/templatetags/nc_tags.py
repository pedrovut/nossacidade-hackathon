from django import template
from nossacidade.prioridade import nivel_prioridade

register = template.Library()

@register.filter
def nivel(reclamacao):
    return nivel_prioridade(reclamacao.score_prioridade)

@register.filter
def nome_autor(user):
    if not user:
        return "Autor removido"
    return user.get_full_name() or user.username

@register.filter
def iniciais(user):
    return nome_autor(user)[:1].upper()
