# FondaFinder PA - Product Requirements Document

## 1. Resumen
FondaFinder PA es un directorio comunitario de fondas, carritos y lugares economicos para comer en Panama. El producto prioriza precio real, tipo de comida, ubicacion y confiabilidad de los datos.

## 2. Problema
Google Maps mezcla restaurantes de todos los segmentos, no permite filtrar bien por precio economico y no muestra con claridad si un local cerro, cambio de menu o cambio de precios.

## 3. Objetivo del MVP
Permitir que una persona encuentre una fonda cercana o por texto en menos de 30 segundos, con precio, barrio, menu y estado visible. El MVP debe validarse con datos de una ciudad o pocos barrios antes de agregar cuentas y mapas complejos.

## 4. Usuarios
- Visitante: busca y filtra fondas sin registrarse.
- Usuario registrado: reporta cambios y aporta resenas o fotos.
- Dueno: solicita registrar o reclamar un local.
- Moderador: revisa altas y reportes.
- Admin: gestiona usuarios, roles, catalogo y configuracion.

## 5. Alcance MVP, menor a dos semanas
### Incluido
- Catalogo de fondas con nombre, descripcion, barrio, coordenadas, menu y precio.
- Busqueda por nombre, descripcion, barrio y menu.
- Filtro por barrio y rango de precio.
- Estado activo/inactivo visible en datos internos.
- API FastAPI y popup web funcional para validar la idea.
- Carga inicial desde `fondas.json`.
- Flujo manual de moderacion documentado.

### Fuera del MVP
- Pagos, delivery y chat.
- Recomendaciones de IA.
- Subida de imagenes a almacenamiento externo.
- Geolocalizacion en tiempo real.
- Aplicacion movil nativa.
- Login completo y panel administrativo automatico.

## 6. Requisitos funcionales
1. El visitante puede buscar por texto.
2. El visitante puede filtrar por barrio y precio: `$`, `$$` o `$$$`.
3. Cada resultado muestra nombre, descripcion, barrio, precio promedio y menu.
4. Un registro nuevo inicia como `pending` y no se publica hasta ser aprobado.
5. Un reporte de cambio guarda motivo, descripcion y fecha.
6. Un moderador puede aprobar, rechazar o pedir cambios.
7. Los registros inactivos no aparecen en la busqueda publica.

## 7. Requisitos no funcionales
- API documentada automaticamente por FastAPI en `/docs`.
- Consultas publicas de lectura sin autenticacion en el MVP.
- Validacion de entradas y limites de longitud.
- No guardar secretos en el repositorio.
- Responder busquedas normales en menos de 500 ms con hasta 10.000 registros.

## 8. Metricas
- Tiempo hasta primer resultado.
- Porcentaje de busquedas con al menos un resultado.
- Registros aprobados frente a enviados.
- Reportes resueltos en menos de 72 horas.
- Porcentaje de locales verificados en los ultimos 90 dias.

## 9. Riesgos y mitigaciones
- Datos falsos: moderacion, historial y limite de reportes.
- Locales cerrados: fecha de ultima verificacion y reportes comunitarios.
- Alcance excesivo: comenzar con catalogo y busqueda, no con red social.
- Costos de mapas: usar Leaflet + OpenStreetMap primero.

## 10. Criterios de exito del MVP
Una persona puede instalar/iniciar el proyecto, abrir la interfaz, buscar `pollo`, encontrar resultados del JSON y recibir un mensaje claro cuando el backend no esta disponible. El equipo puede revisar una propuesta antes de publicarla.
