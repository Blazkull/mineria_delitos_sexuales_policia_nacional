# 📡 Catálogo Maestro de Endpoints de la API REST (FastAPI)

> **Servicio:** Backend API REST — Delitos Sexuales en Atlántico (2010–2026)  
> **Plataforma de Despliegue:** Render Cloud (`https://api-delitos-sexuales-atlantico.onrender.com`)  
> **Entorno Local:** `http://localhost:8000`  
> **Documentación Interactiva Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)  
> **Especificación OpenAPI (ReDoc):** [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---

## 1. Resumen de Endpoints Disponibles en Swagger

| Método | Endpoint | Resumen Swagger | Parámetros Principales |
|---|---|---|---|
| `GET` | `/health` | Verificar disponibilidad del servicio (Health Check) | Ninguno |
| `GET` | `/api/v1/delitos` | Listado general paginado con filtros multidimensionales | `skip`, `limit`, `fecha_desde`, `fecha_hasta`, `anio`, `municipio`, `genero`, `grupo_etario`, `codigo_articulo`, etc. |
| `GET` | `/api/v1/delitos/filtros/opciones` | Catálogo de opciones únicas para poblar selectores | Ninguno |
| `GET` | `/api/v1/delitos/powerbi/dataset` | Dataset completo optimizado para Power BI Desktop | Ninguno (Dataset completo plano) |
| `GET` | `/api/v1/delitos/metricas/anual` | Serie temporal cronológica anual (2010 a 2026) | Ninguno |
| `GET` | `/api/v1/delitos/metricas/municipios` | Ranking de criticidad y concentración por municipio | `top` (1 a 25) |
| `GET` | `/api/v1/delitos/metricas/genero` | Distribución porcentual por género de la víctima | Ninguno |
| `GET` | `/api/v1/delitos/metricas/grupo-etario` | Distribución y vulnerabilidad por grupo etario | Ninguno |
| `GET` | `/api/v1/delitos/metricas/articulos` | Frecuencia por artículo del Código Penal | `top` (1 a 30) |

---

## 2. Detalle de Endpoints y Ejemplos Prácticos en Swagger

---

### 2.1. `GET /api/v1/delitos`
**Propósito:** Consulta y filtrado granular de los 16,664 registros de delitos sexuales con paginación y ordenamiento.

#### Parámetros con Ejemplos en Swagger:
- `skip` (`int`, ej. `0`): Cantidad de registros a omitir para paginar.
- `limit` (`int`, ej. `50`): Registros por página (máx 1.000).
- `fecha_desde` (`date`, ej. `2020-01-01`): Inicio del rango.
- `fecha_hasta` (`date`, ej. `2024-12-31`): Fin del rango.
- `anio` (`int`, ej. `2023`): Año exacto.
- `anio_desde` (`int`, ej. `2018`): Límite inferior de año.
- `anio_hasta` (`int`, ej. `2024`): Límite superior de año.
- `mes` (`int`, ej. `5`): Mes numérico (Mayo).
- `dia_semana` (`str`, ej. `Lunes`): Día en español.
- `municipio` (`str`, ej. `Barranquilla`): Municipio oficial.
- `codigo_dane` (`str`, ej. `08001000`): Código DANE de 8 dígitos.
- `genero` (`str`, ej. `FEMENINO`): `FEMENINO`, `MASCULINO`, `NO REPORTADO`.
- `grupo_etario` (`str`, ej. `MENORES`): `MENORES`, `ADOLESCENTES`, `ADULTOS`, `NO REPORTADO`.
- `codigo_articulo` (`str`, ej. `ARTÍCULO 209`): Artículo penal.
- `delito_buscar` (`str`, ej. `menor de 14`): Búsqueda textual.
- `ordenar_por` (`str`, ej. `fecha_hecho`): Columna de orden.
- `orden_dir` (`str`, ej. `desc`): Dirección de orden (`asc` o `desc`).

#### Ejemplo de Respuesta JSON:
```json
{
  "total": 181,
  "limit": 2,
  "offset": 0,
  "fuente": "PostgreSQL (Supabase)",
  "data": [
    {
      "id": 12,
      "departamento": "ATLÁNTICO",
      "municipio": "Soledad",
      "codigo_dane": "08758000",
      "armas_medios": "NO REPORTADO",
      "fecha_hecho": "2024-03-12",
      "anio": 2024,
      "mes": 3,
      "nombre_mes": "Marzo",
      "dia": 12,
      "dia_semana": "Martes",
      "trimestre": 1,
      "semestre": 1,
      "genero": "FEMENINO",
      "grupo_etario": "ADULTOS",
      "cantidad": 1,
      "codigo_articulo": "ARTÍCULO 206",
      "delito": "ARTÍCULO 206. ACTO SEXUAL VIOLENTO",
      "fecha_descarga_dataset": "2026-11-06",
      "origen_datos": "Policía Nacional de Colombia - Datos Abiertos"
    }
  ]
}
```

---

### 2.2. `GET /api/v1/delitos/filtros/opciones`
**Propósito:** Retorna todos los valores únicos para poblar dinámicamente controles desplegables (`<select>`, `Dropdown`) en interfaces de usuario.

#### Ejemplo de Respuesta JSON:
```json
{
  "total_registros": 16664,
  "anios_disponibles": [2010, 2011, 2012, 2024, 2025, 2026],
  "meses_disponibles": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
  "dias_semana": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
  "municipios": ["Baranoa", "Barranquilla", "Galapa", "Malambo", "Puerto Colombia", "Soledad"],
  "generos": ["FEMENINO", "MASCULINO", "NO REPORTADO"],
  "grupos_etarios": ["ADOLESCENTES", "ADULTOS", "MENORES", "NO REPORTADO"],
  "codigos_articulo": ["ARTÍCULO 205", "ARTÍCULO 206", "ARTÍCULO 209", "ARTÍCULO 210"],
  "armas_medios": ["ARMA BLANCA / CORTOPUNZANTE", "ARMA DE FUEGO", "CONTUNDENTE", "NO REPORTADO"],
  "fecha_minima": "2010-01-01",
  "fecha_maxima": "2026-10-31",
  "fecha_descarga_dataset": "2026-11-06"
}
```

---

### 2.3. `GET /api/v1/delitos/powerbi/dataset`
**Propósito:** Provee el conjunto completo de **16,664 registros** en JSON plano para que Power BI Desktop los absorba directamente en su motor en memoria **VertiPaq**.

#### Ejemplo de Invocación en Power Query:
```powerquery
let
    Origen = Json.Document(Web.Contents("https://api-delitos-sexuales-atlantico.onrender.com/api/v1/delitos/powerbi/dataset")),
    Tabla = Table.FromList(Origen, Splitter.SplitByNothing(), null, null, ExtraValues.Error)
in
    Tabla
```

---

### 2.4. `GET /api/v1/delitos/metricas/anual`
**Propósito:** Agrupa casos y víctimas por año (2010–2026).

#### Ejemplo de Respuesta JSON:
```json
[
  { "anio": 2023, "total_casos": 1245, "total_victimas": 1250 },
  { "anio": 2024, "total_casos": 1180, "total_victimas": 1185 }
]
```

---

### 2.5. `GET /api/v1/delitos/metricas/municipios?top=5`
**Propósito:** Obtener el ranking de municipios más afectados.

#### Ejemplo de Respuesta JSON:
```json
[
  { "municipio": "Barranquilla", "total_casos": 8778, "porcentaje": 52.68 },
  { "municipio": "Soledad", "total_casos": 3613, "porcentaje": 21.68 },
  { "municipio": "Sabanalarga", "total_casos": 869, "porcentaje": 5.21 },
  { "municipio": "Malambo", "total_casos": 854, "porcentaje": 5.13 },
  { "municipio": "Baranoa", "total_casos": 393, "porcentaje": 2.36 }
]
```

---

### 2.6. `GET /api/v1/delitos/metricas/genero`
**Propósito:** Proporción de víctimas por género.

#### Ejemplo de Respuesta JSON:
```json
[
  { "genero": "FEMENINO", "total_casos": 14184, "porcentaje": 85.12 },
  { "genero": "MASCULINO", "total_casos": 2355, "porcentaje": 14.13 },
  { "genero": "NO REPORTADO", "total_casos": 125, "porcentaje": 0.75 }
]
```

---

### 2.7. `GET /api/v1/delitos/metricas/grupo-etario`
**Propósito:** Proporción de víctimas por grupo etario.

#### Ejemplo de Respuesta JSON:
```json
[
  { "grupo_etario": "ADULTOS", "total_casos": 11151, "porcentaje": 66.92 },
  { "grupo_etario": "MENORES", "total_casos": 3026, "porcentaje": 18.16 },
  { "grupo_etario": "ADOLESCENTES", "total_casos": 2461, "porcentaje": 14.77 },
  { "grupo_etario": "NO REPORTADO", "total_casos": 26, "porcentaje": 0.16 }
]
```

---

### 2.8. `GET /api/v1/delitos/metricas/articulos?top=3`
**Propósito:** Conteo de transgresiones por artículo penal.

#### Ejemplo de Respuesta JSON:
```json
[
  { "codigo_articulo": "ARTÍCULO 209", "total_casos": 6840 },
  { "codigo_articulo": "ARTÍCULO 205", "total_casos": 4120 },
  { "codigo_articulo": "ARTÍCULO 206", "total_casos": 2315 }
]
```

---

### 2.9. `GET /health`
**Propósito:** Health check para monitores de nube (Render, UptimeRobot).

#### Ejemplo de Respuesta JSON:
```json
{
  "status": "healthy",
  "service": "Minería de Delitos Sexuales - Policía Nacional (Atlántico)",
  "version": "1.0.0",
  "environment": "development",
  "fecha_descarga_dataset": "2026-11-06"
}
```
