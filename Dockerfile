FROM python:3.9-slim
# Use an official lightweight Alpine image.
# FROM alpine:latest

WORKDIR /app

# Install the libraries needed to run a binary compiled in a glibc environment.
# RUN apk add --no-cache libstdc++

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the binary file from the local directory to the working directory in the container.
#COPY ./dist/app_vehicles /app/app_vehicles
COPY ./dist/app_vehicles /app/app_vehicles

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Comando para executar o aplicativo
CMD ["python", "app_vehicles"]
# CMD ["./app/app_vehicles"]