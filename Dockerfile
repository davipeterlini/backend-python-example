FROM python:3.9-slim

WORKDIR /app

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the binary file from the local directory to the working directory in the container.
#COPY ./dist/app_veiculos /app/app_veiculos
COPY dist/app_veiculos /app/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Comando para executar o aplicativo
CMD ["python", "./app_veiculos.py"]