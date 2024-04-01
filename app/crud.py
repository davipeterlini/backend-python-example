from models import db, Veiculo

def adicionar_veiculo(modelo, marca, ano, preco):
    novo_veiculo = Veiculo(modelo=modelo, marca=marca, ano=ano, preco=preco)
    db.session.add(novo_veiculo)
    db.session.commit()
    return novo_veiculo

def listar_veiculos():
    return Veiculo.query.all()

def atualizar_veiculo(id, modelo, marca, ano, preco):
    veiculo = Veiculo.query.filter_by(id=id).first()
    if veiculo:
        veiculo.modelo = modelo
        veiculo.marca = marca
        veiculo.ano = ano
        veiculo.preco = preco
        db.session.commit()
        return veiculo
    return None

def deletar_veiculo(id):
    veiculo = Veiculo.query.filter_by(id=id).first()
    if veiculo:
        db.session.delete(veiculo)
        db.session.commit()
        return True
    return False