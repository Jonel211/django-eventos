from django.contrib import admin
from .models import Autor, Receta, Comentario

# Register your models here.
admin.site.register(Autor)
admin.site.register(Receta)
admin.site.register(Comentario)