import sys

print("--- Generando .env desde GitLab CI ---")
try:
    with open('.env', 'w') as f:
        f.write(f"DATABASE_URL={sys.argv[1]}\n")
        f.write(f"DATABASE_USER={sys.argv[2]}\n")
        f.write(f"DATABASE_PW={sys.argv[3]}\n")
    print("✅ Archivo .env generado correctamente.")
except Exception as e:
    print(f"⚠️ Error al generar .env: {e}")
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