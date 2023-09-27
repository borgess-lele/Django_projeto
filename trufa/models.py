from django.db import models

class Trufa(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
