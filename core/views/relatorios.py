from django.db.models.aggregates import Sum
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
        queryset = Sum('quantidade', distinct=True)
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

class ProdutosFaltaEstoque(ListView):

    template_name = "base/relatorio_prod_falt.html"
    context_object_name = 'produtos'    

    def get_queryset(self):
        queryset = Produtos.objects.filter(quantidade=0)
        return queryset

class FornecedoresFaltaEstoque(ListView):

    template_name = "base/relatorio_forne_falt.html"
    context_object_name = 'produtos'    

    def get_queryset(self):
        queryset = Produtos.objects.filter(quantidade=0)
        print(queryset)

        return queryset


class Exportar_csv_prod_falta(View):

    def get(self, request, *args, **kwargs):

        queryset = Produtos.objects.filter(quantidade=0)         

        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': f'attachment; filename="Produtos em Falta.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(
            ['Produto', 'Quantidade']
        )
        for produto in queryset:    
            writer.writerow(
                [produto,0]
            )
        return response

class Exportar_csv_forne_falta(View):

    def get(self, request, *args, **kwargs):

        queryset = Produtos.objects.filter(quantidade=0)

        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': f'attachment; filename="Fornecedor Produtos Falta.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(
            ['Fornecedor', 'Produto']
        )

        for produto in queryset:
            writer.writerow(
                [produto.fornecedor,produto]
            )
        return response
