# Proyecto API

Esta es una API basada en Flask que permite obtener información sobre Pokémon desde la PokéAPI.
La API está protegida con autenticación basada en Firebase y proporciona documentación Swagger.

## Características
- Obtención de tipos de un Pokémon específico.
- Obtención de un Pokémon aleatorio de un tipo dado.
- Búsqueda del Pokémon con el nombre más largo dentro de un tipo.
- Logs de actividad en archivos rotativos.
- Autenticación con Firebase JWT.
- Documentación con Swagger.

## NOTA
Caracteristicas de cada rama:
1. Master: Solo incluye el consumo de los endpoints
2. Autenticacion: Se implementa la configuración de la autenticación y validación del token JWT usando firebase
3. Trazabilidad: Se crea la configuración de loggin de las actividades de los endpoint y eventos relevantes del API
4. Documentación: Esta rama tiene el proyecto completo con la integración de Firebase, la configuración de los logs, y la creación de la documentación

## Instalación
1. Clona este repositorio:
    ```sh
    git clone https://github.com/jexus909/Proyecto_Mercadolibre
    cd Proyecto_Mercadolibre
    ```
2. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
3. Configura Firebase agregando el archivo `api_firebase.json` en la carpeta principal del proyecto.
4. Ejecuta la API:
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

---
Este proyecto está basado en la PokéAPI para la obtención de datos.

