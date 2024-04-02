import pytest
from app.main import create_app  # Importação ajustada para a localização atual de create_app
from app import db  # Ajuste conforme necessário, baseado na localização de db
from config import TestConfig

# Opcional: importar modelos se necessário para os testes
# from app.models import Veiculo

@pytest.fixture(scope='module')
def test_app():
    """
    Cria uma instância do app Flask configurada para testes.
    """
    app = create_app()
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,  # Desativa o CSRF para os testes
    })

    # Cria o contexto da aplicação
    with app.app_context():
        db.create_all()
        yield app  # Isso permite o uso do aplicativo nos testes
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(test_app):
    """
    Cria um cliente de teste para enviar requisições ao app.
    """
    return test_app.test_client()

# Exemplo de função de teste
def test_add_vehicle(client):
    """Testa a adição de um novo veículo."""
    response = client.post('/vehicles', json={
        'modelo': 'Teste Modelo', 
        'marca': 'Teste Marca', 
        'ano': 2021, 
        'preco': 30000
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Vehicle added successfully!'
    assert 'id' in data

# Inclua mais funções de teste conforme necessário para cobrir as operações CRUD.
