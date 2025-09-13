from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Filme(models.Model):
    nome = models.CharField(max_length=200, help_text="Nome do filme")
    nota = models.DecimalField(
        max_digits=2, 
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        help_text="Nota de 1 a 5"
    )
    # É melhor armazenar a duração em uma unidade padrão, como segundos (inteiro).
    # A conversão para horas pode ser feita na exibição.
    duracao_em_segundos = models.IntegerField(help_text="Duração em segundos")
    genero = models.CharField(max_length=100, help_text="Gênero do filme")
    data_publicacao = models.DateField(help_text="Data de Publicação")

    # O ID int comum é criado automaticamente pelo Django como chave primária (pk).

    class Meta:
        ordering = ['-data_publicacao', 'nome'] # Ordena os filmes por data (mais recente primeiro) e depois por nome

    def __str__(self):
        return self.nome