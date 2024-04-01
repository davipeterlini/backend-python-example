from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Veiculo
from config import Config
from crud import adicionar_veiculo, listar_veiculos, atualizar_veiculo, deletar_veiculo

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Creating the database and tables
with app.app_context():
    db.create_all()

# Criação da aplicação e rotas abaixo
@app.route('/veiculos', methods=['GET', 'POST'])
def handle_veiculos():
    if request.method == 'POST':
        data = request.get_json()
        veiculo = adicionar_veiculo(data['modelo'], data['marca'], data['ano'], data['preco'])
        return jsonify({'message': 'Vehicle added successfully!', 'id': veiculo.id}), 201
    else:
        veiculos = listar_veiculos()
        return jsonify([{'id': v.id, 'modelo': v.modelo, 'marca': v.marca, 'ano': v.ano, 'preco': v.preco} for v in veiculos]), 200

@app.route('/veiculos/<int:id>', methods=['PUT', 'DELETE'])
def handle_veiculo(id):
    if request.method == 'PUT':
        data = request.get_json()
        veiculo = atualizar_veiculo(id, data.get('modelo'), data.get('marca'), data.get('ano'), data.get('preco'))
        if veiculo:
            return jsonify({'message': 'Vehicle updated successfully.'}), 200
        else:
            return jsonify({'message': 'Vehicle not found.'}), 404
    elif request.method == 'DELETE':
        if deletar_veiculo(id):
            return jsonify({'message': 'Vehicle deleted successfully.'}), 200
        else:
            return jsonify({'message': 'Vehicle not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
