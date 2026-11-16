from django import forms
from .models import Pedido

class formularioPedidos(forms.modelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'correo', 'telefono', 'cant_unidades']
        labels = {
            'nombre_cliente': 'Nombre del Cliente',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'cant_unidades': 'Cantidad de Unidades',
        }
        widgets = {
            "nombre_cliente": forms.TextInput(attrs={"maxlength": 50, "required": True}),
            "correo": forms.EmailInput(attrs={"maxlength": 50, "required": True}),
            "telefono": forms.TextInput(attrs={"maxlength": 15, "required": True}),
            "cant_unidades": forms.NumberInput(attrs={"min": 1, "max": 5, "required": True}),
        }

        def __init__(self, *args, **kwargs):
            self.juego = kwargs.pop("juego", None)
            super().__init__(*args, **kwargs)
            if self.juego is not None:
                self.fields["cant_unidades"].label = f"Cantidad (disponible: {self.juego.stock})"

        def verificar_stock(self):
            cantidad = self.cleaned_data.get("cant_unidades")
            if cantidad is None or cantidad < 1 or cantidad > 5:
                raise forms.ValidationError("La cantidad debe estar entre 1 y 5 unidades.")

            if self.juego is not None:
                if self.juego.stock <= 0:
                    raise forms.ValidationError("El juego está agotado.")
                if cantidad > self.juego.stock:
                    raise forms.validationError(f"Solo hay {self.juego.stock} unidades disponibles.")

            return cantidad