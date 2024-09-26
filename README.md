# Loja de Veículos Online

## Organization Project


backend-python-example/
│
├── app/                # Contém o código fonte da aplicação.
│   ├── __init__.py
│   ├── main.py         # Ponto de entrada da aplicação
│   ├── models.py       # Define os modelos de dados
│   └── crud.py         # Operações CRUD
├── tests/              # Contém os testes da aplicação.
│   ├── __init__.py
│   └── test_app.py     # Testes da aplicação
├── run.py/             # Contém os testes da aplicação.
├── config.py           # Configurações do aplicativo
|
├── Dockerfile
├── docker-compose.yml  # Docker compose para PostgreSQL e H2
├── requirements.txt    # Dependências Python
├── .env                    # Variáveis de ambiente
└── README.md           # Instruções de setup e uso

## Setup Inicial

### Requisitos

- Python 3.8+
- Docker e Docker Compose
- Homebrew (para usuários MAC)

### Install

1. Install Homebrew
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python
```shell
brew install python
brew link --overwrite python@3.12
# brew reinstall python@3.12
python3 --version
pip3 --version
```

3. Clone o repositório:
```shell
git clone git@github.com:davipeterlini/backend-python-example.git
```

4. Create Struture
```shell
cd scripts  
python3 create_struture.py
```

## Execute APP

1. Create o Virtual Enviroment
```shell
python3 -m venv virtual_enviroment
source virtual_enviroment/bin/activate
# Stop virtual enviroment
deactivate
```

2. Install dependencies
```shell
pip3 install -r requirements.txt
pip install Flask-SQLAlchemy
```

3. Docker Up
```shell
docker-compose up -d
```

4. Exec APP
```shell
python run.py
```

5. Run tests
```shell
curl http://localhost:5000/
# POST
curl -X POST http://localhost:5000/vehicles \
     -H 'Content-Type: application/json' \
     -d '{"modelo": "Modelo Exemplo", "marca": "Marca Exemplo", "ano": 2020, "preco": 35000}'
# GET
curl http://localhost:5000/vehicles
# UPDATE
curl -X PUT http://localhost:5000/vehicles/1 \
-H 'Content-Type: application/json' \
-d '{"modelo": "Modelo Atualizado", "marca": "Marca Atualizada", "ano": 2021, "preco": 50000}'
# DELETE
curl -X DELETE http://localhost:5000/vehicles/1
```

6. Database Validation
```shell
# Open Dbeaver --> Create a New Connection --> Create a SQLite with instance/vehicles.db --> Open Editor and exec query: 
SELECT * FROM vehicles;
```

## Execute APP Test

1. Adding Dependencies in requirements.txt
```shell
pytest
pytest-flask
Flask-Testing
coverage
```

2. Update virtual enviroment
```shell
source virtual_enviroment/bin/activate
pip install -r requirements.txt
```

3. Exec APP Tests
```shell
pytest tests/
```

4. Coverage Test
```shell
coverage run -m pytest tests/
coverage report
```


## Create Binary Packge

1. Dependencies
```shell
source virtual_enviroment/bin/activate
pip install pyinstaller
```

2. Install pyinstaller
```shell
cd scripts
chmod +x generate_bynary.sh
./generate_bynary.sh
```

3. Run Binary
```shell
chmod +x dist/app_vehicles
./dist/app_vehicles
```

## Generatge Image

1. Create Image
```shell
docker build -t app_image .
docker build -t app_image:latest .
docker build --no-cache -t app_image:latest .
```

2. Run image with docker
```shell
docker run -p 5000:5000 app_image:latest
docker run -d -p 5000:5000 app_image:latest
```

3. Run tests
```shell
curl http://localhost:5000/
curl -d '{"chave":"valor"}' -H "Content-Type: application/json" -X POST http://localhost:5000/caminho_do_recurso
```


# Docker compose to build 
docker-compose up --build

