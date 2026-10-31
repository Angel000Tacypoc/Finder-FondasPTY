# Roadmap

## Fase 0 - Fundacion, dias 1-2
- Confirmar barrios iniciales y criterios de precio.
- Cargar 20-50 locales reales con fuente y fecha de verificacion.
- Ejecutar FastAPI y validar busqueda desde la extension.
- Definir metricas y formulario corto de feedback.

## MVP - Dias 3-10
- Busqueda y filtros por texto, barrio y precio.
- Lista de resultados con menu y ubicacion.
- Leaflet con marcadores, solo despues de validar la lista.
- Formulario de propuesta de local.
- Cola manual de moderacion.
- Reporte de local cerrado o dato incorrecto.
- Migracion opcional del JSON a Supabase al final de la fase.

## v2 - Semanas 3-6
- Supabase Auth y perfiles.
- Roles y politicas RLS.
- Reclamo de propiedad por parte de duenos.
- Fotos y menus en Supabase Storage.
- Historial de cambios y reputacion basica de reportes.
- Busqueda por distancia usando coordenadas.

## v3 - Despues de validar uso
- PWA responsive y notificaciones.
- Recomendaciones personalizadas con reglas simples.
- IA opcional con Ollama o Gemini, siempre como ayuda y no como fuente de verdad.
- Analitica de horarios y popularidad.
- Moderacion asistida y deteccion de duplicados.

## Orden de recorte si falta tiempo
1. Mantener busqueda y precio.
2. Mantener moderacion manual.
3. Posponer auth, fotos y mapa.
4. Posponer IA hasta tener suficiente contenido y feedback.
