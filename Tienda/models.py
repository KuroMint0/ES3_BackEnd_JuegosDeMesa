from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    cant_jugadores = models.PositiveIntegerField()
    edad_min = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='juegos/', blank=True, null=True)
    is_disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cod_identificacion = models.CharField(max_length=20, unique=True)
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)
    cant_unidades = models.PositiveIntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    hora_pedido = models.TimeField(auto_now_add=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido #{self.cod_identificacion}"