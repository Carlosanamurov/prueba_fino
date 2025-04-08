

from http.client import HTTPException
from sqlalchemy.orm import Session # type: ignore
from models import DimEstudiantes, HechosDesempeñoEstudiante
from schemas import DimEstudiantesCreate, HechosDesempeñoEstudianteCreate

# Crear un nuevo estudiante
def create_dim_estudiante(db: Session, estudiante: DimEstudiantesCreate):
    db_estudiante = DimEstudiantes(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

# Obtener estudiantes
def get_dim_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    estudiantes = db.query(DimEstudiantes).order_by(DimEstudiantes.ID_Estudiante).offset(skip).limit(limit).all()
    return estudiantes

# Obtener desempeño de estudiantes
def get_hechos_desempeño_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HechosDesempeñoEstudiante).order_by(HechosDesempeñoEstudiante.ID_Estudiante).offset(skip).limit(limit).all()

# Obtener Desempeño de un Estudiante Específico (GET por ID de Estudiante)
def get_hechos_desempeño_estudiante_por_id(db: Session, id_estudiante: int):
    return db.query(HechosDesempeñoEstudiante).filter(HechosDesempeñoEstudiante.ID_Estudiante == id_estudiante).first()


#########################


# Crear un nuevo desempeño de estudiante
def create_hecho_desempeño_estudiante(db: Session, desempeño: HechosDesempeñoEstudianteCreate):
    db_desempeño = HechosDesempeñoEstudiante(**desempeño.dict())
    db.add(db_desempeño)
    db.commit()
    db.refresh(db_desempeño)
    return db_desempeño