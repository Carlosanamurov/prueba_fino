from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import text

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
                    DimPadreTutor,DimTipoEvaluacion,HechosDesempeñoEstudiante)
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
@app.post("/sincronizar")
def sincronizar_datos(
    db_local: Session = Depends(get_db_sqlserver),
    db_remoto: Session = Depends(get_db_mysql)
):
    tabla_config = {
        "DimEstudiantes": ("Data_Estudiantes", "pract_01_Data_Estudiantes"),
        "DimDocentes": ("Data_Docentes", "pract_01_Data_Docentes"),
        "DimCursos": ("Data_Cursos", "pract_01_Data_Cursos"),
        "DimBeca": ("Data_Beca", "pract_01_Data_Beca"),
        "DimExtracurriculares": ("Data_Extracurriculares", "pract_01_Data_Extracurriculares"),
        "DimFecha": ("Data_Fecha", "pract_01_Data_Fecha"),
        "DimLocalizacion": ("Data_Localizacion", "pract_01_Data_Localizacion"),
        "DimNivelEducativo": ("Data_NivelEducativo", "pract_01_Data_Nivel_Educativo"),
        "DimPadreTutor": ("Data_PadreTutor", "pract_01_Data_Padre_Tutor"),
        "DimTipoEvaluacion": ("Data_TipoEvaluacion", "pract_01_Data_Tipo_Evaluacion"),
        "HechosDesempeñoEstudiante":("Hechos_Desempeño_Estudiante","pract_01_Hechos_Desempeño_Estudiante")
    }

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
        {"modelo": DimTipoEvaluacion, "nombre": "DimTipoEvaluacion"},
        {"modelo": HechosDesempeñoEstudiante, "nombre": "HechosDesempeñoEstudiante"}
    ]

    resultados = {}

    for tabla in tablas:
        modelo = tabla["modelo"]
        nombre_modelo = tabla["nombre"]
        
        if nombre_modelo not in tabla_config:
            resultados[nombre_modelo] = "Error: Tabla no configurada."
            continue

        nombre_tabla_local, nombre_tabla_remota = tabla_config[nombre_modelo]

        try:
            # 1. Obtener datos locales
            datos_locales = db_local.query(modelo).all()
            
            # 2. Obtener IDs existentes en remoto
            pk_column = list(modelo.__table__.primary_key.columns)[0].name
            ids_remotos = {row[0] for row in db_remoto.execute(text(f"SELECT {pk_column} FROM {nombre_tabla_remota}"))}

            # 3. Filtrar registros nuevos
            nuevos = [
                {c.name: getattr(fila, c.name) for c in modelo.__table__.columns}
                for fila in datos_locales
                if getattr(fila, pk_column) not in ids_remotos
            ]

            # 4. Insertar en remoto
            if nuevos:
                columnas = nuevos[0].keys()
                placeholders = ", ".join([f":{c}" for c in columnas])
                query = text(
                    f"INSERT INTO {nombre_tabla_remota} ({', '.join(columnas)}) "
                    f"VALUES ({placeholders})"
                )
                db_remoto.execute(query, nuevos)
                db_remoto.commit()

            resultados[nombre_modelo] = f"{len(nuevos)} registros sincronizados."

        except Exception as e:
            resultados[nombre_modelo] = f"Error: {str(e)}"
            db_remoto.rollback()

    return {"resultado": resultados}
