from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud, models, schemas  # Sin el punto, ya que están en el mismo directorio
from database import (
    Base,
    engine_sqlserver,
    engine_mysql,
    get_db_sqlserver,
    get_db_mysql,
    SessionLocal_SQLServer,
    SessionLocal_MySQL
)
from models import (DimEstudiantes, DimDocentes, DimCursos,
                    DimBeca,DimExtracurriculares,DimFecha,
                    DimLocalizacion,DimNivelEducativo,
                    DimPadreTutor,DimTipoEvaluacion)
from sqlalchemy.inspection import inspect
from schemas import (DimEstudiantesBase,HechosDesempeñoEstudianteBase,
                     DimBecaBase,DimCursosBase,DimDocentesBase,
                     DimExtracurricularesBase,DimFechaBase,
                     DimLocalizacionBase,DimPadreTutorBase,
                     DimNivelEducativoBase,DimTipoEvaluacionBase)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Crear las tablas si no existen
models.Base.metadata.create_all(bind=engine_sqlserver)

app = FastAPI()

# Obtener la sesión de la base de datos
def get_db():
    db = SessionLocal_SQLServer()
    try:
        yield db
    finally:
        db.close()


# Rutas para DimEstudiantes
@app.post("/estudiantes/", response_model=schemas.DimEstudiantesResponse)
def create_estudiante(estudiante: schemas.DimEstudiantesCreate, db: Session = Depends(get_db)):
    return crud.create_dim_estudiante(db=db, estudiante=estudiante)




