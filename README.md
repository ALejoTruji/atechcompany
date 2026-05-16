# ATech – Guía de instalación paso a paso
## ─────────────────────────────────────────

## ESTRUCTURA DE CARPETAS
```
atech_project/
├── manage.py
├── requirements.txt
├── db.sqlite3               ← se crea al migrar
│
├── atech_project/           ← carpeta de configuración
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── atech/                   ← app principal
    ├── __init__.py
    ├── apps.py
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    │
    ├── templates/
    │   └── atech/
    │       └── home.html
    │
    └── static/
        └── atech/
            ├── css/
            │   └── style.css
            ├── js/
            │   └── main.js
            └── images/
                └── logo.png   ← COLOCA TU LOGO AQUÍ
```

## ─────────────────────────────────────────
## PASO 1 – Crear el entorno virtual
## ─────────────────────────────────────────
```bash
# En la carpeta raíz del proyecto (donde está manage.py)
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Mac / Linux)
source venv/bin/activate
```

## PASO 2 – Instalar dependencias
```bash
pip install -r requirements.txt
```

## PASO 3 – Colocar el logo
Copia tu logo con el nombre exacto:
  atech/static/atech/images/logo.png

Recomendaciones:
  - Formato: PNG con fondo transparente
  - Tamaño ideal: 200x200 px o cuadrado
  - El logo.png aparece en: navbar, hero flotante y footer

## PASO 4 – Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

## PASO 5 – Crear superusuario (admin Django)
```bash
python manage.py createsuperuser
# Ingresa: usuario, email, contraseña
```

## PASO 6 – Ejecutar servidor
```bash
python manage.py runserver
```
Abre: http://127.0.0.1:8000

Panel de admin: http://127.0.0.1:8000/admin

## ─────────────────────────────────────────
## CONFIGURAR EMAIL REAL (Gmail SMTP)
## ─────────────────────────────────────────

1. Ve a tu cuenta Google: https://myaccount.google.com
2. Seguridad → Verificación en dos pasos → actívala
3. Seguridad → Contraseñas de aplicaciones
4. Genera una contraseña para "Correo" / "Otro"
5. En settings.py, REEMPLAZA el backend console por:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'atechtrujillo@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'   # contraseña de aplicación (16 chars)
DEFAULT_FROM_EMAIL = 'ATech <atechtrujillo@gmail.com>'
CONTACT_EMAIL = 'atechtrujillo@gmail.com'
```

## ─────────────────────────────────────────
## CONFIGURAR WHATSAPP
## ─────────────────────────────────────────
En settings.py, reemplaza:
  WHATSAPP_LINK = 'https://chat.whatsapp.com/TU_ENLACE_AQUI'

Para obtener el enlace de tu grupo:
  WhatsApp → Grupo → Configuración → Invitar al grupo → Copiar enlace

## ─────────────────────────────────────────
## COLECTAR ESTÁTICOS (producción)
## ─────────────────────────────────────────
```bash
python manage.py collectstatic
```

## ─────────────────────────────────────────
## VERIFICAR EL ENVÍO DE EMAIL (consola)
## ─────────────────────────────────────────
Con EMAIL_BACKEND = console, el email aparece en la terminal al enviar el formulario.
Busca "Content-Type: text/plain" en la salida de runserver.

## ─────────────────────────────────────────
## MENSAJES GUARDADOS EN ADMIN
## ─────────────────────────────────────────
Todos los mensajes de contacto se guardan en la BD y se pueden ver en:
  http://127.0.0.1:8000/admin  → "Mensajes de contacto"
