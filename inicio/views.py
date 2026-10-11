from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm

# Creamos una función que devuelve el HTML que acabas de guardar
def index(request):
    return render(request, 'inicio/index.html')

def usuario(request):
    return render(request, 'inicio/usuario.html')


def login_view(request):
    """Bloque 4: Iniciar sesión con usuario o correo."""
    if request.user.is_authenticated:
        return redirect('usuario')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ident = form.cleaned_data['username'].strip()
        password = form.cleaned_data['password']
        # Permite entrar con correo: resuelve a username.
        if '@' in ident:
            try:
                ident = User.objects.get(email__iexact=ident).username
            except User.DoesNotExist:
                form.add_error(None, 'Credenciales inválidas.')
                return render(request, 'inicio/login.html', {'form': form})
        user = authenticate(request, username=ident, password=password)
        if user is not None:
            login(request, user)
            return redirect('usuario')
        form.add_error(None, 'Credenciales inválidas.')
    return render(request, 'inicio/login.html', {'form': form})


def registro_view(request):
    """Bloque 4: Crear cuenta y auto-login."""
    if request.user.is_authenticated:
        return redirect('usuario')
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('usuario')
    return render(request, 'inicio/registro.html', {'form': form})