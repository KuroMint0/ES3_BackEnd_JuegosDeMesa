from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Juego, Pedido

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_formateado', 'cant_jugadores', 'edad_min', 'stock', 'disponibilidad', 'miniatura')
    list_filter = ('categoria', 'is_disponible')
    search_fields = ('nombre',)

    def precio_formateado(self, obj):
        return f"${obj.precio}".replace(',', '.')

    @admin.display(description="Disponibilidad")
    def disponibilidad(self, obj):
        return "Disponible" if obj.is_disponible else "No disponible"

    @admin.display(description="Imagen")
    def miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px;" />',
                obj.imagen.url
            )
        return 'Sin imagen'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_cliente', 'cant_unidades', 'fecha_pedido')
    list_filter = ('juego',)
    search_fields = ('nombre', 'correo')

    def codigo(self, obj):
        return f"Pedido #{obj.cod_identificacion}"