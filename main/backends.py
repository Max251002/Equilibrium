
from django.contrib.auth.backends import ModelBackend
from .models import Alumno, Psicologo
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



class PersonalizedLoginBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwars):
       
        try:
            user = Alumno.objects.get(usuario=username)
        except Alumno.DoesNotExist:
            return None
        if check_password(password, user.contraseña1):
            return user
        else:
            return None

    def get_user(self, user_id):
        #This shall return the user given the id
        from django.contrib.auth.models import AnonymousUser
        try:
            user = Alumno.objects.get(id=user_id)
        except Exception as e:
            user = AnonymousUser()
        return user

class PersonalizedLoginBackend2(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwars):
       
        try:
            user = Psicologo.objects.get(usuario=username)
        except Psicologo.DoesNotExist:
            return None
        if check_password(password, user.contraseña1):
            return user
        else:
            return None

    def get_user(self, user_id):
        #This shall return the user given the id
        from django.contrib.auth.models import AnonymousUser
        try:
            user = Psicologo.objects.get(id=user_id)
        except Exception as e:
            user = AnonymousUser()
        return user

class findUserEmail(ModelBackend):
       def get_user(self, email):
        #This shall return the user given the id
        from django.contrib.auth.models import AnonymousUser
        try:
            user = Alumno.objects.get(correo=email)
        except Exception as e:
            user = AnonymousUser()
        return user
