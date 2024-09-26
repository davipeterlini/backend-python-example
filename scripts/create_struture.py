# Script para criar a estrutura de pastas e diretórios do projeto CRUD de veículos

import os

# Estrutura de pastas do projeto
estrutura_pastas = [
    "../app",
    "../tests",
]

# Criar as pastas
for pasta in estrutura_pastas:
    os.makedirs(pasta, exist_ok=True)

# Criar arquivos __init__.py para tornar os diretórios em pacotes Python
for pasta in estrutura_pastas:
    with open(os.path.join(pasta, '__init__.py'), 'w') as f:
        pass

# Caminhos dos arquivos principais a serem criados
arquivos_principais = [
    "../app/main.py",
    "../app/models.py",
    "../app/config.py",
    "../app/crud.py",
    "../tests/test_app.py",
    "../Dockerfile",
    "../docker-compose.yml",
    "../requirements.txt",
    "../README.md",
]

# Criar os arquivos principais
for arquivo in arquivos_principais:
    with open(arquivo, 'w') as f:
        pass

# Exibir os caminhos dos arquivos e pastas criados
arquivos_e_pastas_criados = estrutura_pastas + arquivos_principais
arquivos_e_pastas_criados
