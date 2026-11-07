# AGENTS.md — Contexto de IA para el Microservicio Backend & Procesamiento ETL

> Este archivo proporciona contexto específico para cualquier IA o agente que trabaje en el directorio `backend/`.
> El contexto global del sistema está en el archivo raíz: `../AGENTS.md`.

---

## 📌 Identidad de este Módulo

| Campo | Valor |
|---|---|
| **Nombre** | Backend — API REST & Pipeline ETL de Minería de Datos |
| **Framework API** | FastAPI 0.110+ (Python 3.11+) |
| **Herramientas ETL** | Pandas 2.2+, NumPy, Python-dotenv |
| **Base de Datos** | PostgreSQL (Supabase / Neon) vía SQLAlchemy & Psycopg2 |
| **Entorno Virtual** | `backend/.venv` (Obligatorio aislar dependencias aquí) |
| **Puerto por Defecto** | 8000 |

---

## 🏗️ Arquitectura Interna de `backend/`

```
backend/
├── .venv/                   → Entorno virtual Python 3.11 aislado
├── app/
│   ├── main.py              → Punto de entrada FastAPI, middlewares, CORS y routers
│   ├── core/
│   │   ├── config.py        → Configuración tipada con Pydantic Settings
│   │   └── database.py      → Motor SQLAlchemy y sesión de base de datos
│   ├── models/
│   │   └── delito.py        → Modelo ORM SQLAlchemy para delitos_sexuales_atlantico
│   ├── schemas/
│   │   └── delito.py        → Esquemas Pydantic v2 para validación y serialización
│   ├── services/
│   │   └── delito_service.py→ Lógica de consulta analítica, filtros y agregaciones
│   └── api/
│       └── v1/
│           ├── router.py    → Enrutador central v1
│           └── endpoints/   → Endpoints REST (/delitos, /metricas, /municipios)
├── scripts/
│   ├── clean_and_filter_atlantico.py → Script maestro ETL de limpieza y normalización
│   └── upload_to_supabase.py         → Ingestión batch masiva hacia PostgreSQL
├── requirements.txt         → Lista estricta de dependencias
├── .env.example             → Plantilla de variables de entorno
├── AGENTS.md                → Contexto para agentes en este módulo
└── README.md                → Manual de ejecución
```

---

## 🚨 Reglas Críticas para la IA en `backend/`

1. **Uso Exclusivo del Entorno Virtual:** Todo comando de ejecución o instalación debe usar `backend/.venv/Scripts/python.exe` (o activar `.venv`).
2. **Inmutabilidad del Dataset Original:** El script ETL lee `docs/data_set/Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv` en modo lectura y exporta a `docs/data_set/delitos_sexuales_atlantico_limpio.csv`. NUNCA modificar el archivo crudo.
3. **Cero Eliminación de Líneas en Atlántico:** En el departamento del Atlántico hay exactamente **16,664 registros**. No descartar filas por tener datos faltantes; imputar `NO REPORTADO` según la metodología científica.
4. **Validación Pydantic v2:** Usar `model_validator(mode='before')` o `field_validator`, nunca sintaxis obsoleta de Pydantic v1.
5. **Auditoría de Ingestión:** Asegurar que cada registro incluya `fecha_descarga_dataset = '2026-11-06'`.
6. **Endpoints Optimizados:** Los endpoints que sirvan a Power BI o a clientes externos deben admitir paginación y agregaciones precalculadas (GROUP BY por año, municipio, género, delito).

