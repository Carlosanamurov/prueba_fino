


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declara la base para tus modelos
Base = declarative_base()

# Aquí puedes configurar tu motor de base de datos
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://SA:CodeWithArjun123@localhost:1433/PRACTIC_01?driver=ODBC+Driver+17+for+SQL+Server"  # O la URL de tu base de datos

# Crear el motor y las sesiones
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"driver": "ODBC Driver 17 for SQL Server"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para crear las tablas
def create_database():
    Base.metadata.create_all(bind=engine)

