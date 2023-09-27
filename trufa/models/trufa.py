from uploader.models import Image
from django.db import models

from .categoria import Categoria

class Trufa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    categoria = models.ForeignKey(Categoria, related_name="trufas", on_delete=models.PROTECT, null=True, default=None)

    def __str__(self):
        return self.descricao