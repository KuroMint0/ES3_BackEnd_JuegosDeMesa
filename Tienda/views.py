from django.shortcuts import get_object_or_404, render

from .models import Categoria, Juego, Pedido


def _formatear_pesos(valor):
    return f"${valor:,}".replace(",", ".")


def catalogo(request):
    juegos = Juego.objects.select_related("categoria").filter(is_disponible=True)
    busqueda = request.GET.get("q", "")
    categoria_seleccionada = request.GET.get("categoria", "")

    if busqueda:
        juegos = juegos.filter(nombre__icontains=busqueda)
    if categoria_seleccionada.isdigit():
        juegos = juegos.filter(categoria_id=int(categoria_seleccionada))

    for juego in juegos:
        juego.precio_formateado = _formatear_pesos(juego.precio)

    return render(
        request,
        "Tienda/catalogo.html",
        {
            "juegos": juegos,
            "categorias": Categoria.objects.all(),
            "busqueda": busqueda,
            "categoria_seleccionada": categoria_seleccionada,
        },
    )


def detalle_juego(request, juego_id):
    juego = get_object_or_404(
        Juego.objects.select_related("categoria"),
        pk=juego_id,
        is_disponible=True,
    )
    return render(
        request,
        "Tienda/detalle_juego.html",
        {
            "juego": juego,
            "precio_formateado": _formatear_pesos(juego.precio),
        },
    )


def comprobante(request, pedido_id):
    pedido = get_object_or_404(
        Pedido.objects.select_related("juego"),
        pk=pedido_id,
    )
    total = pedido.cant_unidades * pedido.juego.precio
    return render(
        request,
        "Tienda/comprobante.html",
        {
            "pedido": pedido,
            "total_formateado": _formatear_pesos(total),
        },
    )
