import os
import time
import pymysql

# --- CÓDIGO TEMPORAL PARA LEER EL ARCHIVO DE GITLAB CI ---
def load_env_file():
    if os.path.exists('.env'):
        with open('.env') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value # Las inyectamos en la memoria
        print("✅ Variables cargadas desde el archivo .env de GitLab")
    else:
        print("⚠️ No se encontró archivo .env")

# Ejecutamos la función antes de leer las variables
load_env_file()
# ---------------------------------------------------------

# El resto de tu código queda EXACTAMENTE IGUAL. 
# os.environ.get ahora encontrará las variables gracias a la función de arriba.
db_host = os.environ.get('DATABASE_URL')      
db_user = os.environ.get('DATABASE_USER')    
db_password = os.environ.get('DATABASE_PW')   
db_name = os.environ.get('DATABASE_NAME', 'test1DB') 

print(f"--- INICIANDO PRUEBA DE CONEXION MULTIPROD ---")
print(f"Target Host: {db_host}")
# ... (sigue tu función connect)

# import os
# import time
# import pymysql
# from pymysql import OperationalError


# db_host = os.environ.get('DATABASE_URL')      
# db_user = os.environ.get('DATABASE_USER')    
# db_password = os.environ.get('DATABASE_PW')   
# db_name = os.environ.get('DATABASE_NAME', 'test1DB') 

# print(f"--- INICIANDO PRUEBA DE CONEXION MULTIPROD ---")
# print(f"Target Host: {db_host}")
# print(f"Target DB:  {db_name}")
# print(f"User:       {db_user}")

# db_hostname = db_host.split(":")[0]
# db_port = int(db_host.split(":")[1])

# def connect():
#     if not db_host or not db_password:
#         print(" ERROR: Faltan variables de entorno (DATABASE_URL o DATABASE_PW).")
#         return False

#     try:
#         conn = pymysql.connect(
#             host=db_hostname,
#             user=db_user,
#             port=db_port,
#             password=db_password,
#             database=db_name,
#             connect_timeout=5
#         )
#         conn.close()
#         print(f" ¡EXITO! Conectado correctamente a: {db_host} ({db_name})")
#         return True
#     except Exception as e:
#         print(f"ERROR DE CONEXIÓN: {e}")
#         return False

# while True:
#     connect()
#     print("Durmiendo 10 segundos...")
#     time.sleep(10)