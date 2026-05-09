# ⚡ Especialización en FastAPI

FastAPI es un framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.7+ basado en las sugerencias de tipo estándar de Python.

## 🎯 Conceptos Clave
1. **Tipado de Datos (Pydantic)**: Validación automática de datos usando clases.
2. **Operaciones de Ruta**: `GET`, `POST`, `PUT`, `DELETE`.
3. **Documentación Automática**: Explora `/docs` (Swagger UI) y `/redoc`.
4. **Asincronismo (`async` / `await`)**: Cómo manejar múltiples peticiones concurrentes.
5. **Inyección de Dependencias**: Un sistema potente para compartir lógica entre rutas.

## 🚀 Tu Primer Desafío
Crea una API con FastAPI que:
- Tenga un endpoint `GET /items/` que devuelva una lista de objetos.
- Tenga un endpoint `POST /items/` que reciba un JSON con `nombre` y `precio`, y lo valide usando Pydantic.
- Prueba tu API usando la documentación automática en el navegador.

## 📚 Recursos
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://pydantic-docs.helpmanual.io/)
