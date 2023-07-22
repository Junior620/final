from django.contrib import admin
from .models import AcceuilContact


# Register your models here.

class AdminAcceuilContact(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'detail')


admin.site.register(AcceuilContact, AdminAcceuilContact)
