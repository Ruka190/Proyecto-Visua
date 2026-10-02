from django.shortcuts import render

# Creamos una función que devuelve el HTML que acabas de guardar
def index(request):
    return render(request, 'inicio/index.html')

def usuario(request):
    return render(request, 'inicio/usuario.html')