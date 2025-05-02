from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import urllib.parse
from sqlalchemy.dialects.mssql import pymssql


load_dotenv()
Base = declarative_base()

# ========== CONEXIÓN LOCAL: MYSQL ==========
MYSQL_USER = os.getenv("DB_USER", "root")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD", "root.123")
MYSQL_HOST = os.getenv("DB_HOST", "localhost")
MYSQL_PORT = os.getenv("DB_PORT", "3306")
MYSQL_NAME = os.getenv("DB_NAME", "DVZ_ColegioUnion")

MYSQL_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_NAME}"
engine_mysql_local = create_engine(MYSQL_URL)
SessionLocal_MySQL_LO = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_local)


# ========== CONEXIÓN REMOTA: MYSQL ==========
MYSQL_USER = os.getenv("DB_USER", "u777467137_deviozapp")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD", "Deviozapp10+")
MYSQL_HOST = os.getenv("DB_HOST", "auth-db465.hstgr.io")
MYSQL_PORT = os.getenv("DB_PORT", "3306")
MYSQL_NAME = os.getenv("DB_NAME", "u777467137_deviozapp")

MYSQL_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_NAME}"
engine_mysql_remoto = create_engine(MYSQL_URL)
SessionLocal_MySQL_RE = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_remoto)

# ========== CREACIÓN DE TABLAS ==========
def create_sqlserver_tables():
    """Crea todas las tablas definidas en los modelos para SQL Server"""
    Base.metadata.create_all(bind=engine_mysql_local)
    print("Tablas de SQL Server creadas exitosamente")

def create_mysql_tables():
    """Crea todas las tablas definidas en los modelos para MySQL"""
    Base.metadata.create_all(bind=engine_mysql_remoto)
    print("Tablas de MySQL creadas exitosamente")

# ========== DEPENDENCIAS DE SESIÓN ==========
def get_db_sqlserver():
    """Generador de sesiones para SQL Server (Azure SQL)"""
    db = SessionLocal_MySQL_LO()
    try:
        yield db
    finally:
        db.close()

def get_db_mysql():
    """Generador de sesiones para MySQL"""
    db = SessionLocal_MySQL_RE()
    try:
        yield db
    finally:
        db.close()

