from django.conf.urls import url
from setup.settings import DEBUG
from . import views


app_name = 'core'

urlpatterns = [
    url(r'^home/$', views.Index.as_view(), name='index'),
    url(r'^exportar_csv/$', views.Exportar_csv_prod_falta.as_view(), name='relatorio_csv'),
    url(r'^exportar_csv/fornecedor$', views.Exportar_csv_forne_falta.as_view(), name='relatorio_csv_forne_falta'),

    url(r'^produtos/$', views.PodutosLista.as_view(), name='listprodutos'),
    url(r'^addproduto/$', views.ProdutosAdicionar.as_view(), name='addproduto'),
    url(r'^addproduto/(?P<pk>[0-9]+)/$', views.ProdutoEdit.as_view(), name='editproduto'),
    url(r'^produto/deletar/(?P<pk>[0-9]+)/$', views.ProdutoDelete.as_view(), name='delproduto'),

    url(r'^fornecedores/$', views.FornecedorLista.as_view(), name='listfornecedores'),
    url(r'^addfornecedor/$', views.FornecedorAdd.as_view(), name='addfornecedor'),
    url(r'^editfornecedor/(?P<pk>[0-9]+)/$', views.FornecedorEdit.as_view(), name='editfornecedor'),
    url(r'^fornecedor/deletar/(?P<pk>[0-9]+)/$', views.FornecedorDelete.as_view(), name='delfornecedor'),

    url(r'^categorias/$', views.CategoriaList.as_view(), name='listcategorias'),
    url(r'^addcategoria/$', views.CategoriaAdd.as_view(), name='addcategoria'),
    url(r'^categorias/(?P<pk>[0-9]+)/$', views.CategoriaEdit.as_view(), name='editcategoria'),
    url(r'^categorias/deletar/(?P<pk>[0-9]+)/$', views.CategoriaDelete.as_view(), name='delcategoria'),

    url(r'^relatorio/$', views.ListaProdutosView.as_view(), name='relatorio'),
    url(r'^relatorio/ProdutosEstoqueFalta/$', views.ProdutosFaltaEstoque.as_view(), name='relatorio2'),
    url(r'^relatorio/fornecedorestoquefalta/$', views.FornecedoresFaltaEstoque.as_view(), name='relatorio3'),

    url(r'^vendas/$', views.VendasLista.as_view(), name='listvendas'),
    url(r'^addvenda/$', views.VendasAdicionar.as_view(), name='addvenda'),
]