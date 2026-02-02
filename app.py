import os
import time
import pymysql
from pymysql import OperationalError

# --- LECTURA DE VARIABLES DE ENTORNO ---
# El script no sabe si es Test 1 o Test 2. Solo lee lo que Kubernetes le da.
db_host = os.environ.get('DATABASE_URL')      # Host (Endpoint RDS)
db_user = os.environ.get('DATABASE_USER')      # Usuario
db_password = os.environ.get('DATABASE_PW')    # Contraseña

# CAMBIO CLAVE: Si no hay variable, usa 'test_db' por defecto, pero intenta leerla.
db_name = os.environ.get('DATABASE_NAME', 'siges-multiprod-test1') 

print(f"--- INICIANDO PRUEBA DE CONEXION MULTIPROD ---")
print(f"Target Host: {db_host}")
print(f"Target DB:  {db_name}")
print(f"User:       {db_user}")

def connect():
    if not db_host or not db_password:
        print("❌ ERROR: Faltan variables de entorno (DATABASE_URL o DATABASE_PW).")
        return False

    try:
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            connect_timeout=5
        )
        conn.close()
        print(f"✅ ¡EXITO! Conectado correctamente a: {db_host} ({db_name})")
        return True
    except Exception as e:
        print(f"❌ ERROR DE CONEXIÓN: {e}")
        return False

while True:
    connect()
    print("Durmiendo 10 segundos...")
    time.sleep(10)