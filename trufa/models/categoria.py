from uploader.models import Image
from django.db import models

class Trufa(models.Model):
    descricao = models.CharField(max_length=100)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


    def __str__(self):
        return self.descricao