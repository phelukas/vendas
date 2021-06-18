from django.db import models

class Fornecedor(models.Model):

    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Fornecedo"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.cnpj


class Categoria(models.Model):

    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produtos(models.Model):

    categoria = models.ForeignKey(
        Categoria, related_name="produtos", on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(
        Fornecedor, related_name="fornecedores", on_delete=models.CASCADE, max_length=225)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    disponivel = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
