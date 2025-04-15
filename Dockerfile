FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer el puerto donde corre FastAPI
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]