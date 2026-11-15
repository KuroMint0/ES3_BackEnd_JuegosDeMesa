from django.test import TestCase
from django.contrib import admin
from django.urls import reverse

from .admin import JuegoAdmin
from .models import Categoria, Juego, Pedido
from .templatetags.clp import clp


class FormatoPesosChilenosTests(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nombre="Estrategia")
        self.juego = Juego.objects.create(
            nombre="Juego de prueba",
            descripcion="Un juego para probar el formato.",
            precio=24990,
            cant_jugadores=4,
            edad_min=10,
            stock=3,
            categoria=categoria,
        )

    def test_formatea_pesos_con_puntos_de_miles(self):
        self.assertEqual(clp(24990), "$24.990")
        self.assertEqual(clp(0), "$0")

    def test_formatea_precios_en_catalogo_y_detalle(self):
        catalogo = self.client.get(reverse("catalogo"))
        detalle = self.client.get(
            reverse("detalle_juego", args=[self.juego.pk])
        )

        self.assertContains(catalogo, "$24.990")
        self.assertContains(detalle, "$24.990")
        self.assertEqual(detalle.context["precio_formateado"], "$24.990")

    def test_formatea_total_en_comprobante_y_precio_en_admin(self):
        pedido = Pedido.objects.create(
            cod_identificacion="PED-001",
            nombre_cliente="Persona de prueba",
            correo="persona@example.com",
            telefono="123456789",
            cant_unidades=2,
            juego=self.juego,
        )
        comprobante = self.client.get(
            reverse("comprobante", args=[pedido.pk])
        )
        precio_admin = JuegoAdmin(Juego, admin.site).precio_formateado(
            self.juego
        )

        self.assertContains(comprobante, "$49.980")
        self.assertEqual(precio_admin, "$24.990")
