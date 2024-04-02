import pytest
from flask_testing import TestCase
from app import create_app  # Importe sua função de fábrica de app, se disponível
from models import db, Veiculo

class TestVeiculoCRUD(TestCase):
    def create_app(self):
        # Configurar sua aplicação Flask para testes
        app = create_app(config_name='testing')
        return app

    def setUp(self):
        # Configurar o banco de dados de teste
        db.create_all()

    def tearDown(self):
        # Limpar o banco de dados de teste após cada teste
        db.session.remove()
        db.drop_all()

    def test_adicionar_veiculo(self):
        # Teste para adicionar um veículo
        with self.client:
            response = self.client.post('/veiculos', json={
                'modelo': 'Teste Modelo',
                'marca': 'Teste Marca',
                'ano': 2020,
                'preco': 15000.00
            })
            self.assertEqual(response.status_code, 201)
            self.assertIn('Veículo adicionado com sucesso!', response.json['message'])

    def test_listar_veiculos(self):
        # Teste para listar veículos
        pass  # Implementar

    def test_atualizar_veiculo(self):
        # Teste para atualizar um veículo
        pass  # Implementar

    def test_deletar_veiculo(self):
        # Teste para deletar um veículo
        pass  # Implementar

# Configuração para rodar os testes com pytest
if __name__ == '__main__':
    pytest.main()
