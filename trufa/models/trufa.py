from uploader.models import Image
from django.db import models


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
    sem_lactose = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao