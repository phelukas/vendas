from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import View, TemplateView
from django.views.generic.edit import UpdateView, CreateView

from django.contrib import messages

from django.db import DatabaseError
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from users.forms import UserLoginForm, PerfilUsuarioForm, UserCreationForm
from users.models import User

class UserFormView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class(None)

        if request.user.is_authenticated:
            return redirect('core:index')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if request.POST and form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = form.authenticate_user(username=username, password=password)
            if user:
                if not request.POST.get('remember_me', None):
                    request.session.set_expiry(0)
                login(request, user)
                return redirect('core:index')

        return render(request, self.template_name, {'form': form})


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login:loginview")

class MeuPerfilView(TemplateView):
    model = User
    template_name = 'account/perfil.html'

class EditarPerfilView(UpdateView):
    
    form_class = PerfilUsuarioForm
    template_name = 'account/editar_perfil.html'
    success_url = reverse_lazy('login:perfilview')
    success_message = "Perfil editado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message

    def get_object(self, queryset=None):
        obj = User.objects.get_or_create(pk=self.request.user.id)[0]
        return obj

    def get_success_url(self, *args, **kwargs):
        return self.success_url

    def get(self, request, *args, **kwargs):
        super(EditarPerfilView, self).get(request, *args, **kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(form=form, object=self.object))

    def post(self, request):
        self.object = self.get_object()

        try:
            instance = User.objects.get(pk=self.request.user.pk)
            form = self.form_class(
                request.POST, request.FILES, instance=instance)
        except User.DoesNotExist:
            form = self.form_class(request.POST, request.FILES, instance=None)

        user = User.objects.get(pk=self.request.user.id)

        if form.is_valid():
            try:
                perfil = form.save(commit=False)
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.username = request.POST.get("email")
                user.email = request.POST.get("email")

                user.save()
                perfil.user = user
                return self.form_valid(form)

            except (DatabaseError, ValidationError) as e:
                form.add_error(field=None, error=e)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.success_url)


class CriarPefilView(CreateView):   

    form_class = UserCreationForm
    template_name = 'account/criar_perfil.html'
    success_url = reverse_lazy('login:loginview')
    success_message = "Perfil criado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=str(self.object))

    def form_valid(self, form):
        messages.success(
            self.request, self.get_success_message(form.cleaned_data))
        return redirect(self.get_success_url())            


    def get(self, request, *args, **kwargs):
        return super(CriarPefilView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()            
            return self.form_valid(form)
            
        return self.form_invalid(form=form)
