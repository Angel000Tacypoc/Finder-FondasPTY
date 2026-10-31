# Pantallas iniciales del MVP

## 1. Busqueda publica
- Campo: `Que quieres comer?`
- Select de barrio.
- Select de precio: `$`, `$$`, `$$$`.
- Boton buscar.
- Lista de resultados con nombre, descripcion, precio, menu y estado de verificacion.
- Estado vacio y estado de backend desconectado.

## 2. Detalle de fonda
- Nombre y descripcion.
- Precio promedio y rango.
- Barrio y mapa Leaflet.
- Menu.
- Fecha de ultima verificacion.
- Boton `Reportar un cambio`.

## 3. Proponer una fonda
- Nombre, descripcion, barrio, coordenadas.
- Rango y precio promedio.
- Menu y contacto opcional.
- Evidencia opcional.
- Confirmacion: `Tu propuesta sera revisada antes de publicarse`.

## 4. Moderacion
- Tabs: pendientes, reportes abiertos, historial.
- Filtros por fecha y barrio.
- Vista de datos enviados.
- Acciones: aprobar, rechazar, solicitar cambios.
- Campo obligatorio de nota al rechazar.

## Prioridad de construccion
Primero pantalla 1, luego detalle, despues propuesta y finalmente moderacion. La pantalla publica debe funcionar con datos locales incluso antes de incorporar autenticacion.
