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
    labels = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    datasets = [{
            "data": [120, 180, 90, 220, 150],
            "borderColor": "#B94448",
            "backgroundColor": "#B944482E",
            "tension": 0.2,
            "fill": True,
        }]

    matches_totales = 20012
    return render(request, "admin/inicio.html", {
        "clientes_registrados": 20, ##
        "matches_totales": f"{matches_totales:,}".replace(",", "."), ##
        "reportes_usuarios": 33, ##s
        "notificacion_pendiente": 67, ##
        "labels_json": json.dumps(labels, ensure_ascii=False),
        "datasets_json": json.dumps(datasets, ensure_ascii=False),
    })

def admin_dinero(request):

    periodos_matchs = {
        "semana": {
            "labels": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
            "data": [18, 26, 20, 34, 29, 41, 23],
            "detalle": "Matches por día de la semana",
            "eje_x": "Día",
        },
        "mes": {
            "labels": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
            "data": [120, 180, 145, 220],
            "detalle": "Matches por semana del mes",
            "eje_x": "Semana",
        },
        "anio": {
            "labels": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
            "data": [120, 180, 90, 220, 150, 175, 205, 190, 230, 215, 245, 260],
            "detalle": "Matches por mes del año",
            "eje_x": "Mes",
        },
    }

    
    edades_labels = ["18-19", "20-29", "30-39", "40-49", "50-59", "60+"]
    hombres_por_edad = {"18-19": 38, "20-29": 55, "30-39": 64, "40-49": 52, "60+": 22}
    mujeres_por_edad = {"18-19": 42, "20-29": 61, "30-39": 70, "40-49": 58, "60+": 35}
    datasets2 = [
        {
            "label": "Hombres",
            "data": [-hombres_por_edad.get(rango, 0) for rango in edades_labels],
            "backgroundColor": "#652E38",
        },
        {
            "label": "Mujeres",
            "data": [mujeres_por_edad.get(rango, 0) for rango in edades_labels],
            "backgroundColor": "#E86E67",
        },
    ]

    top_gustos = {"Música": 60, "Viajes": 55, "Cine": 49, "Deporte": 32, "Libros": 2}
    gustos_ordenados = sorted(top_gustos.items(), key=lambda gusto: gusto[1], reverse=True)[:5]

    context = {
        "periodos_matchs_json": json.dumps(periodos_matchs, ensure_ascii=False),
        "edades_labels_json": json.dumps(edades_labels, ensure_ascii=False),
        "datasets2_json": json.dumps(datasets2, ensure_ascii=False),
        "gustos_labels_json": json.dumps([gusto for gusto, _ in gustos_ordenados], ensure_ascii=False),
        "gustos_valores_json": json.dumps([total for _, total in gustos_ordenados]),
        "kpi_matchs": 60.3, ###Clientes con al menos un match/ total * 100
        "kpi_estancados": 3.25, ### Clientes sin match / total* 100 
    }

    return render(request, "admin/dinero.html", context)

def admin_notificaciones(request):
    notificaciones = [
        {
            "id_notificacion": 1,
            "tema": "Reporte",
            "fecha": "Enero",
            "id_usuario": 2,
            "mensaje": "Usuario reportado por feo",
            "estado": 1
        },
        {
            "id_notificacion": 2,
            "tema": "Mensaje",
            "fecha": "Febrero",
            "id_usuario": 3,
            "mensaje": "Nuevo correo en bandeja",
            "estado": 1
        },
        {
            "id_notificacion": 3,
            "tema": "Reporte",
            "fecha": "Marzo",
            "id_usuario": 1,
            "mensaje": "Usuario menor de edad",
            "estado": 2
        }
    ]

    return render(
        request,
        "admin/notificacion.html",
        {"notificaciones": notificaciones}
    )


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
