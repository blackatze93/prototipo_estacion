from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'estado', 'autor', 'actualizado', 'creado')
    list_filter = ('estado',)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}


# Register your models here.
admin.site.register(Post, PostAdmin)

