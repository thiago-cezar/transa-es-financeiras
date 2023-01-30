from django.db import models


class tradesModel(models.Model):
    class Meta:
        ordering = ["id"]

    Dono_da_loja = models.CharField(max_length=14)
    Nome_loja = models.CharField(max_length=19)

    
