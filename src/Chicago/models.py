from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Talle(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    descripcion = models.TextField()
    marca = models.CharField(max_length=20, default="Necesita especificar")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    color = models.CharField(max_length=15, null=True, blank=True, default="Sin especificar")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.descripcion

class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='stocks')
    talle = models.ForeignKey(Talle, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.descripcion} - Talle {self.talle.nombre} ({self.cantidad} disponibles)"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"