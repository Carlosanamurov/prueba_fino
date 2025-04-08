# app/schemas.py

from pydantic import BaseModel # type: ignore
from datetime import date
from typing import List, Optional

class DimEstudiantesBase(BaseModel):
    Nombre: str
    Apellido: str
    Género: str
    Grado: str
    Sección: str
    Fecha_Ingreso: date
    Correo_Electrónico: str

class DimEstudiantesCreate(DimEstudiantesBase):
    pass

class DimEstudiantesResponse(DimEstudiantesBase):
    ID_Estudiante: int

    class Config:
        orm_mode = True

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

class HechosDesempeñoEstudianteCreate(HechosDesempeñoEstudianteBase):
    pass

class HechosDesempeñoEstudianteResponse(HechosDesempeñoEstudianteBase):
    ID_Hecho: int

    class Config:
        orm_mode = True
