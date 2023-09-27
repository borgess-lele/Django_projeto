from django.db import models
from django.db.models import CharField


class Categoria(models.Model):
    descricao = CharField(max_length=100)