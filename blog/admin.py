from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated') 
    list_display=("titulo","contenido",)
    list_filter=("categorias",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)