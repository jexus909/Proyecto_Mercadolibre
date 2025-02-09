import firebase_admin
from firebase_admin import credentials
from flask import Flask
from flask_restful import Api
from routes import register_routes

# Cargar credenciales de Firebase
cred = credentials.Certificate("api_firebase.json")  # Ajusta el nombre si es diferente
firebase_admin.initialize_app(cred)

app = Flask(__name__)
api = Api(app)

# Registrar rutas
register_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
