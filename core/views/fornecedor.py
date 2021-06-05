from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from core.models import Fornecedor

from core.forms import FornecedoForm


class FornecedorLista(ListView):

    template_name = 'fornecedor/fornecedor_list.html'
    context_object_name = 'fornecedores'

    def get_context_data(self, **kwargs):
        context = super(FornecedorLista, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addfornecedor')
        return context

    def get_queryset(self):
        queryset = Fornecedor.objects.all()
        return queryset


class FornecedorAdd(CreateView):

    template_name = 'fornecedor/fornecedor_add.html'
    success_url = reverse_lazy('core:listfornecedores')
    model = Fornecedor

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