# Usa una imagen base oficial
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /opt/app

# Copia los requirements (si tienes)
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia la aplicación FastAPI
COPY ./app /opt/app/app

# Expone el puerto
EXPOSE 8000

# Comando por defecto para correr FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
