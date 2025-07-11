<em> # mercadito-uoh </em>
App web para la compra/venta de productos o servicios entre la comunidad universitaria. 

# Instrucciones de uso
Tener Python 🧑‍🦲
En la cmd instalar virtualenv para usar en la carpeta matriz del proyecto 
```
pip install virtualenv
```
En la carpeta del proyecto crear un virtualenv con:
```
virtualenv <name>
```
Para activar el virtualenv, debemos activar una opción de Windows. Para ello, abrir **Windows Powershell** como administrador y usar:
```
Set-ExecutionPolicy Unrestricted
```
Aceptar usando 'S' y luego volviendo a la cmd, activar el ambiente con el path:
```
.\<name>\Scripts\activate
```
Para confirmar que se activó el ambiente, al ejecutar ```python --version ``` al lado del path aparecerá entre paréntesis el nombre del ambiente.
Ya con el ambiente listo, usar:
```
code .
```
Una vez dentro del editor verificar el ambiente, crear una ventana y usar:
```
pip install django
pip install psycopg2
```
Para iniciar el proyecto usar en la terminal:
```
python manage.py runserver
```
Copiar la url local en el navegador y para más comandos usar:
```
pyhton manage.py help
```
