from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import database

app = FastAPI(title="FondaFinder PA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    database.init_db()

class FondaCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    barrio: str
    lat: Optional[float] = None
    lng: Optional[float] = None
    precio_rango: str
    precio_promedio: Optional[float] = None
    menu: Optional[str] = None

class ReporteCreate(BaseModel):
    fonda_id: int
    tipo: str
    descripcion: Optional[str] = None

@app.get("/fondas")
async def list_fondas(
    q: str = Query(default="", max_length=100),
    barrio: Optional[str] = None,
    precio_rango: Optional[str] = None,
) -> dict:
    conn = database.get_db_connection()
    query = "SELECT * FROM fondas WHERE status = 'approved'"
    params = []
    
    if q:
        query += " AND (nombre LIKE ? OR descripcion LIKE ? OR barrio LIKE ?)"
        search = f"%{database.normalize_text(q)}%"
        params.extend([search, search, search])
    
    if barrio:
        query += " AND barrio = ?"
        params.append(database.normalize_text(barrio))
        
    if precio_rango:
        query += " AND precio_rango = ?"
        params.append(precio_rango)
        
    fondas = conn.execute(query, params).fetchall()
    conn.close()
    return {"fondas": [dict(f) for f in fondas]}

@app.post("/fondas")
async def create_fonda(fonda: FondaCreate):
    conn = database.get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO fondas (
                nombre, descripcion, barrio, lat, lng,
                precio_rango, precio_promedio, menu, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'approved')
        ''', (
            database.normalize_text(fonda.nombre),
            database.normalize_text(fonda.descripcion),
            database.normalize_text(fonda.barrio),
            fonda.lat,
            fonda.lng,
            fonda.precio_rango,
            fonda.precio_promedio,
            database.normalize_text(fonda.menu),
        ))
        conn.commit()
        return {"message": "Fonda registrada exitosamente", "id": cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()

@app.post("/reportes")
async def create_reporte(reporte: ReporteCreate):
    conn = database.get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reportes (fonda_id, tipo, descripcion)
            VALUES (?, ?, ?)
        ''', (reporte.fonda_id, reporte.tipo, reporte.descripcion))
        conn.commit()
        return {"message": "Reporte enviado"}
    finally:
        conn.close()

@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
