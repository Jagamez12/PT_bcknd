from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_email
from django.conf import settings
from .models import Empleado, Email

@receiver(post_save, sender=Email)
def enviar_correo_bienvenida(sender, instance, created, **kwargs):
    if created:
        # Recuperar información del empleado asociado al userId
        empleado = Empleado.objects.get(id=instance.usuario)

        # Enviar correo de bienvenida utilizando la información del empleado
        subject = '¡Bienvenido a la empresa!'
        message = f'Estimado/a {empleado.nombres} {empleado.apellidos},\n\nBienvenido/a a nuestra empresa. Esperamos que te sientas cómodo/a y encuentres satisfacción en tu nuevo puesto de trabajo.\n\nDetalles del empleado:\nID: {empleado.id}\nNombre: {empleado.nombres} {empleado.apellidos}\nTipo de Identificación: {empleado.tipoIdentificacion}\nIdentificación: {empleado.identificacion}\nFecha de Ingreso: {empleado.fechaIngreso}\nSalario Mensual: {empleado.salarioMensual}\nCargo: {empleado.cargo}\nDepartamento: {empleado.departamento}\n\nAtentamente,\nEl equipo de la empresa'
        html = f'<p>{message}</p>'
        send_email(instance.email, subject, html)