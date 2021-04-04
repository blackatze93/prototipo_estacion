from django.db import models
from django.contrib.auth.models import User

ESTADO = (
    (0, "Borrador"),
    (1, "Publicado")
)


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    autor = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE, related_name='blog_posts')
    actualizado = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    estado = models.IntegerField(choices=ESTADO, default=0)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo
