# Usa una imagen oficial de Python como base
FROM python:3.11

# Configurar el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la API al contenedor
COPY . /app

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements1.txt

# Exponer el puerto en el que Flask correrá
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
