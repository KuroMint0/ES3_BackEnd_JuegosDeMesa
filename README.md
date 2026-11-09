# Evaluación 3 - Back End - Tienda de juegos de mesa

## Integrantes

> - Alexis Sepúlveda
> - Christopher Cortés

## Contexto

Una **tienda de juegos de mesa** quiere publicar su catálogo en línea y recibir pedidos para retiro en tienda. El personal carga
las categorías y los juegos, con la imagen de la caja, desde el panel de administración. Las personas recorren el catálogo, eligen
un juego y hacen su pedido desde el sitio, sin necesidad de crear una cuenta.

## Instalación y ejecución en local

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_REPOSITORIO>
```

### 2. Crear y activar el entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Instalar las dependencias y realizar las migraciones de la BD

```bash
pip install -r requirements.txt
python manage.py migrate
```

### 4. Crear un super usuario

```bash
python manage.py createsuperuser
```

### 5. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Para visualizar la tienda se debe abrir <http://127.0.0.1:8000/> y <http://127.0.0.1:8000/admin/> para abrir el panel de administrador.