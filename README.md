# mercadito-uoh
App web para la compra/venta de productos o servicios entre la comunidad universitaria. 

## Instrucciones de uso

### 1. Requisitos

- Tener Python instalado 
- Tener PostgreSQL instalado  

---

### 2. Crear y activar un entorno virtual

En la terminal (CMD o PowerShell), instala `virtualenv`:

```bash
pip install virtualenv
```
En la carpeta del proyecto crear un virtualenv con:
```
virtualenv venv
```
Para activar el virtualenv, debemos activar una opción de Windows. Para ello, abrir **Windows Powershell** como administrador y usar:
```
Set-ExecutionPolicy Unrestricted
```
Aceptar usando 'S' y luego volviendo a la cmd, activar el ambiente con el path:
```
.\venv\Scripts\activate
```
Para confirmar que se activó el ambiente, al ejecutar ```python --version ``` al lado del path aparecerá entre paréntesis el nombre del ambiente.  
Ya con el ambiente listo, usar:
```
code .
```
---
### 3. Instalar dependencias
Una vez dentro del editor (o fuera si uno lo prefiere) verificar el ambiente, crear un terminal y usar:
```
pip install django
pip install psycopg2
```
---
### 4. Restaurar la base de datos

Usa una interfaz gráfica de PostgreSQL (como **pgAdmin**) o la terminal para crear la base de datos del proyecto.

Asegúrate de que los datos de conexión definidos en `settings.py` coincidan exactamente con los usados al crear la base de datos. Por ejemplo:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mercadito',      #Nombre de la base de datos
        'USER': 'postgres',       #Usuario de PostgreSQL
        'PASSWORD': 'postgres',   #Contraseña del usuario
        'HOST': 'localhost',      #Dirección del servidor (normalmente localhost)
        'PORT': '5432',           #Puerto por defecto de PostgreSQL
    }
}
```
**Importante:** Si modificas alguno de estos valores (por ejemplo, el nombre de la base o la contraseña), recuerda actualizar también settings.py para que Django pueda conectarse correctamente.

### 5. Activar base de datos
Debe verificar que la direccion donde se encuentra PostgreSQL esta añadida al PATH, en el caso de que no lo este, siga los siguientes pasos:
Buscar la carpeta donde esta instalada PostgreSQL, por ejemplo:
```makefile
C:\Program Files\PostgreSQL\15\bin
```
Copiar esa ruta y agregarla al PATH del sistema: 

Ir al Panel de control > Sistema > Configuración avanzada del sistema > Variables de entorno.
Buscar la variable Path en "Variables del sistema" y hacer clic en Editar.
Agregar una nueva entrada con la ruta de la carpeta bin.
Aceptar los cambios, cerrar y volver a abrir la terminal.

Para importar la base de datos, en la terminal CMD, ejecutar:
```bash
psql -U tu_usuario -d nombre_de_tu_base -f archivo.sql
```
Para asegurar que la base de datos tengo las tablas/filas necesarias, ocupar:
```bash
python manage.py makemigrations
python manage.py migrate
````
Para iniciar el proyecto usar en la terminal:
```bash
python manage.py runserver
```
Copiar la url local en el navegador y para más comandos usar:
```bash
python manage.py help
```
### 6. Adicional
Si se desea crear un administrador (super-usuario) usar:
```bash
python manage.py createsuperuser
```
Dentro del panel de admin (esto es ir a '/admin/' luego de runserver para ir al panel administrador), se pueden crear usuarios.