@app.get("/estudiantes/", response_model=List[DimEstudiantesBase],include_in_schema=False)
def get_estudiantes(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /estudiantes/")
    try:
        estudiantes = crud.get_dim_estudiantes(db=db)
        print("Estudiantes ok")
        return  JSONResponse(content=jsonable_encoder(estudiantes), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/beca/", response_model=List[DimBecaBase],include_in_schema=False)
def get_beca(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /beca/")
    try:
        beca = crud.get_dim_beca(db=db)
        print("beca ok")
        return  JSONResponse(content=jsonable_encoder(beca), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@app.get("/cursos/", response_model=List[DimCursosBase],include_in_schema=False)
def get_cursos(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /cursos/")
    try:
        cursos = crud.get_dim_cursos(db=db)
        print("cursos ok")
        return  JSONResponse(content=jsonable_encoder(cursos), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@app.get("/docentes/", response_model=List[DimBecaBase],include_in_schema=False)
def get_beca(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /docentes/")
    try:
        docentes = crud.get_dim_docente(db=db)
        print("docentes ok")
        return  JSONResponse(content=jsonable_encoder(docentes), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/extracurriculares/", response_model=List[DimExtracurricularesBase],include_in_schema=False)
def get_extracurriculares(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /extracurriculares/")
    try:
        extracurriculares = crud.get_dim_extracurriculares(db=db)
        print("extracurriculares ok")
        return  JSONResponse(content=jsonable_encoder(extracurriculares), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    


@app.get("/fechas/", response_model=List[DimFechaBase],include_in_schema=False)
def get_fecha(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /fechas/")
    try:
        fechas = crud.get_dim_fecha(db=db)
        print("fechas ok")
        return  JSONResponse(content=jsonable_encoder(fechas), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    

@app.get("/nivel_educativo/", response_model=List[DimFechaBase],include_in_schema=False)
def get_nivel_educativo(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /nivel_educativo/")
    try:
        nivel_educativo = crud.get_dim_nivel_educativo(db=db)
        print("nivel_educativo ok")
        return  JSONResponse(content=jsonable_encoder(nivel_educativo), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)



@app.get("/localizaciones/", response_model=List[DimLocalizacionBase],include_in_schema=False)
def get_localizacion(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /localizacion/")
    try:
        localizacion = crud.get_dim_localizacion(db=db)
        print("localizacion ok")
        return  JSONResponse(content=jsonable_encoder(localizacion), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")



@app.get("/padres_tutor/", response_model=List[DimPadreTutorBase],include_in_schema=False)
def get_padre_tutor(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /padres_tutor/")
    try:
        padre_tutor = crud.get_dim_padre_tutor(db=db)
        print("padre_tutor ok")
        return  JSONResponse(content=jsonable_encoder(padre_tutor), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
    

@app.get("/tipo_evaluacion/", response_model=List[DimTipoEvaluacionBase],include_in_schema=False)
def get_tipo_evaluacion(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /tipo_evaluacion/")
    try:
        tipo_evaluacion = crud.get_dim_tipo_evaluacion(db=db)
        print("tipo_evaluacion ok")
        return  JSONResponse(content=jsonable_encoder(tipo_evaluacion), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")


  
    
    


# Endpoint para obtener el desempeño de los estudiantes
@app.get("/desempeño/", response_model=List[HechosDesempeñoEstudianteBase],include_in_schema=False)
def get_desempeño_estudiantes(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /desempeño/")
    try:
        # Llamamos a la función CRUD para obtener los datos
        desempeño = crud.get_hechos_desempeño_estudiantes(db=db)
        print("Desempeño de estudiantes ok")
        return JSONResponse(content=jsonable_encoder(desempeño), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
    
    
# Endpoint para Obtener Desempeño de un Estudiante Específico (GET por ID de Estudiante)
@app.get("/desempeño/{id_estudiante}", response_model=schemas.HechosDesempeñoEstudianteResponse)
def get_desempeño_estudiante(id_estudiante: int, db: Session = Depends(get_db)):
    desempeño = crud.get_hechos_desempeño_estudiante_por_id(db=db, id_estudiante=id_estudiante)
    if not desempeño:
        raise HTTPException(status_code=404, detail="Desempeño de estudiante no encontrado")
    return JSONResponse(content=jsonable_encoder(desempeño), media_type="application/json; charset=utf-8")
    

#--- Sincronizar----#


def get_dict(model_instance):
    return {
        column.name: getattr(model_instance, column.name)
        for column in model_instance.__table__.columns
    }

@app.post("/sincronizar")
def sincronizar_datos(
    db_local: Session = Depends(get_db_sqlserver),
    db_remoto: Session = Depends(get_db_mysql)
):
    tablas = [
        {"modelo": DimEstudiantes, "nombre": "DimEstudiantes"},
        {"modelo": DimDocentes, "nombre": "DimDocentes"},
        {"modelo": DimCursos, "nombre": "DimCursos"},
        {"modelo": DimBeca, "nombre": "DimBeca"},
        {"modelo": DimExtracurriculares, "nombre": "DimExtracurriculares"},
        {"modelo": DimFecha, "nombre": "DimFecha"},
        {"modelo": DimLocalizacion, "nombre": "DimLocalizacion"},
        {"modelo": DimNivelEducativo, "nombre": "DimNivelEducativo"},
        {"modelo": DimPadreTutor, "nombre": "DimPadreTutor"},
        {"modelo": DimTipoEvaluacion, "nombre": "DimTipoEvaluacion"}
    ]

    resultados = {}

    for tabla in tablas:
        modelo = tabla["modelo"]
        nombre_tabla = tabla["nombre"]

        try:
            datos_locales = db_local.query(modelo).all()
            pk_column = list(modelo.__table__.primary_key.columns)[0]
            ids_remotos = {
                getattr(e, pk_column.name)
                for e in db_remoto.query(pk_column).all()
            }

            nuevos = [
                modelo(**get_dict(fila))
                for fila in datos_locales
                if getattr(fila, pk_column.name) not in ids_remotos
            ]

            if nuevos:
                db_remoto.add_all(nuevos)
                db_remoto.commit()

            resultados[nombre_tabla] = f"{len(nuevos)} nuevos registros sincronizados."

        except Exception as e:
            resultados[nombre_tabla] = f"Error: {str(e)}"

    return {"resultado": resultados}