from typing import Optional, List
from datetime import date
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.schemas.delito import (
    DelitoPaginationSchema,
    OpcionesFiltrosSchema,
    MetricaAnualSchema,
    MetricaMunicipioSchema,
    MetricaGeneroSchema,
    MetricaGrupoEtarioSchema,
    MetricaArticuloSchema,
    DelitoResponseSchema
)
from backend.app.services.delito_service import DelitoService

router = APIRouter(prefix="/delitos", tags=["Delitos Sexuales Atlántico"])

@router.get(
    "",
    response_model=DelitoPaginationSchema,
    summary="Listado general paginado con filtros multidimensionales",
    description="""
### 📋 Propósito del Endpoint
Permite consultar, filtrar y paginar el conjunto íntegro de **16,664 registros** de delitos sexuales en el Departamento del Atlántico (2010 a 2026).

---
### 🔍 Capacidades de Filtrado Soportadas:
1. **Paginación Eficiente:** Use `skip` (desplazamiento) y `limit` (tamaño de página, máx 1.000).
2. **Rango de Fechas Calendario:** `fecha_desde` y `fecha_hasta` en formato estándar `YYYY-MM-DD`.
3. **Periodos Cronológicos:** Filtrado por año exacto (`anio`), rango de años (`anio_desde`, `anio_hasta`), mes numérico (`mes` 1–12), día de la semana (`dia_semana`), trimestre (`trimestre` 1–4) o semestre (`semestre` 1–2).
4. **Territorio y Ubicación:** Filtrado por municipio (`municipio`) entre los 23 municipios oficiales del Atlántico o por código DANE (`codigo_dane`).
5. **Perfil Demográfico:** Filtrado por género (`genero`: `FEMENINO`, `MASCULINO`, `NO REPORTADO`) y grupo etario (`grupo_etario`: `MENORES`, `ADOLESCENTES`, `ADULTOS`, `NO REPORTADO`).
6. **Tipificación Penal:** Filtrado por artículo del Código Penal (`codigo_articulo`, ej. `ARTÍCULO 209`) o búsqueda textual en el nombre del delito (`delito_buscar`).
7. **Medios Empleados:** Filtrado por tipo de arma o medio (`armas_medios`, ej. `ARMA BLANCA`, `NO REPORTADO`).
8. **Ordenamiento:** Selección de columna (`ordenar_por`) y dirección (`orden_dir`: `asc` o `desc`).

---
### 💡 Ejemplos Prácticos de Consulta:
- **Casos en Soledad en 2024 de género femenino:**  
  `?municipio=Soledad&genero=FEMENINO&anio=2024&limit=10`
- **Delitos contra menores en Barranquilla entre 2020 y 2023:**  
  `?municipio=Barranquilla&grupo_etario=MENORES&anio_desde=2020&anio_hasta=2023`
- **Búsqueda del delito de Acoso Sexual en todo el Atlántico:**  
  `?delito_buscar=acoso`
""",
    response_description="Objeto JSON paginado con el total de coincidencias, metadatos y lista de registros"
)
def listar_delitos(
    skip: int = Query(0, ge=0, description="Cantidad de registros a omitir para paginar", examples=[0]),
    limit: int = Query(50, ge=1, le=1000, description="Cantidad máxima de registros a retornar por página", examples=[50]),
    fecha_desde: Optional[date] = Query(None, description="Fecha de inicio del rango (YYYY-MM-DD)", examples=["2020-01-01"]),
    fecha_hasta: Optional[date] = Query(None, description="Fecha final del rango (YYYY-MM-DD)", examples=["2024-12-31"]),
    anio: Optional[int] = Query(None, description="Año específico del hecho (2010 a 2026)", examples=[2023]),
    anio_desde: Optional[int] = Query(None, description="Límite inferior del año del hecho", examples=[2018]),
    anio_hasta: Optional[int] = Query(None, description="Límite superior del año del hecho", examples=[2024]),
    mes: Optional[int] = Query(None, ge=1, le=12, description="Mes del año (1: Enero, ..., 12: Diciembre)", examples=[5]),
    trimestre: Optional[int] = Query(None, ge=1, le=4, description="Trimestre del año (1 a 4)", examples=[2]),
    semestre: Optional[int] = Query(None, ge=1, le=2, description="Semestre del año (1 a 2)", examples=[1]),
    dia_semana: Optional[str] = Query(None, description="Día de la semana en español (Lunes, Martes, ..., Domingo)", examples=["Lunes"]),
    municipio: Optional[str] = Query(None, description="Nombre del municipio del Atlántico", examples=["Barranquilla"]),
    codigo_dane: Optional[str] = Query(None, description="Código DANE oficial de 8 dígitos", examples=["08001000"]),
    armas_medios: Optional[str] = Query(None, description="Arma o medio empleado", examples=["NO REPORTADO"]),
    genero: Optional[str] = Query(None, description="Género de la víctima: FEMENINO, MASCULINO, NO REPORTADO", examples=["FEMENINO"]),
    grupo_etario: Optional[str] = Query(None, description="Grupo etario de la víctima: ADULTOS, ADOLESCENTES, MENORES, NO REPORTADO", examples=["MENORES"]),
    codigo_articulo: Optional[str] = Query(None, description="Código del artículo penal (ej. ARTÍCULO 209, ARTÍCULO 205)", examples=["ARTÍCULO 209"]),
    delito_buscar: Optional[str] = Query(None, description="Palabra o fragmento para buscar en la descripción del delito", examples=["menor de 14"]),
    cantidad_min: Optional[int] = Query(None, ge=1, description="Cantidad mínima de víctimas registradas", examples=[1]),
    cantidad_max: Optional[int] = Query(None, ge=1, description="Cantidad máxima de víctimas registradas", examples=[5]),
    ordenar_por: str = Query("fecha_hecho", description="Columna para ordenar: fecha_hecho, anio, municipio, cantidad, codigo_articulo", examples=["fecha_hecho"]),
    orden_dir: str = Query("desc", description="Dirección del ordenamiento: 'asc' o 'desc'", examples=["desc"]),
    db: Session = Depends(get_db)
):
    return DelitoService.get_delitos(
        db=db,
        skip=skip,
        limit=limit,
        fecha_desde=fecha_desde,
        fecha_hasta=fecha_hasta,
        anio=anio,
        anio_desde=anio_desde,
        anio_hasta=anio_hasta,
        mes=mes,
        trimestre=trimestre,
        semestre=semestre,
        dia_semana=dia_semana,
        municipio=municipio,
        codigo_dane=codigo_dane,
        armas_medios=armas_medios,
        genero=genero,
        grupo_etario=grupo_etario,
        codigo_articulo=codigo_articulo,
        delito_buscar=delito_buscar,
        cantidad_min=cantidad_min,
        cantidad_max=cantidad_max,
        ordenar_por=ordenar_por,
        orden_dir=orden_dir
    )

