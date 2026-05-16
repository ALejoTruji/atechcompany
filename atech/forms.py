from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=150,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre completo',
            'id': 'id_nombre',
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tucorreo@ejemplo.com',
            'id': 'id_email',
        })
    )
    asunto = forms.CharField(
        max_length=200,
        label="Asunto",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '¿En qué podemos ayudarte?',
            'id': 'id_asunto',
        })
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Cuéntanos sobre tu proyecto...',
            'rows': 5,
            'id': 'id_mensaje',
        })
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 2:
            raise forms.ValidationError("Por favor ingresa un nombre válido.")
        return nombre

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje', '').strip()
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return mensaje
