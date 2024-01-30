from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=80)
    foto = models.FileField(upload_to='produtos')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome