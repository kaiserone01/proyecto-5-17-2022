"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Planeta
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/user', methods=['POST'])
def create_user():
    # POST request
        body = request.get_json() # get the request body content
        if body is None:
            return "The request body is null", 400
        if 'nombre' not in body:
            return 'You need to specify the nombre',400
        if 'email' not in body:
            return 'You need to specify the email', 400
        if 'password' not in body:
            return 'You need to specify the password', 400   
       

        newUser=User(nombre=body["nombre"],email=body["email"],password=body["password"],is_active=True)
        db.session.add(newUser)
        db.session.commit()
        
    

        return jsonify(newUser.serialize()), 200

@app.route('/user', methods=['GET'])
def listausuarios():
    user = User.query.all()
    user_serializado = list(map(lambda user: user.serialize(),user))
    return jsonify(user_serializado), 200


@app.route('/personajes', methods=['POST'])
def create_person():
    # POST request
        body = request.get_json() # get the request body content
        if body is None:
            return "The request body is null", 400
        if 'nombre' not in body:
            return 'You need to specify the first_name',400
        if 'tipo' not in body:
            return 'You need to specify the last_name', 400
        if 'poder' not in body:
            return 'You need to specify the last_name', 400

        newPersonaje=Personajes(nombre=body["nombre"], tipo=body["tipo"], poder=body["poder"])
        db.session.add(newPersonaje)
        db.session.commit()
        
    

        return jsonify(newPersonaje.serialize()), 200

@app.route('/personajes', methods=['GET'])
def listapersonajes():
    personajes = Personajes.query.all()
    personajes_serializado = list(map(lambda personaje: personaje.serialize(),personajes))
    return jsonify(personajes_serializado), 200

@app.route('/planetas', methods=['POST'])
def create_planeta():
    # POST request
        body = request.get_json() # get the request body content
        if body is None:
            return "The request body is null", 400
        if 'nombre' not in body:
            return 'You need to specify the nombre',400
        if 'habitable' not in body:
            return 'You need to specify the habitable', 400
        if 'clima' not in body:
            return 'You need to specify the clima', 400

        newPlaneta=Planeta(nombre=body["nombre"], habitable=body["habitable"], clima=body["clima"])
        db.session.add(newPlaneta)
        db.session.commit()
        
    

        return jsonify(newPlaneta.serialize()), 200

@app.route('/planetas', methods=['GET'])
def listadeplanetas():
    planeta = Planeta.query.all()
    planeta_serializado = list(map(lambda planeta: planeta.serialize(),planeta))
    return jsonify(planeta_serializado), 200
    






@app.route('/')
def sitemap():
    return generate_sitemap(app)

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
