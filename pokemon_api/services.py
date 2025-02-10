from flask_restful import Resource, reqparse
import requests
import random
import json
from flask import request
from firebase_admin import auth
from functools import wraps
from logger_config import logger  # Importamos el logger desde el módulo

def token_required(f):
    """Middleware para validar el token JWT de Firebase."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")  # Extraer token del encabezado

        if not token:
            logger.warning("Intento de acceso sin token.")
            return {"error": "Token faltante"}, 401

        try:
            # Verificar token eliminando "Bearer " del inicio si existe
            token = token.replace("Bearer ", "")
            decoded_token = auth.verify_id_token(token)

            # Obtener datos del usuario autenticado
            uid = decoded_token.get("uid")
            email = decoded_token.get("email", "Desconocido")
            name = decoded_token.get("name", "Desconocido")

            # Guardar el usuario en la solicitud
            request.user = decoded_token  

            # Registrar información en los logs
            logger.info(f"Usuario autenticado UID: {uid}, Email: {email}, Nombre: {name}")

        except Exception as e:
            logger.error(f"Error de autenticación: {str(e)}")
            return {"error": "Token inválido o expirado"}, 401

        return f(*args, **kwargs)
    return decorated


class PokemonType(Resource):
    """Obtiene el tipo del Pokemon desde la PokéAPI."""
    @token_required
    def get(self, name):
        logger.info(f"Solicitud de tipo de Pokemon para: {name} por usuario {request.user.get('uid')}")
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            logger.warning(f"Pokemon no encontrado: {name}")
            return {"error": "Pokemon no encontrado"}, 404

        data = response.json()
        types = [t["type"]["name"] for t in data["types"]]
        logger.info(f"Tipos de Pokemon obtenidos para {name}: {types}")

        return {"pokemon": name, "types": types}

class RandomPokemonByType(Resource):
    """Obtiene un Pokemon aleatorio de un tipo específico."""
    @token_required
    def get(self, type_name):
        logger.info(f"Solicitud de Pokemon aleatorio para el tipo: {type_name} por usuario {request.user.get('uid')}")
        url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            logger.warning(f"Tipo de Pokemon no encontrado: {type_name}")
            return {"error": "Tipo de Pokemon no encontrado"}, 404

        data = response.json()
        pokemon_list = data.get("pokemon", [])

        if not pokemon_list:
            logger.warning(f"No hay Pokemon disponibles para el tipo: {type_name}")
            return {"error": "No hay Pokemon disponibles para este tipo"}, 404

        random_pokemon = random.choice([p["pokemon"]["name"] for p in pokemon_list])
        logger.info(f"Pokemon aleatorio obtenido: {random_pokemon} para el tipo {type_name}")

        return {"type": type_name, "random_pokemon": random_pokemon}

class LongestPokemonNameByType(Resource):
    """Encuentra el Pokemon con el nombre mas largo de un tipo específico."""
    @token_required
    def get(self, long_name):
        logger.info(f"Solicitud de Pokemon con nombre mas largo para el tipo: {long_name} por usuario {request.user.get('uid')}")
        url = f"https://pokeapi.co/api/v2/type/{long_name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            logger.warning(f"Tipo de Pokemon no encontrado: {long_name}")
            return {"error": "Tipo de Pokemon no encontrado"}, 404

        data = response.json()
        pokemon_list = data.get("pokemon", [])

        if not pokemon_list:
            logger.warning(f"No hay Pokemon disponibles para el tipo: {long_name}")
            return {"error": "No hay Pokemon disponibles para este tipo"}, 404

        longest_pokemon = max(pokemon_list, key=lambda p: len(p["pokemon"]["name"]))["pokemon"]["name"]
        logger.info(f"Pokemon con el nombre mas largo: {longest_pokemon} (longitud {len(longest_pokemon)})")

        return {
            "type": long_name,
            "total_pokemon": len(pokemon_list),
            "longest_pokemon_name": longest_pokemon,
            "name_length": len(longest_pokemon)
        }
