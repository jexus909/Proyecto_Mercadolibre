from flask_restful import Resource, reqparse
import requests
import random
import json
from flask import request
from firebase_admin import auth
from functools import wraps

def token_required(f):
    """Middleware para validar el token JWT de Firebase."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")  # Extraer token del encabezado
        
        if not token:
            return {"error": "Token faltante"}, 401

        try:
            # Verificar token eliminando "Bearer " del inicio si existe
            token = token.replace("Bearer ", "")
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token  # Almacenar datos del usuario autenticado
        except Exception as e:
            return {"error": "Token inválido o expirado"}, 401

        return f(*args, **kwargs)
    return decorated

class PokemonType(Resource):
    """Obtiene el tipo del Pokémon desde la PokéAPI."""
    @token_required  # 🔐 Ahora este endpoint requiere autenticación
    def get(self, name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Pokemon no encontrado"}, 404

        data = response.json()
        types = [t["type"]["name"] for t in data["types"]]

        return {"pokemon": name, "types": types}

class RandomPokemonByType(Resource):
    """Obtiene un Pokémon aleatorio de un tipo específico."""
    @token_required
    def get(self, type_name):
        url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Tipo de Pokemon no encontrado"}, 404

        data = response.json()
        pokemon_list = data.get("pokemon", [])

        if not pokemon_list:
            return {"error": "No hay Pokémon disponibles para este tipo"}, 404

        random_pokemon = random.choice([p["pokemon"]["name"] for p in pokemon_list])

        return {"type": type_name, "random_pokemon": random_pokemon}

class LongestPokemonNameByType(Resource):
    """Encuentra el Pokémon con el nombre más largo de un tipo específico."""
    @token_required
    def get(self, long_name):
        url = f"https://pokeapi.co/api/v2/type/{long_name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Tipo de Pokémon no encontrado"}, 404

        data = response.json()
        pokemon_list = data.get("pokemon", [])

        if not pokemon_list:
            return {"error": "No hay Pokémon disponibles para este tipo"}, 404

        longest_pokemon = max(pokemon_list, key=lambda p: len(p["pokemon"]["name"]))["pokemon"]["name"]

        return {
            "type": long_name,
            "total_pokemon": len(pokemon_list),
            "longest_pokemon_name": longest_pokemon,
            "name_length": len(longest_pokemon)
        }
