from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from Tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.catalogo, name="catalogo"),
    path("juegos/<int:juego_id>/", views.detalle_juego, name="detalle_juego"),
    path("pedidos/<int:pedido_id>/", views.comprobante, name="comprobante"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

