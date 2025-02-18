## API de Pokémon

Esta es una API basada en Flask que permite obtener información sobre Pokémon desde la PokéAPI.
La API está protegida con autenticación basada en Firebase y proporciona documentación Swagger.

## Características

Obtención de tipos de un Pokémon específico.
Obtención de un Pokémon aleatorio de un tipo dado.
Búsqueda del Pokémon con el nombre más largo dentro de un tipo.
Logs de actividad en archivos rotativos.
Autenticación con Firebase JWT.
Documentación con Swagger.
## Digrama de arbol del proyecto
```sh
Proyecto-API
├── app.py
├── logger_config.py
├── routes.py
├── services.py
├── docs/
│   ├── pokemon_type.yml
│   ├── random_pokemon.yml
│   └── longest_pokemon.yml
├── api_firebase.json
└── logs/
    └── app.log
└──Dokerfile
└──__init__.py
```
## Instalación

1. Crea y activa un entorno virtual:
```sh
python -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate  # En Windows
```
2. Clona este repositorio y cambia a la rama documentacion:
```sh
git clone --branch documentacion --single-branch https://github.com/jexus909/Proyecto_Mercadolibre
    cd Proyecto_Mercadolibre/pokemon_api
```
3. Instala las dependencias que estan dentro de la carpeta pokemon_api:
```sh
pip install -r requirements1.txt
```
4. Configura Firebase agregando el archivo api_firebase.json en la carpeta pokemon_api del proyecto.

Ejecuta la API:
```sh
python app.py
```

## Diagrama de Arquitectua del API REST
![Logo de la API1](https://github.com/jexus909/Proyecto_Mercadolibre/blob/main/pokemon_api-Diagrama%20API1.drawio.png)

## Diagrama de Flujo 
![Logo de la API](https://github.com/jexus909/Proyecto_Mercadolibre/blob/main/pokemon_api-Flujo%20API.drawio.png)



## Endpoints
### 1. Obtener tipos de un Pokémon
```
GET /pokemon/type/{nombre}
```
**Ejemplo de respuesta:**
```json
{
  "pokemon": "pikachu",
  "types": ["electric"]
}
```

### 2. Obtener un Pokémon aleatorio por tipo
```
GET /pokemon/random/{tipo}
```
**Ejemplo de respuesta:**
```json
{
  "type": "fire",
  "random_pokemon": "charmander"
}
```

### 3. Obtener el Pokémon con el nombre más largo dentro de un tipo
```
GET /pokemon/longname/{tipo}
```
**Ejemplo de respuesta:**
```json
{
  "type": "water",
  "total_pokemon": 45,
  "longest_pokemon_name": "blastoise",
  "name_length": 9
}
```

## Autenticación
Todos los endpoints requieren autenticación con Firebase.
Debe enviarse un token en el header `Authorization` en formato:
```
Authorization: Bearer <TOKEN>
```

## Documentación
Swagger está disponible en:
```
http://localhost:5000/apidocs/
```
## SWAGGER
![swagger](https://github.com/jexus909/Proyecto_Mercadolibre/blob/main/swagger.png)
En el se podra hacer el consumo de los endpoint directamente, para lo cual necesitara tener previamente despledo en firebase los usuarios y el archivo .json que permite la comunicación con su API, para obtener el token JWT .

## Logging
Los logs se guardan en `app.log` con rotación automática.
Los logs validan:
Se usa logger.info(), logger.warning(), logger.error(), etc., para registrar eventos importantes en la API.
Se registran eventos como intentos de acceso sin token, autenticaciones exitosas y errores en peticiones a la PokéAPI.
```
[Fecha y Hora] - [Nivel] - [Mensaje]
2025-02-15 10:45:23,123 - INFO - API inicializada y rutas registradas.

```

## Tecnologías utilizadas
- Flask
- Flask-RESTful
- Firebase Admin
- Flasgger (Swagger para Flask)
- Requests

## Autor
- **Jesus Beltran** - [GitHub](https://github.com/jexus909)

## Implementar Docker
Debes previamente tener instalado docker
busca dentro de la carpeta Proyecto-API el archivo Dockerfile
ejecuta en un cmd para windows o una shell para unix
```
docker build -t nombre_de_tu_imagen .

```
Luego revisa que se hubiera creado de forma exitosa la imagen:

```
docker images
```
Dado que necesitamos que el docker permita la conexión con la maquina local debemos ejecutar el siguiente comando para mapear el puerto 
```
docker run -p 5000:5000 nombre_de_tu_imagen
```
---
Este proyecto está basado en la PokéAPI para la obtención de datos.

