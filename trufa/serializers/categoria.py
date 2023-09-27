from django.db import models
from django.db.models import CharField

class CategoriaSerializer(models.Model):
    descricao = CharField(max_length=100)