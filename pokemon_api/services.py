from flask_restful import Resource
import requests
import random
import json

class PokemonType(Resource):
    """Obtiene el tipo del Pokémon desde la PokéAPI."""
    def get(self, name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Pokemon no encontrado"}, 404

        data = response.json()
        
        types = []  # Crear una lista vacía para almacenar los tipos

        for t in data["types"]:  # Iterar sobre la lista "types" en el JSON
            types.append(t["type"]["name"])  # Extraer el nombre del tipo y agregarlo a la lista

        return {"pokemon": name, "types": types}

class RandomPokemonByType(Resource):
    """Obtiene un Pokémon aleatorio de un tipo específico."""
    def get(self, type_name):
        url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Tipo de Pokemon no encontrado"}, 404

        data = response.json()
        pokemon_list = data.get("pokemon", [])

        if not pokemon_list:
            return {"error": "No hay Pokémon disponibles para este tipo"}, 404

        # 🔹 Usamos un for normal para extraer los nombres de los Pokémon
        pokemon_names = []
        for p in pokemon_list:
            pokemon_names.append(p["pokemon"]["name"])

        # Elegir un Pokémon al azar
        random_pokemon = random.choice(pokemon_names)

        return {"type": type_name, "random_pokemon": random_pokemon}


class LongestPokemonNameByType(Resource):
    """Encuentra el Pokémon con el nombre más largo de un tipo específico."""

    def get(self, long_name):
        url = f"https://pokeapi.co/api/v2/type/{long_name.lower()}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Tipo de Pokémon no encontrado"}, 404

        data = response.json()
        pokemon_list = data.get("pokemon", [])

        if not pokemon_list:
            return {"error": "No hay Pokémon disponibles para este tipo"}, 404

        # Variables para encontrar el nombre más largo
        longest_pokemon = None
        max_length = 0

        #print("\ Lista de Pokémon de tipo", long_name.upper())

        for p in pokemon_list:
            name = p["pokemon"]["name"]
            name_length = len(name)

            #print(f" Comparando: {name} ({name_length} caracteres) vs. actual más largo: {longest_pokemon} ({max_length} caracteres)")

            # 🔹 Aseguramos que el Pokémon con el nombre más largo se guarde correctamente
            if name_length > max_length:
                longest_pokemon = name
                max_length = name_length
                #print(f" Nuevo más largo encontrado: {longest_pokemon} ({max_length} caracteres)")

        return {
            "type": long_name,
            "total_pokemon": len(pokemon_list),
            "longest_pokemon_name": longest_pokemon,
            "name_length": max_length
        }
            
        