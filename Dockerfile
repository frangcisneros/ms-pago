# ms_stock/Dockerfile

FROM python:3.12.7

# Configuración del entorno
ENV FLASK_CONTEXT=development
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

# Crear un usuario no root
RUN useradd --create-home --home-dir /home/flaskapp flaskapp

# Actualizar e instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y python3-dev build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /home/flaskapp

USER flaskapp

# Crear el directorio para la aplicación
RUN mkdir app

# Copiar los archivos de la aplicación
COPY ./app ./app
COPY ./app.py ./

# Copiar el archivo de requisitos
ADD requirements.txt ./requirements.txt

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "./app.py"]
