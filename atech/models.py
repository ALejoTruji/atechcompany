from django.db import models


class ContactMessage(models.Model):
    """
    Guarda una copia de los mensajes de contacto en la base de datos.
    Opcional pero útil para no perder mensajes si el email falla.
    """
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")
    leido = models.BooleanField(default=False, verbose_name="Leído")

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre} - {self.asunto} ({self.fecha.strftime('%d/%m/%Y')})"
