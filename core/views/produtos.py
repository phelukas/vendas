from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from core.models import Produtos

from core.forms import ProdutoForm


class Index(TemplateView):
    template_name = 'base/index.html'


class PodutosLista(ListView):

    template_name = 'produtos/produtos_list.html'
    context_object_name = 'produtos'

    def get_context_data(self, **kwargs):
        context = super(PodutosLista, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addproduto')
        return context

    def get_queryset(self):
        queryset = Produtos.objects.all()
        return queryset


class ProdutosAdicionar(CreateView):

    template_name = 'produtos/produtos_add.html'
    success_url = reverse_lazy('core:listprodutos')
    model = Produtos

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
            self.object =  produtoform.save(commit=False)
            self.object.save()

            return self.form_valid(produtoform)
        return self.form_invalid(form=produtoform)

class ProdutoDelete(DeleteView):

    model = Produtos
    template_name = 'produtos/produtos_confirm_delete.html'
    success_url = reverse_lazy('core:listprodutos')        