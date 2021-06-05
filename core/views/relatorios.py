from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
import csv
from django.db.models import Count
from django.http import HttpResponse, response
from core.models import Produtos, Categoria, Fornecedor, Item, Ordem


# Função para verificar parametro para filtro
def is_valid_queryparam(param):
    return param != '' and param is not None

# Classe responsável por listar todas as vendas
class ListaProdutosView(ListView):

    template_name = "base/relatorio.html"
    context_object_name = 'produtos'

    def get_queryset(self):
        queryset = Produtos.objects.select_related('categoria').annotate(Count('quantidade')).distinct   
        print(queryset)
        return queryset

    def quantidade_categoria(self):

        all_categorias = Categoria.objects.all()
        nome_categorias = list(all_categorias.values('nome'))

        lista = dict()
        lista2 = list()

        all_produtos = Produtos.objects.select_related('categoria').values('categoria','nome','quantidade')

        x = all_produtos




        for i in x:
            categoria = i.get('categoria')
            quantidade = i.get('quantidade')
            


        for i in nome_categorias:
            nome = i.get('nome')
            quan = Produtos.objects.filter(categoria__nome=nome).count()
            
            lista[nome] = quan

        return lista

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        vendas_finalizadas = request.GET.get('vendas_finalizadas')
        vendas_aguardando = request.GET.get('vendas_aguardando')
        clientes = request.GET.get('clientes')

        # Filtar todas vendas finalizadas
        if is_valid_queryparam(vendas_finalizadas):
            self.object_list = self.object_list.filter(venda_status=True)

        # Filtar todas vendas não finalizadas
        if is_valid_queryparam(vendas_aguardando):
            self.object_list = self.object_list.filter(venda_status=False)

        # Filtar vendas de um específico
        if is_valid_queryparam(clientes) and clientes != 'Todos':
            self.object_list = self.object_list.filter(
                cliente_cliente__email=clientes)

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(ListaProdutosView, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addvenda')
        context['quantidade_categoria'] = self.quantidade_categoria()
        return context


# class Exportar_csv(View):

#     def get(self, request, *args, **kwargs):


#         self.object = self.get_object()
#         paciente = self.object
#         endereco = paciente.endereco_paciente
#         dados_sociodemograficos = paciente.socio_paciente
#         dados_clinicos = paciente.clinico_paciente
#         diagnostico_medio = paciente.diagmedico_paciente
#         comorbidade = paciente.comorbidades_paciente
#         diagnostico_obesidade = paciente.diagobesidade_paciente
#         diagnostico_sedentario = paciente.diagsedentario_paciente
#         response = HttpResponse(
#             content_type='text/csv',
#             headers={
#                 'Content-Disposition': f'attachment; filename="Paciente {paciente.first_name}.csv"'},
#         )
#         writer = csv.writer(response)
#         writer.writerow(
#             ['Nome', 'E-mail', 'CPF', 'Telefone',
#              'Endereço', 'Numero', 'Bairro', 'Complemento', 'Cidade - Estado', 'CEP',
#              'Estado civil', 'Cor/Raça', 'Ocupação', 'Religião', 'Anos de estudo', 'Sexo', 'Renda familiar', 'Com quantas pessoas vivem',
#              ]
#         )

#         writer.writerow(
#             [paciente.first_name + paciente.last_name, paciente.email, paciente.cpf, paciente.telefone,

#              endereco.endereco, endereco.numero, endereco.bairro, endereco.complemento, endereco.cidade +
#              '-' + endereco.estado, endereco.cep,

#              dados_sociodemograficos.estado_civil, dados_sociodemograficos.corraca, dados_sociodemograficos.ocupacao, dados_sociodemograficos.religiao,
#              dados_sociodemograficos.anos_estudo, dados_sociodemograficos.sexo, dados_sociodemograficos.renda_familiar, dados_sociodemograficos.pessoas_vivem]
#         )

#         return response



from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)