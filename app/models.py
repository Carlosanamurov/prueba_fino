# app/models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL, BOOLEAN
from sqlalchemy.orm import relationship
from app.database import Base

Base = declarative_base()

# Modelo para Dim_Estudiantes
class DimEstudiantes(Base):
    __tablename__ = 'Data_Estudiantes'

    ID_Estudiante = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(50))
    Apellido = Column(String(50))
    Género = Column(String(20))
    Grado = Column(String(20))
    Sección = Column(String(1))
    Fecha_Ingreso = Column(Date)
    Correo_Electrónico = Column(String(100))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="estudiante")
    

# Modelo para Dim_Nivel_Educativo
class DimNivelEducativo(Base):
    __tablename__ = 'Data_Nivel_Educativo'

    ID_Nivel = Column(Integer, primary_key=True, index=True)
    Nivel_Educativo = Column(String(50))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="nivel")

# Modelo para Dim_Localizacion
class DimLocalizacion(Base):
    __tablename__ = 'Data_Localizacion'

    ID_Localizacion = Column(Integer, primary_key=True, index=True)
    Ciudad = Column(String(50))
    Provincia = Column(String(50))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="localizacion")

# Modelo para Dim_Beca
class DimBeca(Base):
    __tablename__ = 'Data_Beca'

    ID_Beca = Column(Integer, primary_key=True, index=True)
    Tipo_Beca = Column(String(50))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="beca")

# Modelo para Dim_Extracurriculares
class DimExtracurriculares(Base):
    __tablename__ = 'Data_Extracurriculares'

    ID_Actividad = Column(Integer, primary_key=True, index=True)
    Actividad = Column(String(50))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="actividad")

# Modelo para Dim_Padre_Tutor
class DimPadreTutor(Base):
    __tablename__ = 'Data_Padre_Tutor'

    ID_Padre_Tutor = Column(Integer, primary_key=True, index=True)
    Nombre_Padre_Tutor = Column(String(50))
    Apellido_Padre_Tutor = Column(String(50))
    Teléfono = Column(String(15))
    Correo_Electrónico = Column(String(100))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="padre_tutor")

# Modelo para Dim_Cursos
class DimCursos(Base):
    __tablename__ = 'Data_Cursos'

    ID_Curso = Column(Integer, primary_key=True, index=True)
    Nombre_Curso = Column(String(100))
    Grado = Column(String(50))
    Créditos = Column(Integer)
    Nivel_Académico = Column(String(50))
    Duración = Column(Integer)
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="curso")

# Modelo para Dim_Docentes
class DimDocentes(Base):
    __tablename__ = 'Data_Docentes'

    ID_Docente = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(50))
    Apellido = Column(String(50))
    Especialidad = Column(String(50))
    Correo_Electrónico = Column(String(100))
    Teléfono = Column(String(15))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="docente")

# Modelo para Dim_Fecha
class DimFecha(Base):
    __tablename__ = 'Data_Fecha'

    ID_Fecha = Column(Integer, primary_key=True, index=True)
    Fecha = Column(Date)
    Año = Column(Integer)
    Mes = Column(Integer)
    Trimestre = Column(Integer)
    Día_Semana = Column(String(20))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="fecha")

# Modelo para Dim_Tipo_Evaluacion
class DimTipoEvaluacion(Base):
    __tablename__ = 'Data_Tipo_Evaluacion'

    ID_Tipo_Evaluacion = Column(Integer, primary_key=True, index=True)
    Tipo_Evaluacion = Column(String(50))
    desempeños = relationship("HechosDesempeñoEstudiante", back_populates="tipo_evaluacion")


# Modelo para Hechos_Desempeño_Estudiante
class HechosDesempeñoEstudiante(Base):
    __tablename__ = 'Hechos_Desempeño_Estudiante'

    ID_Hecho = Column(Integer, primary_key=True, index=True)
    ID_Estudiante = Column(Integer, ForeignKey('Data_Estudiantes.ID_Estudiante'))
    ID_Curso = Column(Integer, ForeignKey('Data_Cursos.ID_Curso'))
    ID_Docente = Column(Integer, ForeignKey('Data_Docentes.ID_Docente'))
    ID_Fecha = Column(Integer, ForeignKey('Data_Fecha.ID_Fecha'))
    ID_Tipo_Evaluacion = Column(Integer, ForeignKey('Data_Tipo_Evaluacion.ID_Tipo_Evaluacion'))
    ID_Nivel = Column(Integer, ForeignKey('Data_Nivel_Educativo.ID_Nivel'))
    ID_Localizacion = Column(Integer, ForeignKey('Data_Localizacion.ID_Localizacion'))
    ID_Beca = Column(Integer, ForeignKey('Data_Beca.ID_Beca'))
    ID_Actividad = Column(Integer, ForeignKey('Data_Extracurriculares.ID_Actividad'))
    ID_Padre_Tutor = Column(Integer, ForeignKey('Data_Padre_Tutor.ID_Padre_Tutor'))
    
    Calificación = Column(DECIMAL(5, 2))
    Asistencia = Column(Integer)
    Fecha_Registro = Column(Date)
    Observaciones = Column(String(255))

    # Relaciones
    estudiante = relationship('DimEstudiantes', back_populates='desempeños')
    curso = relationship('DimCursos', back_populates='desempeños')
    docente = relationship('DimDocentes', back_populates='desempeños')
    fecha = relationship('DimFecha', back_populates='desempeños')
    tipo_evaluacion = relationship('DimTipoEvaluacion', back_populates='desempeños')
    nivel = relationship('DimNivelEducativo', back_populates='desempeños')
    localizacion = relationship('DimLocalizacion', back_populates='desempeños')
    beca = relationship('DimBeca', back_populates='desempeños')
    actividad = relationship('DimExtracurriculares', back_populates='desempeños')
    padre_tutor = relationship('DimPadreTutor', back_populates='desempeños')
