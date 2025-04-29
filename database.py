from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv


load_dotenv()
Base = declarative_base()


# ========== CONEXIÓN LOCAL: SQL SERVER ==========
#SQLSERVER_URL = "mssql+pyodbc://SA:CodeWithArjun123@localhost:1433/DVZ_ColegioUnion?driver=ODBC+Driver+17+for+SQL+Server"
SQLSERVER_URL="mssql+pyodbc://admin-carlos%40carlos-server:%40root.123@carlos-server.database.windows.net:1433/DVZ_ColegioUnion?driver=ODBC+Driver+18+for+SQL+Server&encrypt=yes&trustservercertificate=yes&Connection+Timeout=30"



engine_sqlserver = create_engine(SQLSERVER_URL)
SessionLocal_SQLServer = sessionmaker(autocommit=False, autoflush=False, bind=engine_sqlserver)

# ========== CONEXIÓN REMOTA: MYSQL ==========
# Asegúrate que estas variables estén definidas como variables de entorno en Render o tu .env local
MYSQL_USER = os.getenv("DB_USER", "u777467137_deviozapp")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD", "Deviozapp10+")
MYSQL_HOST = os.getenv("DB_HOST", "auth-db465.hstgr.io")
MYSQL_PORT = os.getenv("DB_PORT", "3306")
MYSQL_NAME = os.getenv("DB_NAME", "u777467137_deviozapp")

MYSQL_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_NAME}"

#MYSQL_URL = "mysql+mysqlconnector://u777467137_deviozapp:TU_CONTRASEÑA@nombre_host_remoto/nombre_bd"


engine_mysql = create_engine(MYSQL_URL)
SessionLocal_MySQL = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql)

# ========== OPCIONAL: Crear tablas para SQL Server ==========
def create_sqlserver_database():
    Base.metadata.create_all(bind=engine_sqlserver)

# ========== OPCIONAL: Crear tablas para MySQL ==========
def create_mysql_database():
    Base.metadata.create_all(bind=engine_mysql)

# Dependencia para obtener sesión SQL Server
def get_db_sqlserver():
    db = SessionLocal_SQLServer()
    try:
        yield db
    finally:
        db.close()

# Dependencia para obtener sesión MySQL
def get_db_mysql():
    db = SessionLocal_MySQL()
    try:
        yield db
    finally:
        db.close()
