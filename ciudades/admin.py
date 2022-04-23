from django.contrib import admin
from .models import Ciudad

class CiudadAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

admin.site.register(Ciudad, CiudadAdmin)