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
]
