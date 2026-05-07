FROM python:3.9-slim

RUN pip install pymysql

WORKDIR /app

# Esto copia app.py y también el archivo .env
COPY . .

CMD ["python", "-u", "app.py"]