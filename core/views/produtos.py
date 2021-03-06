from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.shortcuts import redirect

from core.models import Produtos, Fornecedor, Categoria

from core.forms import ProdutoForm


def is_valid_queryparam(param):
    return param != '' and param != 'Todos' and param is not None


class Index(TemplateView):
    template_name = 'base/index.html'


class PodutosLista(ListView):

    template_name = 'produtos/produtos_list.html'
    context_object_name = 'produtos'

    def get_context_data(self, **kwargs):
        context = super(PodutosLista, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addproduto')
        context['todos_fornecedores'] = Fornecedor.objects.all()
        context['todas_categorias'] = Categoria.objects.all()
        context['todos_produtos'] = Produtos.objects.distinct('nome')
        return context

    def get_queryset(self):
        queryset = Produtos.objects.all()

        return queryset
            

    def post(self, request, *args, **kwargs):
        self.object_list = Produtos.objects

        forncedores = self.request.POST.get("forncedores")
        categorias = self.request.POST.get("categorias")
        produtos = self.request.POST.get("produtos")

        if is_valid_queryparam(produtos):
            self.object_list = self.object_list.filter(
                nome=produtos
            )
        else:
            self.object_list = self.object_list.all()

        if is_valid_queryparam(categorias):
            self.object_list = self.object_list.filter(
                categoria__nome=categorias
            )
        else:
            self.object_list = self.object_list.all()

        if is_valid_queryparam(forncedores):
            self.object_list = self.object_list.filter(
                fornecedor__cnpj=forncedores
            )
        else:
            self.object_list = self.object_list.all()

        return self.render_to_response(self.get_context_data())



class ProdutosAdicionar(CreateView):

    model = Produtos
    template_name = 'produtos/produtos_add.html'
    success_url = reverse_lazy('core:listprodutos')
    success_message = "Produto( <b>%(descricao)s</b>) adicionado com sucesso ."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ProdutosAdicionar, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addproduto')
        return context

    def get(self, request, *args, **kwargs):
        self.object = None

        produtoform = ProdutoForm(prefix='produtoform')

        return self.render_to_response(self.get_context_data(form=produtoform))

    def post(self, request, *args, **kwargs):
        self.object = None

        produtoform = ProdutoForm(
            request.POST, request.FILES, prefix='produtoform', request=request)

        if produtoform.is_valid():
            self.object = produtoform.save(commit=False)
            self.object.save()
            return self.form_valid(produtoform)

        return self.form_invalid(form=produtoform)


class ProdutoEdit(UpdateView):

    template_name = 'produtos/produtos_edit.html'
    success_url = reverse_lazy('core:listprodutos')
    success_message = "Produto( <b>%(descricao)s</b>) editado com sucesso ."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = Produtos.objects.get(id=pk)
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        produtoform = ProdutoForm(
            instance=self.object, prefix='produtoform')

        return self.render_to_response(self.get_context_data(form=produtoform))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        produtoform = ProdutoForm(
            request.POST, request.FILES, instance=self.object, prefix='produtoform', request=request)

        if produtoform.is_valid():
            self.object = produtoform.save(commit=False)
            self.object.save()

            return self.form_valid(produtoform)
        return self.form_invalid(form=produtoform)


class ProdutoDelete(DeleteView):

    model = Produtos
    template_name = 'produtos/produtos_confirm_delete.html'
    success_url = reverse_lazy('core:listprodutos')
    success_message = "Produto deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProdutoDelete, self).delete(request, *args, **kwargs)

