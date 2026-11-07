from django.db import models
import math
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Nome da Categoria", max_length=50)
    gravidade = models.IntegerField(verbose_name="Gravidade (1 a 5)", default=1)
    urgencia = models.IntegerField(verbose_name="Urgência (1 a 5)", default=1)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['id']

class Reclamacao(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('ANALISE', 'Em análise'),
        ('ANDAMENTO', 'Equipe no local'),
        ('RESOLVIDO', 'Resolvido'),
    ]

    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria")

    descricao = models.TextField(verbose_name="Descrição", blank=False)
    imagem = models.ImageField(verbose_name="Foto do Problema", upload_to='relatos/', blank=True, null=True)

    endereco = models.CharField(verbose_name="Endereço Aproximado", max_length=200, blank=False)
    latitude = models.FloatField(verbose_name="Latitude", null=True, blank=True)
    longitude = models.FloatField(verbose_name="Longitude", null=True, blank=True)

    data_relato = models.DateTimeField(verbose_name="Data do Relato", auto_now_add=True)
    upvotes = models.IntegerField(verbose_name="Votos", default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTO')

    def __str__(self):
        return f"{self.categoria.nome} em {self.endereco}"

    @property
    def score_prioridade(self):
        """
        Calcula a prioridade dinamicamente baseada em:
        GUT + Log(Votos) + Tempo de espera.
        """
        if not self.categoria:
            return 0
            
        base = self.categoria.gravidade * self.categoria.urgencia
        fator_votos = 1 + math.log10(self.upvotes + 1)
        dias_aberto = (timezone.now() - self.data_criacao).days
        fator_tempo = dias_aberto * 0.5
        
        prioridade = (base * fator_votos) + fator_tempo
        return round(prioridade, 2)