@router.get(
    "/filtros/opciones",
    response_model=OpcionesFiltrosSchema,
    summary="Catálogo de opciones únicas para poblar selectores de interfaz",
    description="""
### 📋 Propósito del Endpoint
Retorna todos los valores discretos y rangos disponibles en el dataset procesado (23 municipios, géneros, grupos etarios, artículos penales, armas, años y fechas extremas).

---
### 💡 Caso de Uso:
Permite a interfaces de usuario (React, Vue, Streamlit) o herramientas de integración poblar menús desplegables (`<select>`, `Dropdown`) dinámicamente sin quemar listas estáticas en código.
""",
    response_description="Listados únicos de municipios, artículos, categorías demográficas y fechas mínimas y máximas"
)
def obtener_opciones_filtros(db: Session = Depends(get_db)):
    return DelitoService.get_opciones_filtros(db)

@router.get(
    "/powerbi/dataset",
    summary="Dataset completo optimizado para Power BI Desktop (Render / Web Connector)",
    description="""
### 📋 Propósito del Endpoint
Expone el conjunto completo de **16,664 registros** limpios en formato JSON plano sin paginación restrictiva para ser importado directamente en **Power BI Desktop**.

---
### 💡 Caso de Uso en Power BI:
1. En Power BI Desktop, seleccione **Obtener datos ➡️ Web**.
2. Pegue la URL del endpoint (en local o en Render):
   `https://api-delitos-sexuales-atlantico.onrender.com/api/v1/delitos/powerbi/dataset`
3. Power Query transforma automáticamente la lista de registros en la tabla dimensional `Fact_Delitos`.
""",
    response_description="Array JSON plano con los 16,664 registros procesados"
)
def obtener_dataset_powerbi(db: Session = Depends(get_db)):
    return DelitoService.get_powerbi_full_dataset(db)

