from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    # login/
    url(r'^$', views.UserFormView.as_view(), name='loginview'),
    # logout
    url(r'^logout/$', views.UserLogoutView.as_view(), name='logoutview'),
    # login/perfil/
    url(r'^perfil/$', views.MeuPerfilView.as_view(), name='perfilview'),
    # login/editarperfil/
    url(r'^editarperfil/$', views.EditarPerfilView.as_view(), name='editarperfilview'),
    # login/criarperfil/
    url(r'^criarperfil/$', views.CriarPefilView.as_view(), name='criarperfilview'),

]