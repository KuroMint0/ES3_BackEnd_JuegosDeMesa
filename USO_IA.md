# Uso de Inteligencia Artificial en el Proyecto

---

## 1. Qué herramientas de IA se usaron

* **GitHub Copilot:** Utilizado directamente en el entorno de desarrollo (IDE) para la asistencia en la escritura de los templates y el styles css.
* **Google Gemini:** Utilizado como copiloto de programación y guía técnico para el diseño lógico, auditoría de requerimientos y resolución de errores durante la implementación del backend.

---

## 2. Para qué se usaron

* **Generación y maquetación de interfaz (GitHub Copilot):**
  * Acelerar la creación de la estructura HTML semántica y la herencia de plantillas en Django (`{% extends %}`, `{% block %}`).
  * Sugerir reglas de diseño responsivo, variables CSS, grillas (`CSS Grid`) y estilos visuales consistentes para las tarjetas, formularios y comprobantes.

* **Copiloto de programación, guía lógica y depuración (Google Gemini):**
  * Contrastar el avance del proyecto contra la pauta de requerimientos funcionales para identificar qué flujos faltaban por construir.
  * Orientar sobre cómo estructurar las funciones, formularios y validaciones en Django (sin entregar la solución final cerrada, sino guiando el paso a paso de qué métodos sobreescribir y dónde ubicar cada lógica).
  * Explicar conceptos clave de integridad de datos, como el uso de transacciones atómicas (`transaction.atomic()`), validación personalizada en `ModelForm` y el patrón *Post/Redirect/Get* (PRG) para evitar pedidos duplicados.
  * Interpretar *tracebacks* y guiar en la depuración de excepciones (`TypeError`, `AttributeError`, `NoReverseMatch`) y configuraciones del panel administrativo.

---

## 3. En qué partes del proyecto se aplicaron

### Frontend y Estilos (GitHub Copilot)
* **`templates/Tienda/base.html`:** Estructura base del sitio, barra de navegación y enlaces globales.
* **`templates/Tienda/catalogo.html`:** Grilla de productos, formulario de filtros por nombre/categoría y etiquetas de estado (*Agotado*).
* **`templates/Tienda/detalle_juego.html`:** Vista de detalle del producto, ficha técnica y estructura base del formulario de reserva.
* **`templates/Tienda/comprobante.html`:** Diseño del resumen de confirmación del pedido mediante listas de definición (`<dl>`).
* **`static/styles.css`:** Hoja de estilos completa, incluyendo variables de color, diseño adaptativo (`@media`), tarjetas de productos y estilos de botones/inputs.

### Backend, Administración y Validaciones (Google Gemini)
* **`Tienda/forms.py`:** Orientación sobre cómo armar `formularioPedidos` (`ModelForm`), cómo inyectar dinámicamente la instancia del juego mediante `__init__` y cómo estructurar el método `verificar_stock` para validar rangos y disponibilidad de stock.
* **`Tienda/views.py`:** Guía sobre la arquitectura del flujo `POST` en `detalle_juego`, los pasos para descontar el stock de forma segura dentro de una transacción, la generación de IDs únicos y el uso correcto de `redirect` hacia el comprobante.
* **`Tienda/admin.py`:** Revisión diagnóstica para detectar inconsistencias entre los nombres de campos del modelo `Pedido` y las configuraciones de búsqueda (`search_fields`) y listado (`list_display`).
* **`templates/Tienda/detalle_juego.html` y `static/styles.css`:** Orientación sobre cómo conectar los campos del `ModelForm` con las etiquetas del template existente para conservar la estética y mostrar mensajes de error de validación.