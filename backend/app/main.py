from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings
from backend.app.api.v1.router import api_router

# Metadatos descriptivos para organizar las secciones en Swagger UI
tags_metadata = [
    {
        "name": "Delitos Sexuales Atlántico",
        "description": """
Servicios analíticos y de consulta para el conjunto histórico de **16,664 delitos sexuales** registrados en los 23 municipios del **Departamento del Atlántico (Colombia)** entre los años 2010 y 2026.
Incluye endpoints de paginación, filtros multidimensionales, agregaciones y exportación para Power BI.
"""
    },
    {
        "name": "Salud",
        "description": "Endpoints de monitoreo de disponibilidad y verificación de estado del servicio para Render y balanceadores de carga."
    }
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="""
# 🛡️ API REST: Minería de Datos de Delitos Sexuales en el Atlántico (2010–2026)

Bienvenido a la documentación oficial de la API REST para el análisis criminológico, predictivo y visual de los delitos sexuales en el Departamento del Atlántico.

---
### 📌 Información Institucional y de Auditoría
- **Entidad Proveedora:** Policía Nacional de Colombia — Portal Nacional de Datos Abiertos (`datos.gov.co`).
- **Fecha Oficial de Descarga:** **2026-11-06** (Inmutable).
- **Cobertura Territorial:** Departamento del Atlántico (23 municipios, incluyendo el Distrito de Barranquilla).
- **Volumen Procesado:** 405,193 registros a nivel nacional ➡️ **16,664 registros limpios para el Atlántico**.
- **Política Metodológica:** Cero eliminación de registros en Atlántico (100% preservados, 0 valores nulos finales).

---
### 🚀 Características de la API:
1. **Filtros Multidimensionales:** Filtre por fecha, año, mes, día, municipio, género, grupo etario, artículo penal, arma empleada o texto libre.
2. **Paginación Eficiente:** Soporta parámetros `skip` y `limit` (hasta 1.000 registros por llamada).
3. **Integración con Power BI:** Endpoint `/api/v1/delitos/powerbi/dataset` optimizado para consumo directo desde Power BI Desktop.
4. **Alta Disponibilidad:** Operación con PostgreSQL (Supabase) con fallback automático al CSV limpio en memoria en caso de desconexión.
5. **CORS Habilitado:** Acceso universal para clientes web (React, Vue, Streamlit, Power BI).
""",
    openapi_tags=tags_metadata,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración de CORS universal
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get(
    "/health",
    tags=["Salud"],
    summary="Verificar disponibilidad del servicio (Health Check)",
    description="Retorna el estado operativo de la API, versión activa, entorno y fecha de corte del dataset."
)
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "fecha_descarga_dataset": settings.FECHA_DESCARGA_DATASET
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
