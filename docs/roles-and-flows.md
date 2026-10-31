# Roles y flujos

## Roles
| Rol | Puede hacer |
|---|---|
| Visitante | Buscar, filtrar y ver locales publicados |
| Usuario | Todo lo anterior, reportar cambios y enviar propuestas |
| Dueno | Reclamar un local, editar datos y subir menu/fotos para revision |
| Moderador | Revisar propuestas, reportes y aprobar o rechazar cambios |
| Admin | Gestionar roles, moderadores, catalogo y configuracion |

## Alta de una fonda
1. Usuario o dueno completa nombre, barrio, ubicacion, precio y menu.
2. El registro queda `pending`.
3. Moderador revisa duplicados, datos y evidencia.
4. Se aprueba como `published`, se rechaza o se solicitan cambios.
5. Solo `published` aparece en busquedas publicas.

## Reporte comunitario
1. Usuario abre un local y selecciona `cerrado`, `precio cambio`, `menu cambio` o `dato incorrecto`.
2. El reporte queda `open` y conserva autor, motivo y fecha.
3. Moderador contrasta la informacion.
4. Se actualiza el local y se marca `resolved`, o se descarta como `dismissed`.
5. Las acciones quedan en un historial auditable.

## Regla de permisos
El cliente nunca decide si un registro esta publicado. El backend debe validar el rol y el estado en cada operacion de escritura.
