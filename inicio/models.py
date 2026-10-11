from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Perfil(models.Model):
    """Bloque 4 · Info crear usuario. Una ficha por User."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil')
    display_name = models.CharField('nombre visible', max_length=80)
    ciudad = models.CharField(max_length=80, blank=True)
    edad = models.PositiveIntegerField(
        null=True, blank=True, validators=[MinValueValidator(18), MaxValueValidator(99)]
    )
    biografia = models.TextField(blank=True)
    valores = models.CharField(max_length=255, blank=True, help_text='Ej: honestidad, empatía, familia')
    hobbies = models.CharField(max_length=255, blank=True, help_text='Ej: lectura, trekking, cine')
    gustos = models.CharField(max_length=255, blank=True, help_text='Ej: música indie, café, arte')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        return f'{self.display_name} (@{self.user.username})'


class Preferencia(models.Model):
    """Bloque 4 · Preferencias de búsqueda. Una por Perfil."""
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='preferencias')
    edad_min = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(99)])
    edad_max = models.PositiveIntegerField(default=99, validators=[MinValueValidator(18), MaxValueValidator(99)])
    distancia_km = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(500)])
    intereses = models.CharField(max_length=255, blank=True, help_text='Ej: arte y diseño, música indie')
    busco = models.CharField('qué conexión buscas', max_length=255, blank=True)

    class Meta:
        verbose_name = 'preferencia'
        verbose_name_plural = 'preferencias'

    def __str__(self):
        return f'Preferencias de {self.perfil}'
