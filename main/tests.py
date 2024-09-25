from django.test import TestCase
from .models import Alumno, Psicologo

class AlumnoTestCase(TestCase):
    def setUp(self):
        Alumno.objects.create(nombre="Test Alumno", edad=20, usuario="test_alumno", correo="test@correo.com", contraseña1="1234", contraseña2="1234")

    def test_alumno_creation(self):
        alumno = Alumno.objects.get(usuario="test_alumno")
        self.assertEqual(alumno.nombre, "Test Alumno")

class PsicologoTestCase(TestCase):
    def setUp(self):
        Psicologo.objects.create(nombre="Test Psicologo", edad=30, especialidad="Test Especialidad", usuario="test_psicologo", contraseña1="1234", contraseña2="1234")

    def test_psicologo_creation(self):
        psicologo = Psicologo.objects.get(usuario="test_psicologo")
        self.assertEqual(psicologo.nombre, "Test Psicologo")
