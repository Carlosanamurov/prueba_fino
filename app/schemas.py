# app/schema.py

from pydantic import BaseModel # type: ignore
from datetime import date
from typing import List, Optional

class DimEstudiantesBase(BaseModel):
    ID_Estudiante: int
    Nombre: str
    Apellido: str
    Género: str
    Grado: str
    Sección: str
    Fecha_Ingreso: date
    Correo_Electrónico: str
    class Config:
        from_attributes = True


# DimNivelEducativo
class DimNivelEducativoBase(BaseModel):
    ID_Nivel: int
    Nivel_Educativo: str

    class Config:
        from_attributes = True



# DimLocalizacion
class DimLocalizacionBase(BaseModel):
    ID_Localizacion: int
    Ciudad: str
    Provincia: str

    class Config:
        from_attributes = True



# DimBeca
class DimBecaBase(BaseModel):
    ID_Beca: int
    Tipo_Beca: str

    class Config:
        from_attributes = True



# DimExtracurriculares
class DimExtracurricularesBase(BaseModel):
    ID_Actividad: int
    Actividad: str

    class Config:
        from_attributes = True



# DimPadreTutor
class DimPadreTutorBase(BaseModel):
    ID_Padre_Tutor: int
    Nombre_Padre_Tutor: str
    Apellido_Padre_Tutor: str
    Teléfono: str
    Correo_Electrónico: str

    class Config:
        from_attributes = True



# DimCursos
class DimCursosBase(BaseModel):
    ID_Curso: int
    Nombre_Curso: str
    Grado: str
    Créditos: int
    Nivel_Académico: str
    Duración: int

    class Config:
        from_attributes = True



# DimDocentes
class DimDocentesBase(BaseModel):
    ID_Docente: int
    Nombre: str
    Apellido: str
    Especialidad: str
    Correo_Electrónico: str
    Teléfono: str

    class Config:
        from_attributes = True



# DimFecha
class DimFechaBase(BaseModel):
    ID_Fecha: int
    Fecha: date
    Año: int
    Mes: int
    Trimestre: int
    Día_Semana: str

    class Config:
        from_attributes = True



# DimTipoEvaluacion
class DimTipoEvaluacionBase(BaseModel):
    ID_Tipo_Evaluacion: int
    Tipo_Evaluacion: str

    class Config:
        from_attributes = True       


# Esquema para HechosDesempeñoEstudiante
class HechosDesempeñoEstudianteBase(BaseModel):
    ID_Estudiante: int
    ID_Curso: int
    ID_Docente: int
    ID_Fecha: int
    ID_Tipo_Evaluacion: int
    ID_Nivel: int
    ID_Localizacion: int
    ID_Beca: int
    ID_Actividad: int
    ID_Padre_Tutor: int
    Calificación: Optional[float]
    Asistencia: Optional[int]
    Fecha_Registro: date
    Observaciones: Optional[str]
    
    class Config:
        from_attributes = True   
    

class HechosDesempeñoEstudianteCreate(HechosDesempeñoEstudianteBase):
    pass

class HechosDesempeñoEstudianteResponse(HechosDesempeñoEstudianteBase):
    ID_Hecho: int

    class Config:
        from_attributes = True

class DimEstudiantesCreate(DimEstudiantesBase):
    pass

class DimEstudiantesResponse(DimEstudiantesBase):
    ID_Estudiante: int

    class Config:
        from_attributes = True