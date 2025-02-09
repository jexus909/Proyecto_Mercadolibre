from flask_restful import Api
from services import PokemonType 
from services import RandomPokemonByType
from services import LongestPokemonNameByType

def register_routes(api: Api):
    """Registra los endpoints en la API."""
    api.add_resource(PokemonType, "/pokemon/type/<string:name>")
    api.add_resource(RandomPokemonByType, "/pokemon/random/<string:type_name>")
    api.add_resource(LongestPokemonNameByType,"/pokemon/longname/<string:long_name>")
