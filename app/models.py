from . import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(128), nullable=False)
    marca = db.Column(db.String(128), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, modelo, marca, ano, preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def __repr__(self):
        return f'<Vehicle {self.modelo}>'