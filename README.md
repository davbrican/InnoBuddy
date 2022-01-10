# InnoBuddy
InnoBuddy es un bot de Telegram creado para ayudar a los participantes en las Jornadas InnoSoft de la Universidad de Sevilla. La idea es que puedan estar informados de las novedades de las jornadas y puedan consultar información útil como las ponencias, eventos, localización de las aulas...

## Arquitectura
El bot está creado en Python, comunicándose con una base de datos MySQL. Los credenciales y tokens necesarios deben situarse en un archivo .env en la raíz del proyecto. Se incluye un archivo template.env con ejemplos no funcionales de todos los secrets necesarios para que funcione el bot en su totalidad.

## Iniciar el bot
La <b>primera</b> vez que queremos arrancar el bot, una vez tenemos un servicio MySQL, tenemos que popular la base de datos para crear tablas y datos de prueba. El script es el siguiente:
```
python ./src/db/populate.py
```
Una vez tenemos populada la base de datos el bot funcionará correctamente, podemos iniciarlo con el siguiente comando:
```
python ./src/main.py
```
## Funcionamiento a nivel de usuario
El bot cuenta con un comando <b>/help</b> que ayuda al usuario a conocer todas las funcionalidades del bot y su funcionamiento.

## Despliegue en contenedores Docker
Para desplegar el proyecto como contenedores Docker (de forma local) debemos situarnos en la carpeta del proyecto y ejecutar el siguiente comando:
```
docker-compose -f ./docker/docker-compose.yml --project-directory . up
```
Esto hace que se creen 2 contenedores (innobuddy y mysql) y 1 volumen para que persistan los datos de la base de datos.
Como hemos visto en el inicio del bot, si es la primera vez que ejecutamos este despliegue tendremos que popular la base de datos. Esto podemos hacerlo facilmente con el siguiente comando:
```
docker exec -it ID_CONTENEDOR python ./src/db/populate.py
```
Sustituyendo ID_CONTENEDOR por el id del contenedor de <b>MySQL</b>.
