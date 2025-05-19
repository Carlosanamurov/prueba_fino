from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import text
import app.database
import app.models
import app.schemas
from sqlalchemy.inspection import inspect

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Crear las tablas si no existen


appp = FastAPI()

# Obtener la sesión de la base de datos
def get_db():
    db = app.database.SessionLocal_MySQL_LO()
    try:
        yield db
    finally:
        db.close()


# Rutas para DimEstudiantes

@appp.get("/estudiantes", response_model=List[app.schemas.DimEstudiantesBase],include_in_schema=False)
def get_estudiantes(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /estudiantes/")
    try:
        estudiantes = app.crud.get_dim_estudiantes(db=db)
        print("Estudiantes ok")
        return  JSONResponse(content=jsonable_encoder(estudiantes), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@appp.get("/beca", response_model=List[app.schemas.DimBecaBase],include_in_schema=False)
def get_beca(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /beca/")
    try:
        beca = app.crud.get_dim_beca(db=db)
        print("beca ok")
        return  JSONResponse(content=jsonable_encoder(beca), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@appp.get("/cursos", response_model=List[app.schemas.DimCursosBase],include_in_schema=False)
def get_cursos(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /cursos/")
    try:
        cursos = app.crud.get_dim_cursos(db=db)
        print("cursos ok")
        return  JSONResponse(content=jsonable_encoder(cursos), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@appp.get("/docentes", response_model=List[app.schemas.DimDocentesBase],include_in_schema=False)
def get_beca(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /docentes/")
    try:
        docentes = app.crud.get_dim_docente(db=db)
        print("docentes ok")
        return  JSONResponse(content=jsonable_encoder(docentes), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@appp.get("/extracurriculares", response_model=List[app.schemas.DimExtracurricularesBase],include_in_schema=False)
def get_extracurriculares(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /extracurriculares/")
    try:
        extracurriculares = app.crud.get_dim_extracurriculares(db=db)
        print("extracurriculares ok")
        return  JSONResponse(content=jsonable_encoder(extracurriculares), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    


@appp.get("/fechas", response_model=List[app.schemas.DimFechaBase],include_in_schema=False)
def get_fecha(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /fechas/")
    try:
        fechas = app.crud.get_dim_fecha(db=db)
        print("fechas ok")
        return  JSONResponse(content=jsonable_encoder(fechas), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    

@appp.get("/nivel_educativo", response_model=List[app.schemas.DimNivelEducativoBase],include_in_schema=False)
def get_nivel_educativo(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /nivel_educativo/")
    try:
        nivel_educativo = app.crud.get_dim_nivel_educativo(db=db)
        print("nivel_educativo ok")
        return  JSONResponse(content=jsonable_encoder(nivel_educativo), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)



@appp.get("/localizaciones", response_model=List[app.schemas.DimLocalizacionBase],include_in_schema=False)
def get_localizacion(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /localizacion/")
    try:
        localizacion = app.crud.get_dim_localizacion(db=db)
        print("localizacion ok")
        return  JSONResponse(content=jsonable_encoder(localizacion), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")



@appp.get("/padres_tutor", response_model=List[app.schemas.DimPadreTutorBase],include_in_schema=False)
async def get_padre_tutor(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /padres_tutor/")
    try:
        padre_tutor = app.crud.get_dim_padre_tutor(db=db)
        print("padre_tutor ok")
        return  JSONResponse(content=jsonable_encoder(padre_tutor), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
    

@appp.get("/tipo_evaluacion", response_model=List[app.schemas.DimTipoEvaluacionBase],include_in_schema=False)
async def get_tipo_evaluacion(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /tipo_evaluacion/")
    try:
        tipo_evaluacion = app.crud.get_dim_tipo_evaluacion(db=db)
        print("tipo_evaluacion ok")
        return  JSONResponse(content=jsonable_encoder(tipo_evaluacion), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")


@appp.get("/desempeño", response_model=List[app.schemas.HechosDesempeñoEstudianteBase],include_in_schema=False)
async def get_hecho_desempeño(db: Session = Depends(get_db)):
    print("🔍 Se está llamando al endpoint /Hecho desempeño/")
    try:
        desempeño = app.crud.get_hechos_desempeño_estudiantes(db=db)
        print("desempeño ok")
        return  JSONResponse(content=jsonable_encoder(desempeño), media_type="application/json; charset=utf-8")
    except Exception as e:
        print("🔥 Error interno:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
    


# Endpoint para obtener el desempeño de los estudiantes


@appp.post("/sincronizar")
def sincronizar_datos(
    db_local: Session = Depends(app.database.get_db_mysql_local),
    db_remoto: Session = Depends(app.database.get_db_mysql_remoto)
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
        {"modelo": app.models.DimEstudiantes, "nombre": "DimEstudiantes"},
        {"modelo": app.models.DimDocentes, "nombre": "DimDocentes"},
        {"modelo": app.models.DimCursos, "nombre": "DimCursos"},
        {"modelo": app.models.DimBeca, "nombre": "DimBeca"},
        {"modelo": app.models.DimExtracurriculares, "nombre": "DimExtracurriculares"},
        {"modelo": app.models.DimFecha, "nombre": "DimFecha"},
        {"modelo": app.models.DimLocalizacion, "nombre": "DimLocalizacion"},
        {"modelo": app.models.DimNivelEducativo, "nombre": "DimNivelEducativo"},
        {"modelo": app.models.DimPadreTutor, "nombre": "DimPadreTutor"},
        {"modelo": app.models.DimTipoEvaluacion, "nombre": "DimTipoEvaluacion"},
        {"modelo": app.models.HechosDesempeñoEstudiante, "nombre": "HechosDesempeñoEstudiante"}
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