@router.get(
    "/metricas/anual",
    response_model=List[MetricaAnualSchema],
    summary="Serie temporal cronológica anual (2010 a 2026)",
    description="""
### 📋 Propósito del Endpoint
Agrupa y contabiliza el total de casos y víctimas registrados por cada año del periodo 2010 a 2026.

---
### 💡 Caso de Uso:
Ideal para alimentar gráficos de líneas, series de tiempo o calcular tasas de variación interanual.
""",
    response_description="Lista de años con su respectivo conteo de casos y víctimas"
)
def obtener_metrica_anual(db: Session = Depends(get_db)):
    return DelitoService.get_resumen_anual(db)

@router.get(
    "/metricas/municipios",
    response_model=List[MetricaMunicipioSchema],
    summary="Ranking de criticidad y concentración por municipio",
    description="""
### 📋 Propósito del Endpoint
Retorna los municipios con mayor número de hechos registrados junto con su participación porcentual sobre el total departamental.

---
### 💡 Ejemplo de Resultado:
Barranquilla concentra el 52.68% de los casos (8.778 hechos), seguido de Soledad con el 21.68% (3.613 hechos).
""",
    response_description="Ranking de municipios con total de casos y porcentaje"
)
def obtener_metrica_municipios(
    top: int = Query(25, ge=1, le=25, description="Cantidad de municipios a retornar en el ranking", examples=[10]),
    db: Session = Depends(get_db)
):
    return DelitoService.get_resumen_municipios(db, limit=top)

@router.get(
    "/metricas/genero",
    response_model=List[MetricaGeneroSchema],
    summary="Distribución porcentual por género de la víctima",
    description="""
### 📋 Propósito del Endpoint
Calcula la proporción y total de hechos según el género reportado de la víctima (`FEMENINO`, `MASCULINO`, `NO REPORTADO`).

---
### 💡 Hallazgo Relevante:
El 85.12% de las víctimas en el Atlántico son de género femenino (14.184 casos).
""",
    response_description="Totales y porcentajes calculados por género"
)
def obtener_metrica_genero(db: Session = Depends(get_db)):
    return DelitoService.get_resumen_genero(db)

@router.get(
    "/metricas/grupo-etario",
    response_model=List[MetricaGrupoEtarioSchema],
    summary="Distribución y vulnerabilidad por grupo etario",
    description="""
### 📋 Propósito del Endpoint
Desglosa el volumen de victimización entre adultos, menores de 14 años y adolescentes.

---
### 💡 Hallazgo Relevante:
Uno de cada tres delitos sexuales en el Atlántico (32.93%) es cometido contra niños, niñas o adolescentes (5.487 casos en conjunto).
""",
    response_description="Totales y porcentajes calculados por grupo de edad"
)
def obtener_metrica_grupo_etario(db: Session = Depends(get_db)):
    return DelitoService.get_resumen_grupo_etario(db)

@router.get(
    "/metricas/articulos",
    response_model=List[MetricaArticuloSchema],
    summary="Frecuencia por artículo del Código Penal",
    description="""
### 📋 Propósito del Endpoint
Retorna la frecuencia de transgresión de los artículos del Código Penal colombiano (Ley 599 de 2000) en el Atlántico.

---
### 💡 Hallazgo Relevante:
El Artículo 209 (*Actos sexuales con menor de 14 años*) y el Artículo 205 (*Acceso carnal violento*) encabezan las denuncias judiciales en la región.
""",
    response_description="Listado de artículos con su frecuencia de ocurrencia"
)
def obtener_metrica_articulos(
    top: int = Query(15, ge=1, le=30, description="Cantidad de artículos a listar", examples=[10]),
    db: Session = Depends(get_db)
):
    return DelitoService.get_resumen_articulos(db, limit=top)
