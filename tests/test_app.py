import pytest
from app.main import create_app  # Ajuste conforme a localização da sua função create_app
from app import db  # ou from app.models import db, dependendo da sua estrutura
from config import TestConfig

@pytest.fixture(scope='module')
def test_app():
    """Fixture para configurar o app Flask para os testes."""
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
def client(test_app):
    """Fixture para obter um cliente de teste."""
    return test_app.test_client()

def test_add_vehicle(client):
    """Teste para adicionar um novo veículo."""
    response = client.post('/vehicles', json={
        'modelo': 'Teste Modelo',
        'marca': 'Teste Marca',
        'ano': 2021,
        'preco': 30000
    })
    assert response.status_code == 201
    assert 'Vehicle added successfully!' in response.get_json()['message']

def test_get_vehicles(client):
    """Teste para listar todos os veículos."""
    response = client.get('/vehicles')
    assert response.status_code == 200
    vehicles = response.get_json()
    assert isinstance(vehicles, list)

def test_update_vehicle(client):
    """Teste para atualizar um veículo existente."""
    # Adicionar um veículo para teste de atualização
    add_response = client.post('/vehicles', json={
        'modelo': 'Modelo Para Atualizar',
        'marca': 'Marca Para Atualizar',
        'ano': 2020,
        'preco': 25000
    })
    vehicle_id = add_response.get_json()['id']

    # Atualizar o veículo adicionado
    update_response = client.put(f'/vehicles/{vehicle_id}', json={
        'modelo': 'Modelo Atualizado',
        'marca': 'Marca Atualizada',
        'ano': 2022,
        'preco': 35000
    })
    assert update_response.status_code == 200
    assert 'Vehicle updated successfully.' in update_response.get_json()['message']

def test_delete_vehicle(client):
    """Teste para deletar um veículo."""
    # Adicionar um veículo para teste de deleção
    add_response = client.post('/vehicles', json={
        'modelo': 'Modelo Para Deletar',
        'marca': 'Marca Para Deletar',
        'ano': 2019,
        'preco': 20000
    })
    vehicle_id = add_response.get_json()['id']

    # Deletar o veículo adicionado
    delete_response = client.delete(f'/vehicles/{vehicle_id}')
    assert delete_response.status_code == 200
    assert 'Vehicle deleted successfully.' in delete_response.get_json()['message']