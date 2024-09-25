let currentTestimonio = 1;

function rotateTestimonios() {
    const totalTestimonios = 2;  // Tienes 2 grupos de testimonios (testimonio-1 y testimonio-2)
    document.getElementById(`testimonio-${currentTestimonio}`).style.opacity = 0;  // Ocultar el actual
    currentTestimonio = currentTestimonio === totalTestimonios ? 1 : currentTestimonio + 1;
    document.getElementById(`testimonio-${currentTestimonio}`).style.opacity = 1;  // Mostrar el siguiente
}

document.addEventListener("DOMContentLoaded", function() {
    setInterval(rotateTestimonios, 60000);  // Cambiar cada 60 segundos (1 minuto)
});
