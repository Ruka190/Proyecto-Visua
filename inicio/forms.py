from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
