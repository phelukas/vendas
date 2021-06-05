from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.urls import reverse_lazy, reverse

from core.models import Ordem, Item

from core.forms import OrdemForm


class VendasLista(ListView):

    template_name = 'vendas/vendas_list.html'
    context_object_name = 'vendas'

    def get_context_data(self, **kwargs):
        context = super(VendasLista, self).get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('core:addvenda')
        return context

    def get_queryset(self):
        queryset = Ordem.objects.all()
        return queryset


class VendasAdicionar(CreateView):

    template_name = 'vendas/vendas_add.html'
    success_url = reverse_lazy('core:listvendas')
    model = Ordem

    # def get_success_url(self):
    #     success_url = reverse('core:checkout', kwargs={
    #         'pk': self.object.pk,
    #     })
    #     return success_url

    def get(self, request, *args, **kwargs):
        self.object = None

        vendaform = OrdemForm(prefix='vendaform')

        return self.render_to_response(self.get_context_data(form=vendaform))

    def post(self, request, *args, **kwargs):
        self.object = None

        vendaform = OrdemForm(
            request.POST, request.FILES, prefix='vendaform', request=request)

        if vendaform.is_valid():
            self.object = vendaform.save(commit=False)
            self.object.save()
            return self.form_valid(vendaform)

        return self.form_invalid(form=vendaform)
