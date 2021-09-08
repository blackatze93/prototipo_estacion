from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'slug', 'estado', 'autor', 'actualizado', 'creado')
    list_filter = ('estado',)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    summernote_fields = ('contenido',)

    def save_model(self, request, obj, form, change):
        if not obj.autor:
            obj.autor = request.user
        obj.save()


# Register your models here.
admin.site.register(Post, PostAdmin)

