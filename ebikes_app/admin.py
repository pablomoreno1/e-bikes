from django.contrib import admin

from ebikes_app.models import Bicicleta, Insumo, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Bicicleta)
admin.site.register(Insumo)