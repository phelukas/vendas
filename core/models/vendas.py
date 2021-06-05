from django.db import models
from django.urls import reverse

from core.models import Produtos, Categoria


class Ordem(models.Model):
    nome = models.CharField("Nome Completo", max_length=250)
    email = models.EmailField()
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido {self.id}"

    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        return total

    def get_descricao(self):
        return ", ".join(
            [f"{item.quantidade}x {item.produto.nome}" for item in self.items.all()]
        )                


class Item(models.Model):
    ordem = models.ForeignKey(Ordem, related_name="items", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, related_name="ordem_items", on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_total_preco(self):
        return self.preco * self.quantidade 