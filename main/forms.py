from django import forms
from django.contrib.auth.models import User
from .models import Alumno, Psicologo
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

class RegistroAlumnoForm(forms.ModelForm):
    contraseña1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    contraseña2 = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña')

    class Meta:
        model = Alumno
        fields = ['nombre', 'edad', 'usuario', 'correo', 'contraseña1', 'contraseña2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("contraseña1")
        password2 = cleaned_data.get("contraseña2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control',
                   'placeholder': 'Old Password'}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm password'}),
    )

from django import forms
from django.contrib.auth.models import User
from .models import Psicologo

class RegistroPsicologoForm(forms.ModelForm):
    contraseña1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    contraseña2 = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña')

    class Meta:
        model = Psicologo
        fields = ['nombre', 'edad', 'especialidad', 'usuario', 'correo', 'contraseña1', 'contraseña2']

   

    def clean(self):
        cleaned_data = super().clean()
        contraseña1 = cleaned_data.get("contraseña1")
        contraseña2 = cleaned_data.get("contraseña2")

        if contraseña1 and contraseña2 and contraseña1 != contraseña2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data




class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

