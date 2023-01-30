from django.db import models


class cnabModel(models.Model):
    class Meta:
        ordering = ["id"]

    Tipo = models.CharField(max_length=1)
    Data = models.CharField(max_length=10)
    Valor = models.FloatField()
    CPF = models.CharField(max_length=11)
    Cartão = models.CharField(max_length=12)
    Hora = models.CharField(max_length=8)
    
    trades = models.ForeignKey(
        "trades.tradesModel", on_delete=models.CASCADE, related_name="cnab"
    )
