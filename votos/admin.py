from django.contrib import admin
from .models import Departamento,Provincia,Municipio,Localidad,Recinto,Boleta,Jurado

# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
    readonly_fields=()
    
class ProvinciaAdmin(admin.ModelAdmin):
    readonly_fields=()
    
class MunicipioAdmin(admin.ModelAdmin):
    readonly_fields=()
    
class LocalidadAdmin(admin.ModelAdmin):
    readonly_fields=()
    
class RecintoAdmin(admin.ModelAdmin):
    readonly_fields=()
    
class BoletaAdmin(admin.ModelAdmin):
    readonly_fields=()
    
class JuradoAdmin(admin.ModelAdmin):
    readonly_fields=()

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Recinto, RecintoAdmin)
admin.site.register(Boleta, BoletaAdmin)
admin.site.register(Jurado, JuradoAdmin)


