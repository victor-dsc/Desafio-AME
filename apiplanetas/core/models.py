from django.db import models


class Planeta(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    clima = models.CharField(max_length=20)
    terreno = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
