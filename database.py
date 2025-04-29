from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import urllib.parse
from sqlalchemy.dialects.mssql import pymssql

# ===== PARCHE DEFINITIVO PARA pymssql =====
def _fixed_get_server_version_info(self, connection):
    """Versión corregida que maneja correctamente la obtención de versión"""
    version = connection.exec_driver_sql("SELECT CAST(@@version AS VARCHAR)").scalar()
    
    # Implementación manual de _parse_server_version
    if "Microsoft Azure SQL" in version:
        # Ejemplo para Azure SQL
        import re
        match = re.search(r'(\d+)\.(\d+)\.(\d+)', version)
        if match:
            return tuple(int(x) for x in match.groups())
    return (11, 0)  # Versión por defecto si no podemos parsear

pymssql.MSDialect_pymssql._get_server_version_info = _fixed_get_server_version_info
# ===== FIN DEL PARCHE =====

load_dotenv()
Base = declarative_base()

# ========== CONEXIÓN LOCAL: AZURE SQL SERVER ==========
server = "carlos-server.database.windows.net"
database = "DMZ_ColegioUnion"
username = "admin-carlos"
password = "%40root.123"
encoded_password = urllib.parse.quote_plus(password)

# Cadena de conexión para SQLAlchemy con pymssql
connection_string = f"mssql+pymssql://{username}:{password}@{server}/{database}?charset=utf8"

# Motor SQLAlchemy para Azure SQL
engine_sqlserver = create_engine(
    connection_string,
    connect_args={
        "login_timeout": 30,
        "as_dict": False  # Fundamental mantener esto como False
    }
)

# Session maker para SQL Server
SessionLocal_SQLServer = sessionmaker(autocommit=False, autoflush=False, bind=engine_sqlserver)


# ========== CONEXIÓN REMOTA: MYSQL ==========
MYSQL_USER = os.getenv("DB_USER", "u777467137_deviozapp")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD", "Deviozapp10+")
MYSQL_HOST = os.getenv("DB_HOST", "auth-db465.hstgr.io")
MYSQL_PORT = os.getenv("DB_PORT", "3306")
MYSQL_NAME = os.getenv("DB_NAME", "u777467137_deviozapp")

MYSQL_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_NAME}"
engine_mysql = create_engine(MYSQL_URL)
SessionLocal_MySQL = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql)

# ========== CREACIÓN DE TABLAS ==========
def create_sqlserver_tables():
    """Crea todas las tablas definidas en los modelos para SQL Server"""
    Base.metadata.create_all(bind=engine_sqlserver)
    print("Tablas de SQL Server creadas exitosamente")

def create_mysql_tables():
    """Crea todas las tablas definidas en los modelos para MySQL"""
    Base.metadata.create_all(bind=engine_mysql)
    print("Tablas de MySQL creadas exitosamente")

# ========== DEPENDENCIAS DE SESIÓN ==========
def get_db_sqlserver():
    """Generador de sesiones para SQL Server (Azure SQL)"""
    db = SessionLocal_SQLServer()
    try:
        yield db
    finally:
        db.close()

def get_db_mysql():
    """Generador de sesiones para MySQL"""
    db = SessionLocal_MySQL()
    try:
        yield db
    finally:
        db.close()

