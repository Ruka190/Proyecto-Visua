from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/', views.usuario, name='usuario'),
    path('contacto/', views.contacto, name='contacto'),
    path('faq/', views.faq, name='faq'),
    path('nuestra-mision/', views.mision, name='mision'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('info/', views.info_view, name='info'),
    path('preferencias/', views.preferencias_view, name='preferencias'),
    path('administrador/', views.administrador, name= 'administrador'),
    path('administrador/inicio/', views.admin_inicio, name='admin_inicio'),
    path('administrador/dinero/', views.admin_dinero, name='admin_dinero'),
    path('administrador/notificaciones/', views.admin_notificaciones, name='admin_notificaciones'),
]
