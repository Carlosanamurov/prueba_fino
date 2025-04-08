from database import SessionLocal
from models import DimEstudiantes

# Crear sesión
db = SessionLocal()

# Intentar obtener datos
estudiantes = db.query(DimEstudiantes).all()

if estudiantes:
    print("Datos encontrados en Dim_Estudiantes:")
    for est in estudiantes:
        print(est.ID_Estudiante, est.Nombre, est.Apellido)
else:
    print("⚠️ No se encontraron datos en la tabla Dim_Estudiantes.")