# Faixas da legenda (Crítica/Alta/Média/Baixa) sobre Reclamacao.score_prioridade.
# Ajuste os limites conforme a realidade dos seus dados.
def nivel_prioridade(score):
    if score >= 20:
        return "critica"
    if score >= 12:
        return "alta"
    if score >= 6:
        return "media"
    return "baixa"
