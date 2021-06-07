from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from core.models import Categoria

from core.forms import CategoriaForm


class CategoriaList(ListView):

    template_name = 'categoria/categoria_list.html'
    context_object_name = 'categorias'

    def get_context_data(self, **kwargs):
        context = super(CategoriaList, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addcategoria')
        return context

    def get_queryset(self):
        queryset = Categoria.objects.all()
        return queryset


class CategoriaAdd(CreateView):

    template_name = 'categoria/categoria_add.html'
    model = Categoria
    success_url = reverse_lazy('core:listcategorias')
    success_message = "Categoria( <b>%(descricao)s</b>) adicionado com sucesso ."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())       

    def get(self, request, *args, **kwargs):
        self.object = None

        categoriaform = CategoriaForm(prefix='categoriaform')

        return self.render_to_response(self.get_context_data(form=categoriaform))

    def post(self, request, *args, **kwargs):
        self.object = None

        categoriaform = CategoriaForm(
            request.POST, request.FILES, prefix='categoriaform', request=request)

        if categoriaform.is_valid():
            self.object = categoriaform.save(commit=False)
            self.object.save()
            return self.form_valid(categoriaform)

        return self.form_invalid(form=categoriaform)


class CategoriaEdit(UpdateView):

    template_name = 'categoria/categoria_edit.html'
    success_url = reverse_lazy('core:listcategorias')
    success_message = "Categoria( <b>%(descricao)s</b>) adicionado com sucesso ."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())       

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = Categoria.objects.get(id=pk)
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        categoriaform = CategoriaForm(
            instance=self.object, prefix='categoriaform')

        return self.render_to_response(self.get_context_data(form=categoriaform))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        categoriaform = CategoriaForm(
            request.POST, request.FILES, instance=self.object, prefix='categoriaform', request=request)

        if categoriaform.is_valid():
            self.object = categoriaform.save(commit=False)
            self.object.save()

            return self.form_valid(categoriaform)
        return self.form_invalid(form=categoriaform)

class CategoriaDelete(DeleteView):

    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('core:listcategorias')
    success_message = "Categoria deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoriaDelete, self).delete(request, *args, **kwargs)      