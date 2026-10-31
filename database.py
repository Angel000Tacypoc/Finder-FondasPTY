import json
import sqlite3
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "fondafinder.db"
SEED_PATH = BASE_DIR / "fondas.json"


def normalize_text(value):
    if not isinstance(value, str):
        return value
    return "".join(
        char
        for char in unicodedata.normalize("NFKD", value)
        if not unicodedata.combining(char)
    )


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fondas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            barrio TEXT NOT NULL,
            lat REAL,
            lng REAL,
            precio_rango TEXT CHECK(precio_rango IN ('$', '$$', '$$$')),
            precio_promedio REAL,
            menu TEXT,
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'approved', 'rejected')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reportes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fonda_id INTEGER NOT NULL,
            tipo TEXT CHECK(tipo IN ('cerrado', 'price_changed', 'menu_changed')),
            descripcion TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (fonda_id) REFERENCES fondas (id)
        )
    ''')
    
    normalize_existing_fondas(conn)
    seed_initial_fondas(conn)
    conn.commit()
    conn.close()


def normalize_existing_fondas(conn):
    rows = conn.execute(
        "SELECT id, nombre, descripcion, barrio, menu FROM fondas"
    ).fetchall()
    for row in rows:
        conn.execute(
            """
            UPDATE fondas
            SET nombre = ?, descripcion = ?, barrio = ?, menu = ?
            WHERE id = ?
            """,
            (
                normalize_text(row["nombre"]),
                normalize_text(row["descripcion"]),
                normalize_text(row["barrio"]),
                normalize_text(row["menu"]),
                row["id"],
            ),
        )


def seed_initial_fondas(conn):
    if not SEED_PATH.exists():
        return

    with SEED_PATH.open("r", encoding="utf-8") as seed_file:
        data = json.load(seed_file)

    for fonda in data.get("fondas", []):
        exists = conn.execute(
            "SELECT 1 FROM fondas WHERE nombre = ? AND status = 'approved' LIMIT 1",
            (fonda.get("nombre"),),
        ).fetchone()
        if exists:
            continue

        menu = fonda.get("menu")
        if isinstance(menu, list):
            menu = ", ".join(menu)

        conn.execute(
            '''
            INSERT INTO fondas (
                nombre, descripcion, barrio, lat, lng,
                precio_rango, precio_promedio, menu, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'approved')
            ''',
            (
                normalize_text(fonda.get("nombre")),
                normalize_text(fonda.get("descripcion", "")),
                normalize_text(fonda.get("barrio", "Desconocido")),
                fonda.get("lat"),
                fonda.get("lng"),
                fonda.get("precio_rango", "$"),
                fonda.get("precio_promedio"),
                normalize_text(menu),
            ),
        )

if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada.")
