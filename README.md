# FondaFinder PA

MVP de un directorio comunitario de fondas y comida economica en Panama.

## Ejecutar el backend

Requiere Python 3.10 o superior.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Verifica la API en:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## Ejecutar la extension

1. Abre `chrome://extensions`.
2. Activa Developer mode.
3. Selecciona Load unpacked.
4. Elige esta carpeta del proyecto.
5. Abre FondaFinder PA desde la barra de extensiones.
6. Manten el backend ejecutandose en el puerto 8000.

## Prueba rapida de API

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod 'http://127.0.0.1:8000/fondas?q=pollo'
```

Al iniciar, la aplicacion carga automaticamente las fondas iniciales de `fondas.json` como aprobadas. Durante la demo, los registros enviados desde la extension tambien se aprueban automaticamente para que aparezcan de inmediato en las busquedas. El diseno para migrar a PostgreSQL/Supabase esta en `docs/schema.sql`.

## Documentacion de producto

- `docs/PRD.md`: requisitos, alcance y metricas.
- `docs/schema.sql`: esquema de PostgreSQL.
- `docs/roles-and-flows.md`: permisos y moderacion.
- `docs/roadmap.md`: plan MVP, v2 y v3.
- `docs/mvp-screens.md`: pantallas iniciales.
