import firebase_admin
from firebase_admin import credentials
from flask import Flask
from flask_restful import Api
from routes import register_routes
from logger_config import logger  # Importamos el logger desde el módulo


# Cargar credenciales de Firebase
cred = credentials.Certificate("api_firebase.json")  # Ajusta el nombre si es diferente
firebase_admin.initialize_app(cred)

app = Flask(__name__)
api = Api(app)

# Registrar rutas
register_routes(api)
logger.info("API inicializada y rutas registradas.")  # Agregamos un mensaje de inicio

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

