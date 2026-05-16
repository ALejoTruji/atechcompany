from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha', 'leido')
    list_filter = ('leido', 'fecha')
    search_fields = ('nombre', 'email', 'asunto')
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'fecha')
    list_editable = ('leido',)
    ordering = ('-fecha',)

    def has_add_permission(self, request):
        return False
