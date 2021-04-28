from django.contrib import admin

from .models import Producto, Categoria

# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    
    list_filter=("nombre",)
    readonly_fields=("created", "updated")
    
class productoAdmin(admin.ModelAdmin):
    list_filter=("precio",)
    list_display=("nombre","precio","categorias","disponibilidad",)
    readonly_fields=("created", "updated")
    

admin.site.register(Categoria, categoriaAdmin)
admin.site.register(Producto, productoAdmin)