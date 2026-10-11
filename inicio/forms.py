from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil, Preferencia

# Campos con clases Bootstrap + tokens Beyond Date (bd-body form-control).
_INPUT_CLS = 'form-control bd-body'


class RegistroForm(UserCreationForm):
    """Crear cuenta: nombre, correo, contraseña x2 (Miro Registro)."""
    username = forms.CharField(
        label='NOMBRE DE USUARIO',
        max_length=150,
        widget=forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ingresar nombre'}),
    )
    email = forms.EmailField(
        label='CORREO ELECTRÓNICO',
        widget=forms.EmailInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ingresar correo'}),
    )
    password1 = forms.CharField(
        label='CONTRASEÑA',
        widget=forms.PasswordInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ingresar contraseña'}),
    )
    password2 = forms.CharField(
        label='CONFIRMAR CONTRASEÑA',
        widget=forms.PasswordInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Confirmar contraseña'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {'username': ''}


class LoginForm(forms.Form):
    """Iniciar sesión: usuario o correo + contraseña (Miro Login)."""
    username = forms.CharField(
        label='NOMBRE DE USUARIO O CORREO',
        widget=forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Nombre de usuario o correo'}),
    )
    password = forms.CharField(
        label='CONTRASEÑA',
        widget=forms.PasswordInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Contraseña'}),
    )


class PerfilForm(forms.ModelForm):
    """Bloque 4 · Info crear usuario."""
    class Meta:
        model = Perfil
        fields = ['display_name', 'ciudad', 'edad', 'biografia', 'valores', 'hobbies', 'gustos']
        labels = {
            'display_name': 'NOMBRE VISIBLE',
            'ciudad': 'CIUDAD',
            'edad': 'EDAD',
            'biografia': 'BIOGRAFÍA PERSONAL',
            'valores': 'VALORES',
            'hobbies': 'HOBBIES',
            'gustos': 'GUSTOS',
        }
        widgets = {
            'display_name': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ej. Javier'}),
            'ciudad': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ej. Santiago, Chile'}),
            'edad': forms.NumberInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ej. 25', 'min': 18, 'max': 99}),
            'biografia': forms.Textarea(attrs={'class': _INPUT_CLS, 'rows': 3, 'placeholder': 'Cuéntanos sobre ti...'}),
            'valores': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'honestidad, empatía...'}),
            'hobbies': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'lectura, trekking...'}),
            'gustos': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'música indie, café...'}),
        }


class PreferenciaForm(forms.ModelForm):
    """Bloque 4 · Preferencias de búsqueda."""
    class Meta:
        model = Preferencia
        fields = ['edad_min', 'edad_max', 'distancia_km', 'intereses', 'busco']
        labels = {
            'edad_min': 'EDAD MÍNIMA',
            'edad_max': 'EDAD MÁXIMA',
            'distancia_km': 'DISTANCIA (KM)',
            'intereses': 'INTERESES',
            'busco': 'QUÉ CONEXIÓN BUSCAS',
        }
        widgets = {
            'edad_min': forms.NumberInput(attrs={'class': _INPUT_CLS, 'min': 18, 'max': 99}),
            'edad_max': forms.NumberInput(attrs={'class': _INPUT_CLS, 'min': 18, 'max': 99}),
            'distancia_km': forms.NumberInput(attrs={'class': _INPUT_CLS, 'min': 1, 'max': 500}),
            'intereses': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'arte, música indie...'}),
            'busco': forms.TextInput(attrs={'class': _INPUT_CLS, 'placeholder': 'Ej. amistad, relación seria...'}),
        }

    def clean(self):
        cleaned = super().clean()
        mini, maxi = cleaned.get('edad_min'), cleaned.get('edad_max')
        if mini and maxi and mini > maxi:
            raise forms.ValidationError('La edad mínima no puede ser mayor que la máxima.')
        return cleaned
