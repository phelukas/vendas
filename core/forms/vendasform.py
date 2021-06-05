from django import forms
from django.utils.translation import ugettext_lazy as _

from core.models import Ordem, Item


class OrdemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OrdemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Ordem
        fields = "__all__"
        # widgets = {
        #     'categoria': forms.TextInput(attrs={'class': 'form-control'}),
        #     'nome': forms.TextInput(attrs={'class': 'form-control'}),
        #     'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        #     'preco': forms.TextInput(attrs={'class': 'form-control'}),
        #     'fornecedor': forms.TextInput(attrs={'class': 'form-control'}),
        #     'disponivel': forms.CheckboxInput(),
        # }

        # labels = {
        #     'categoria': _('Categoria'),
        #     'nome': _('Nome'),
        #     'descricao': _('Descrição'),
        #     'preco': _('Preço'),
        #     'fornecedor': _('Fornecedor'),
        #     'disponivel': _('Disponivel')
        # }


# class FornecedoForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super(FornecedoForm, self).__init__(*args, **kwargs)

#     class Meta:
#         model = Fornecedor
#         fields = "__all__"
#         # widgets = {
#         #     'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'nome': forms.TextInput(attrs={'class': 'form-control'})
#         # }

#         labels = {
#             'cnpj': _('cnpj'),
#             'nome': _('Nome')
#         }

# class CategoriaForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super(CategoriaForm, self).__init__(*args, **kwargs)

#     class Meta:
#         model = Categoria
#         fields = "__all__"
#         # widgets = {
#         #     'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'nome': forms.TextInput(attrs={'class': 'form-control'})
#         # }

#         # labels = {
#         #     'cnpj': _('cnpj'),
#         #     'nome': _('Nome')
#         # }
