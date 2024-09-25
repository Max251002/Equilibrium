from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password



class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    usuario = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)
    contraseña1 = models.CharField(max_length=100)
    contraseña2 = models.CharField(max_length=100)

    @property
    def is_authenticated(self):
        return True

    def clean(self):
        if self.contraseña1 != self.contraseña2:
            raise ValidationError("Las contraseñas no coinciden")

    def save(self, *args, **kwargs):
        self.contraseña1 = make_password(self.contraseña1)
        self.contraseña2 = make_password(self.contraseña2)
        super(Alumno, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario

    def getAlData(self):
        alumno = Alumno.objects.get(usuario="test_alumno")
        self.assertEqual(alumno.nombre, "Test Alumno")



class Psicologo(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    especialidad = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)
    contraseña1 = models.CharField(max_length=100)                                                                                                          
    contraseña2 = models.CharField(max_length=100)
    def __str__(self):
        
        return f'{self.user.username} - {self.especialidad}'

    def clean(self):
        if self.contraseña1 != self.contraseña2:
            raise ValidationError("Las contraseñas no coinciden")

    def save(self, *args, **kwargs):
        self.contraseña1 = make_password(self.contraseña1)
        self.contraseña2 = make_password(self.contraseña2)
        super(Psicologo, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario
