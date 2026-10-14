import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import RegistroForm, LoginForm, PerfilForm, PreferenciaForm
from .models import Perfil, Preferencia

# Creamos una función que devuelve el HTML que acabas de guardar
def index(request):
    return render(request, 'inicio/index.html')

def usuario(request):
    return render(request, 'inicio/usuario.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')

def faq(request):
    return render(request, 'inicio/faq.html')

def mision(request):
    return render(request, 'inicio/mision.html')

def administrador(request):
    return render(request, 'admin/administrador.html')

def admin_inicio(request):
    labels = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
    datasets = [{
        "label": "Ventas ($)",
        "data": [120, 180, 90, 220, 150],
        "tension": 0.2,
        "fill": True,
    }]
    return render(request, "admin/inicio.html", {
        "labels_json": json.dumps(labels, ensure_ascii=False),
        "datasets_json": json.dumps(datasets, ensure_ascii=False),
    })

def admin_dinero(request):

    labels = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
    datasets = [{
            "label": "Ventas ($)",
            "data": [120, 180, 90, 220, 150],
            "tension": 0.2,
            "fill": True,
        }]
    datasets2 = [{
                "label": "Ventas ($)",
                "data": [10, 50, 90, 30, -10],
                "tension": 0.2,
                "fill": True,
            }]
    context = {
        "labels_json": json.dumps(labels, ensure_ascii=False),
        "datasets_json": json.dumps(datasets, ensure_ascii=False),
        "datasets2_json": json.dumps(datasets2, ensure_ascii=False),
    }

    return render(request, "admin/dinero.html", context)

def admin_notificaciones(request):
    return render(request, "admin/notificacion.html")


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
    """Bloque 4: Crear cuenta y pasar a Info."""
    if request.user.is_authenticated:
        return redirect('info')
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('info')
    return render(request, 'inicio/registro.html', {'form': form})


@login_required(login_url='login')
def info_view(request):
    """Bloque 4 · Paso 1/2: Info crear usuario."""
    perfil, _ = Perfil.objects.get_or_create(
        user=request.user, defaults={'display_name': request.user.username}
    )
    form = PerfilForm(request.POST or None, instance=perfil)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('preferencias')
    return render(request, 'inicio/info.html', {'form': form, 'paso': 1})


@login_required(login_url='login')
def preferencias_view(request):
    """Bloque 4 · Paso 2/2: Preferencias."""
    perfil, _ = Perfil.objects.get_or_create(
        user=request.user, defaults={'display_name': request.user.username}
    )
    prefs, _ = Preferencia.objects.get_or_create(perfil=perfil)
    form = PreferenciaForm(request.POST or None, instance=prefs)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('usuario')
    return render(request, 'inicio/preferencias.html', {'form': form, 'paso': 2})
