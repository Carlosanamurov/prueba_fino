from fastapi import HTTPException
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

MYSQL_URL_LOCAL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_NAME}"
engine_mysql_local = create_engine(MYSQL_URL_LOCAL)
SessionLocal_MySQL_LO = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_local)


# ========== CONEXIÓN REMOTA: MYSQL ==========
DB_PASSWORD = urllib.parse.quote_plus(os.getenv("DB_REMOTO_PASSWORD", "Deviozapp10+"))

MYSQL_URL_REMOTA = (
    f"mysql+pymysql://{os.getenv('DB_REMOTO_USER', 'u777467137_deviozapp')}:{DB_PASSWORD}"
    f"@{os.getenv('DB_REMOTO_HOST', 'auth-db465.hstgr.io')}:{os.getenv('DB_REMOTO_PORT', '3306')}"
    f"/{os.getenv('DB_REMOTO_NAME', 'u777467137_deviozapp')}"
)

engine_mysql_remoto = create_engine(
    MYSQL_URL_REMOTA,
    pool_recycle=3600,
    pool_pre_ping=True,  # Verifica conexiones antes de usarlas
    connect_args={
        "ssl": {"ssl_disabled": True},
        "connect_timeout": 10  # Requerido para Hostinger
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_remoto)

engine_mysql_remoto = create_engine(MYSQL_URL_REMOTA)
SessionLocal_MySQL_RE = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql_remoto)


# ========== DEPENDENCIAS DE SESIÓN ==========
def get_db_mysql_local():
    """Generador de sesiones para SQL Server (Azure SQL)"""
    db = SessionLocal_MySQL_LO()
    try:
        yield db
    except Exception as e:
        db.close()
        raise HTTPException(
            status_code=500,
            detail=f"Error de conexión remota: {str(e)}"
        )
    finally:
        db.close()

def get_db_mysql_remoto():
    """Generador de sesiones para MySQL"""
    db = SessionLocal_MySQL_RE()
    try:
        yield db
    except Exception as e:
        db.close()
        raise HTTPException(
            status_code=500,
            detail=f"Error de conexión remota: {str(e)}"
        )
    finally:
        db.close()

