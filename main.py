from fastapi import FastAPI, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from fastapi import HTTPException # type: ignore
from typing import List

import crud, models, schemas  # Sin el punto, ya que están en el mismo directorio
from database import SessionLocal, engine  # Asumiendo que database.py está en el mismo nivel

# Crear las tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas para DimEstudiantes

@app.post("/estudiantes/", response_model=schemas.DimEstudiantesResponse)
def create_estudiante(estudiante: schemas.DimEstudiantesCreate, db: Session = Depends(get_db)):
    return crud.create_dim_estudiante(db=db, estudiante=estudiante)

@app.get("/estudiantes/", response_model=List[schemas.DimEstudiantesResponse])
def get_estudiantes(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /estudiantes/")
    try:
        estudiantes = crud.get_dim_estudiantes(db=db)
        print("Estudiantes ok")
        return estudiantes
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    

# Endpoint para obtener el desempeño de los estudiantes
@app.get("/desempeño/", response_model=List[schemas.HechosDesempeñoEstudianteResponse])
def get_desempeño_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /desempeño/")
    try:
        # Llamamos a la función CRUD para obtener los datos
        desempeño = crud.get_hechos_desempeño_estudiantes(db=db, skip=skip, limit=limit)
        print("Desempeño de estudiantes ok")
        return desempeño
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
# Endpoint para Obtener Desempeño de un Estudiante Específico (GET por ID de Estudiante)
@app.get("/desempeño/{id_estudiante}", response_model=schemas.HechosDesempeñoEstudianteResponse)
def get_desempeño_estudiante(id_estudiante: int, db: Session = Depends(get_db)):
    desempeño = crud.get_hechos_desempeño_estudiante_por_id(db=db, id_estudiante=id_estudiante)
    if not desempeño:
        raise HTTPException(status_code=404, detail="Desempeño de estudiante no encontrado")
    return desempeño

