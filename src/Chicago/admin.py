from django.contrib import admin
from .models import Producto, Categoria, Cliente

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)