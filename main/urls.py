from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    
    # Rutas para registro de alumno y psicólogo
    path('alumno/registro/', views.registrarse_alumno, name='registrarse_alumno'),  # Ruta para registrar alumno
    path('psicologo/registro/', views.registrarse_psicologo, name='registrarse_psicologo'),  # Ruta para registrar psicólogo
    
    # Rutas para login de alumno y psicólogo
    path('alumno/login/', views.login_alumno, name='login_alumno'),  # Ruta para login alumno
    path('psicologo/login/', views.login_psicologo, name='login_psicologo'),
    
    # Ruta para la página de "Nosotros"
    path('nosotros/', views.nosotros, name='nosotros'),

    # Rutas para restablecimiento de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('reset/', views.password_new, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    
    path('psicologo/dashboard/', views.psicologo_dashboard, name='psicologo_dashboard'),
    path('psicologo/calendario/', views.calendarioPsico, name='calendarioPsico'),
    path('psicologo/citas/', views.citasPsico, name='citasPsico'),
    path('psicologo/alumnos/', views.lista_alumnos, name='lista_alumnos'),


    #path('alumnos/', views.lista_alumnos, name='lista_alumnos'),  # Página para ver la lista de alumnos
    path('alumno/perfil/', views.perfil_alumno, name='perfil_alumno'),  # URL para perfil de alumno
    path('CerrarSesion', views.cerrarsesion, name='cerrarsesion'),  # URL para perfil de alumno
   
]

