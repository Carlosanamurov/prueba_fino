
from sqlalchemy.orm import joinedload
from http.client import HTTPException
from sqlalchemy.orm import Session # type: ignore
from models import (DimEstudiantes,
                   HechosDesempeñoEstudiante,
                   DimNivelEducativo,
                   DimBeca,
                   DimCursos,
                   DimDocentes,
                   DimExtracurriculares,
                   DimFecha,
                   DimLocalizacion,
                   DimPadreTutor,
                   DimTipoEvaluacion)
from schemas import DimEstudiantesCreate, HechosDesempeñoEstudianteCreate

# Crear un nuevo estudiante
def create_dim_estudiante(db: Session, estudiante: DimEstudiantesCreate):
    db_estudiante = DimEstudiantes(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

# Obtener estudiantes
def get_dim_estudiantes(db: Session):
    estudiantes = db.query(DimEstudiantes).order_by(DimEstudiantes.ID_Estudiante).all()
    return estudiantes

# Obtener nivel academico
def get_dim_nivel_educativo(db: Session):
    nivel_academico = db.query(DimNivelEducativo).order_by(DimNivelEducativo.ID_Nivel).all()
    return nivel_academico

# Obtener Beca
def get_dim_beca(db: Session):
    beca = db.query(DimBeca).order_by(DimBeca.ID_Beca).all()
    return beca

# Obtener Cursos
def get_dim_cursos(db: Session):
    cursos = db.query(DimCursos).order_by(DimCursos.ID_Curso).all()
    return cursos

# Obtener Docente
def get_dim_docente(db: Session):
    docente = db.query(DimDocentes).order_by(DimDocentes.ID_Docente).all()
    return docente

# Obtener extracurriculares
def get_dim_extracurriculares(db: Session):
    extracurriculares = db.query(DimExtracurriculares).order_by(DimExtracurriculares.ID_Actividad).all()
    return extracurriculares

# obtener Fecha
def get_dim_fecha(db:Session):
    fecha= db.query(DimFecha).order_by(DimFecha.ID_Fecha).all()
    return fecha

# Obtener Localizacion
def get_dim_localizacion(db: Session):
    localiazacion=db.query(DimLocalizacion).order_by(DimLocalizacion.ID_Localizacion).all()
    return localiazacion

# Obetener padre_tutor
def get_dim_padre_tutor(db:Session):
    padre_tutor=db.query(DimPadreTutor).order_by(DimPadreTutor.ID_Padre_Tutor).all()
    return padre_tutor

# Obtener tipo de evaluacion
def get_dim_tipo_evaluacion(db:Session):
    tipo_evaluacion=db.query(DimTipoEvaluacion).order_by(DimTipoEvaluacion.ID_Tipo_Evaluacion).all()
    return tipo_evaluacion

# Obtener desempeño de estudiantes
def get_hechos_desempeño_estudiantes(db: Session):
    hecho_desempeño= db.query(HechosDesempeñoEstudiante).order_by(HechosDesempeñoEstudiante.ID_Estudiante).all()
    return hecho_desempeño


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