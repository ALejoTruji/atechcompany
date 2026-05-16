from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    """Vista principal con todas las secciones."""
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # 1. Guardar en base de datos
            ContactMessage.objects.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje,
            )

            # 2. Enviar email
            cuerpo_email = f"""
Nuevo mensaje de contacto desde el sitio web de ATech
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nombre:  {nombre}
Email:   {email}
Asunto:  {asunto}

Mensaje:
{mensaje}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Enviado desde atech.com
"""
            try:
                send_mail(
                    subject=f'[ATech Web] {asunto}',
                    message=cuerpo_email,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    '¡Mensaje enviado con éxito! Nos pondremos en contacto contigo pronto.'
                )
            except Exception as e:
                messages.warning(
                    request,
                    'Tu mensaje fue guardado, pero hubo un problema al enviar el email. '
                    'Te contactaremos pronto.'
                )

            return redirect('home')

    context = {
        'form': form,
        'whatsapp_link': getattr(settings, 'WHATSAPP_LINK', '#'),
    }
    return render(request, 'atech/home.html', context)
