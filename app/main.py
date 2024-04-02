from flask import Flask, jsonify, request
from . import db  # Importa a inicialização do SQLAlchemy
from config import Config  # Importa as configurações
from .crud import adicionar_vehicle, listar_vehicles, atualizar_vehicle, deletar_vehicle
    

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def hello():
        return "Hello, World!"

    @app.route('/vehicles', methods=['GET', 'POST'])
    def handle_vehicles():
        if request.method == 'POST':
            data = request.get_json()
            vehicle = adicionar_vehicle(data['modelo'], data['marca'], data['ano'], data['preco'])
            return jsonify({'message': 'Vehicle added successfully!', 'id': vehicle.id}), 201
        else:
            vehicles = listar_vehicles()
            return jsonify([{'id': v.id, 'modelo': v.modelo, 'marca': v.marca, 'ano': v.ano, 'preco': v.preco} for v in vehicles]), 200

    @app.route('/vehicles/<int:id>', methods=['PUT', 'DELETE'])
    def handle_vehicle(id):
        if request.method == 'PUT':
            data = request.get_json()
            vehicle = atualizar_vehicle(id, data.get('modelo'), data.get('marca'), data.get('ano'), data.get('preco'))
            if vehicle:
                return jsonify({'message': 'Vehicle updated successfully.'}), 200
            else:
                return jsonify({'message': 'Vehicle not found.'}), 404
        elif request.method == 'DELETE':
            if deletar_vehicle(id):
                return jsonify({'message': 'Vehicle deleted successfully.'}), 200
            else:
                return jsonify({'message': 'Vehicle not found.'}), 404

    return app
