from django.db.models.aggregates import Count
from django.db.models.expressions import Subquery
from django.db.models.query_utils import Q
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Sum

from core.models import Fornecedor, Produtos

from core.forms import FornecedoForm


class FornecedorLista(ListView):

    template_name = 'fornecedor/fornecedor_list.html'
    context_object_name = 'fornecedores'

    def get_context_data(self, **kwargs):
        context = super(FornecedorLista, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addfornecedor')
        return context

    def get_queryset(self):
        # total = Produtos.objects.aggregate(total=Sum('quantidade'))
        # queryset = Produtos.objects.annotate(total=Sum('quantidade'))
        # u = Produtos.objects.annotate(total=Sum('produto__quantidade')).filter(id=1)
        queryset = Produtos.objects.select_related('fornecedor').distinct('fornecedor')
        queryset2 = Produtos.objects.annotate(total=Subquery())

        return queryset

class FornecedorAdd(CreateView):

    model = Fornecedor
    template_name = 'fornecedor/fornecedor_add.html'
    success_url = reverse_lazy('core:listfornecedores')
    success_message = "Fornecedor( <b>%(descricao)s</b>) adicionado com sucesso ."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())     

    def get(self, request, *args, **kwargs):
        self.object = None

        fornecedorform = FornecedoForm(prefix='fornecedorform')

        return self.render_to_response(self.get_context_data(form=fornecedorform))

    def post(self, request, *args, **kwargs):
        self.object = None

        fornecedorform = FornecedoForm(
            request.POST, request.FILES, prefix='fornecedorform', request=request)

        if fornecedorform.is_valid():
            self.object = fornecedorform.save(commit=False)
            self.object.save()
            return self.form_valid(fornecedorform)

        return self.form_invalid(form=fornecedorform)


class FornecedorEdit(UpdateView):

    template_name = 'fornecedor/fornecedor_edit.html'
    success_url = reverse_lazy('core:listfornecedores')
    success_message = "Fornecedor( <b>%(descricao)s</b>) editado com sucesso ."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())     

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = Fornecedor.objects.get(id=pk)
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        fornecedorform = FornecedoForm(
            instance=self.object, prefix='fornecedorform')

        return self.render_to_response(self.get_context_data(form=fornecedorform))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        fornecedorform = FornecedoForm(
            request.POST, request.FILES, instance=self.object, prefix='fornecedorform', request=request)

        if fornecedorform.is_valid():
            self.object = fornecedorform.save(commit=False)
            self.object.save()

            return self.form_valid(fornecedorform)
        return self.form_invalid(form=fornecedorform)

class FornecedorDelete(DeleteView):

    model = Fornecedor
    template_name = 'fornecedor/pacientes_confirm_delete.html'
    success_url = reverse_lazy('core:listfornecedores')
    success_message = "Fornecedor deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FornecedorDelete, self).delete(request, *args, **kwargs)        