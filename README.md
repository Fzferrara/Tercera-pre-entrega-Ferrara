# Tercera-pre-entrega-Ferrara
PRIMER PASO -- GIT - CREAR UN PROYECTO NUEVO 
1. git --version - chequeo version de GIT instalada
2. git config --list  - chequeo user.name y user.email configurados
3. CREAR PROYECTO NUEVO: dentro de una carpeta nueva (1), abro el GIT BASH (2), y ejecuto "git init nombreproyecto" (3)
4. Dentro de esta nueva carpeta que se creó, abro el VSC
5. Luego para crear el .git en GitHub lo creo directamente desde el VSC, y se crea automaticamente y se ira sincronizando

SEGUNDO PASO -- DJANGO - CREAR UN PROYECTO DE DJANGO 
AMBIENTE VIRTUAL
1. AMBIENTE VIRTUAL - instalar el paquete "virtualenv" - pip3 install virtualenv - RESULTADO: da los comandos de "requirements satisfied"
2. CREAR AMBIENTE VIRTUAL - ejecuto el comando en la carpeta del Proyecto / comando "python -m venv env" - RESULTADO: se crea la carpeta "env" en la carpeta del Proyecto 
	
3. ACTIVAR AMBIENTE VIRTUAL ejecutando el comando "env\Scripts\activate" (CADA VEZ QUE ARRANCAMOS A TRABAJAR)

DJANGO
4. INSTALAR DJANGO EN LA MAQUINA VIRTUAL bajo el comando "pip install django" (recordar que estoy en el ambiente virtual "(env)" ) - (CADA VEZ QUE ARRANCAMOS A TRABAJAR)
5. CREAR PROYECTO DE DJANGO / con el comando "django-admin startproject Proyecto3 ."
	NOTA: el punto final "." es importante para evitar que se cree el proyecto de Django una carpeta dentro de otra. Con el punto final el proyecto Django se crea en la misma carpeta principal.
6. MIGRAR EL MANAGE.PY:
	a. Con la creacion del proyecto de Django, se crea un archivo "manage.py", que es el Controlador del Proyecto. 
	b. Inicialmente me aseguro que el archivo manage.py esté en la carpeta del proyecto, ejecutando "dir" en el CMD dentro del Proyecto. Me deberia mostrar el contenido de la carpeta, y el manage.py dentro
	c. Luego, estando dentro del ambiente virtual "env", dentro de la carpeta que contiene el manage.py ejecuto "python manage.py migrate"
7. EJECUTAR EL SERVIDOR: bajo el comando "python manage.py runserver" - (CADA VEZ QUE ARRANCAMOS A TRABAJAR)


Entrar dentro de la pagina creada y navegar por los diferentes hipervinculos de la cabecera.
