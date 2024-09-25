from django.shortcuts import render, redirect
from .forms import RegistroAlumnoForm, RegistroPsicologoForm, LoginForm, Alumno, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .backends import PersonalizedLoginBackend, PersonalizedLoginBackend2






def index(request):
    return render(request, 'main/index.html')

# Registro de alumnos

def registrarse_alumno(request):
    try:
        request.session['usuario']
        if request.session.get('tipo', None) == "alumno":
            return redirect('perfil_alumno')
        else:
            return redirect('psicologo_dashboard')
    except KeyError:
        if request.method == 'POST':
            form = RegistroAlumnoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registro de alumno exitoso. Ahora puedes iniciar sesión.')
                return redirect('login_alumno')
        else:
            form = RegistroAlumnoForm()
    return render(request, 'main/registro_alumno.html', {'form': form})  # Asegúrate de que 'registro_alumno.html' exista

# Registro de psicólogos
def registrarse_psicologo(request):
    try:
        request.session['usuario']
        if request.session.get('tipo', None) == "alumno":
            return redirect('perfil_alumno')
        else:
            return redirect('psicologo_dashboard')
    except KeyError:
        if request.method == 'POST':
            form = RegistroPsicologoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registro de psicólogo exitoso. Ahora puedes iniciar sesión.')
                return redirect('login_psicologo')
        else:
            form = RegistroPsicologoForm()
    return render(request, 'main/registro_psicologo.html', {'form': form})  # Asegúrate de que 'registro_alumno.html' exista


    # Login para alumnos
def login_alumno(request):
    try:
        request.session['usuario']
        if request.session.get('tipo', None) == "alumno":
            return redirect('perfil_alumno')
        else:
            return redirect('psicologo_dashboard')
    except KeyError:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = PersonalizedLoginBackend.authenticate(request, username=username, password=password)
                    #user.backend = 'django.contrib.auth.backends.ModelBackend'
                    if user is not None:
                        PersonalizedLoginBackend.get_user (request, user)
                        messages.success(request, 'Inicio de sesión exitoso')
                        request.session['usuario'] = user.usuario
                        request.session['nombre'] = user.nombre
                        request.session['email'] = user.correo
                        request.session['edad'] = user.edad
                        request.session['tipo'] = "alumno"
                        return redirect('perfil_alumno')
                    else:
                        messages.error(request, 'Credenciales inválidas. Intenta de nuevo.')
        else:
            messages.error(request, 'Error aca nuevo.')
            form = LoginForm()
    return render(request, 'main/login_alumno.html', {'form': form})  # Asegúrate de que 'login_alumno.html' exista

# Login para psicólogos
def login_psicologo(request):
    try:
        request.session['usuario']
        if request.session.get('tipo', None) == "alumno":
            return redirect('perfil_alumno')
        else:
            return redirect('psicologo_dashboard')
    except KeyError:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = PersonalizedLoginBackend2.authenticate(request, username=username, password=password)
                    #user.backend = 'django.contrib.auth.backends.ModelBackend'
                    if user is not None:
                        PersonalizedLoginBackend2.get_user(request, user)
                        messages.success(request, 'Inicio de sesión exitoso')
                        request.session['usuario'] = user.usuario
                        request.session['nombre'] = user.nombre
                        request.session['email'] = user.correo
                        request.session['edad'] = user.edad
                        request.session['tipo'] = "psicologo"
                        return redirect('psicologo_dashboard')
                    else:
                        messages.error(request, 'Credenciales inválidas. Intenta de nuevo.')
        else:
            messages.error(request, 'Error aca nuevo.')
            form = LoginForm()
    return render(request, 'main/login_psicologo.html', {'form': form})  # Asegúrate de que 'login_alumno.html' exista


# Dashboard para psicólogos (requiere autenticación)

def psicologo_dashboard(request):
    try:
        request.session['usuario']
        if request.session.get('tipo', None) == "psicologo":
            alumno={}
            alumno['username']=request.session['usuario'] 
            alumno['nombre']=request.session['nombre'] 
            alumno['email']=request.session['email'] 
            alumno['edad']=request.session['edad'] 
            return render(request, 'main/psicologo_dashboard.html')
        else:
            return redirect('perfil_alumno')
    except KeyError:
        return redirect('login_psicologo')
    return render(request, 'main/psicologo_dashboard.html')  # Asegúrate de que 'psicologo_dashboard.html' exista

# Página de "Nosotros"
def nosotros(request):
    return render(request, 'main/nosotros.html')  # Asegúrate de que 'nosotros.html' exista

# Vista para restablecer contraseña
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)
            if users.exists():
                # Enviar email para restablecer contraseña
               
                messages.success(request, 'Se ha enviado un enlace a tu correo para restablecer la contraseña.')
                return redirect('index')  # Cambia a la vista que prefieras tras el éxito
            else:
                messages.error(request, 'No se encontró ningún usuario con ese correo.')
            send_mail(
                    "Reestablecer contraseña",
                    "Reestablezca su contraseña en el siguiente link.",
                    ["sofi.diaz17@gmail.com"],
                    fail_silently=False,
                )
    else:
        form = PasswordResetForm()
    return render(request, 'main/password_reset.html', {'form': form})  # Asegúrate de que 'password_reset.html' exista

def password_new(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
    else:
        form = ChangePasswordForm()
    return render(request, 'main/password_reset_confirm.html', {'form': form})  # Asegúrate de que 'password_reset.html' exista


# Vista para listar todos los alumnos
def lista_alumnos(request):
    alumnos = Alumno.objects.all()  # Obtenemos todos los alumnos
    return render(request, 'main/alumnos_list.html')


def citasPsico(request):
    return render(request, 'main/calendario_psico.html')

def calendarioPsico(request):
    return render(request, 'main/calendar_appointment-booking.html')

# Vista para mostrar el perfil de un alumno
def perfil_alumno(request):
    #alumno = get_object_or_404(Alumno, id=alumno_id) 
    #alumno="NICOLAS" # Obtenemos el alumno o un error 404 si no existe
    try:
        request.session['usuario']
        if request.session.get('tipo', None) == "alumno":
            alumno={}
            alumno['username']=request.session['usuario'] 
            alumno['nombre']=request.session['nombre'] 
            alumno['email']=request.session['email'] 
            alumno['edad']=request.session['edad'] 
            return render(request, 'main/alumno_perfil.html', {'alumno': alumno})
        else:
            return redirect('psicologo_dashboard')
    except KeyError:
        return redirect('login_alumno')
    return redirect('login_alumno')



def cerrarsesion(request):
    del request.session['usuario'] 
    del request.session['nombre'] 
    del request.session['email'] 
    del request.session['edad'] 
    del request.session['tipo']
    return redirect('index') 
