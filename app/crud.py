from .models import Vehicle
from . import db

def adicionar_vehicle(modelo, marca, ano, preco):
    novo_vehicle = Vehicle(modelo=modelo, marca=marca, ano=ano, preco=preco)
    db.session.add(novo_vehicle)
    db.session.commit()
    return novo_vehicle

def listar_vehicles():
    return Vehicle.query.all()

def atualizar_vehicle(id, modelo, marca, ano, preco):
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
        vehicle.modelo = modelo
        vehicle.marca = marca
        vehicle.ano = ano
        vehicle.preco = preco
        db.session.commit()
        return vehicle
    return None

def deletar_vehicle(id):
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return True
    return False