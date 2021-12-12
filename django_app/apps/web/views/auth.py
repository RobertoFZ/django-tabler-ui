from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django_app.apps.web.forms.auth.login_form import LoginForm


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        form = LoginForm(initial={'remember_me': True})
        logout(request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            email = data.get('email')
            password = data.get('password')
            remember_me = data.get('remember_me')

            if not remember_me:
                request.session.set_expiry(0)

            user = authenticate(
                request,
                username=email,
                password=password
            )
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('redirect_to', None)
                return redirect(redirect_url) if not redirect_url == None else redirect('web:routes:list')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Correo o contraseña incorrectos')
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


class LogoutView(View):
    redirect_url = 'web:auth:login'

    def get(self, request):
        logout(request)
        return redirect(self.redirect_url)
