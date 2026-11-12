from django.urls import path

from . import views


urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("juegos/<int:juego_id>/", views.detalle_juego, name="detalle_juego"),
    path("pedidos/<int:pedido_id>/", views.comprobante, name="comprobante"),
]
