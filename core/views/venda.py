from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from core.models import Produtos

from core.forms import ProdutoForm


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
