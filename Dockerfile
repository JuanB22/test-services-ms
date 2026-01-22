# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Instalamos el conector de MySQL
RUN pip install pymysql

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos nuestro script
COPY app.py .

# Ejecutamos el script
# "-u" hace que los logs salgan inmediatamente en la consola de Kubernetes
CMD ["python", "-u", "app.py"]