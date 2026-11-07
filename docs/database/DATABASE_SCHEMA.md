# 🗄️ Diccionario y Diseño de Base de Datos (PostgreSQL en Supabase / Neon)

> **Asignatura:** Minería de Datos  
> **Motor:** PostgreSQL 15+ (Alojado en Supabase / Neon)  
> **Script DDL:** `docs/database/supabase_ddl.sql`  

---

## 🎯 Justificación del Diseño y Buenas Prácticas

En cumplimiento de las normas de diseño para analítica y el skill `database-architect`:
1. **Tipado Estricto y Eficiente:** Se emplean tipos `SMALLINT` para año (2010-2026), mes (1-12), día (1-31), trimestre (1-4) y semestre (1-2), ahorrando 75% de almacenamiento respecto a `INTEGER` ordinario.
2. **Dimensiones Temporales Precalculadas:** Para evitar cálculos pesados en tiempo real dentro de Power BI o FastAPI, las columnas temporales (`nombre_mes`, `dia_semana`, `anio`) ya están materializadas.
3. **Indexación Estratégica:** Índices compuestos `(anio, municipio)` y `(genero, grupo_etario)` optimizan los filtros combinados más recurrentes en dashboards.
4. **Auditoría Exigida:** Se garantiza la presencia fija de la columna `fecha_descarga_dataset = '2026-11-06'` y `origen_datos`.

---

## 📋 Estructura de la Tabla `delitos_sexuales_atlantico`

| Columna | Tipo SQL | Nulo | Por Defecto | Descripción |
|---|---|---|---|---|
| `id` | `BIGSERIAL` | NO | Autoincremental | Identificador único de registro |
| `departamento` | `VARCHAR(50)` | NO | `'ATLÁNTICO'` | Departamento de ocurrencia |
| `municipio` | `VARCHAR(100)` | NO | - | Municipio normalizado (sin sufijos '(CT)') |
| `codigo_dane` | `VARCHAR(20)` | NO | - | Código DANE municipal (8 dígitos) |
| `armas_medios` | `VARCHAR(100)` | NO | `'NO REPORTADO'` | Arma o medio utilizado |
| `fecha_hecho` | `DATE` | NO | - | Fecha de ocurrencia en formato `YYYY-MM-DD` |
| `anio` | `SMALLINT` | NO | - | Año (2010 a 2026) |
| `mes` | `SMALLINT` | NO | - | Mes numérico (1 a 12) |
| `nombre_mes` | `VARCHAR(20)` | NO | - | Nombre en español ('Enero' a 'Diciembre') |
| `dia` | `SMALLINT` | NO | - | Día del mes (1 a 31) |
| `dia_semana` | `VARCHAR(20)` | NO | - | Día de la semana ('Lunes' a 'Domingo') |
| `trimestre` | `SMALLINT` | NO | - | Trimestre calendario (1 a 4) |
| `semestre` | `SMALLINT` | NO | - | Semestre calendario (1 a 2) |
| `genero` | `VARCHAR(30)` | NO | `'NO REPORTADO'` | Género (FEMENINO, MASCULINO, NO REPORTADO) |
| `grupo_etario` | `VARCHAR(30)` | NO | `'NO REPORTADO'` | Grupo etario (ADULTOS, MENORES, ADOLESCENTES, NO REPORTADO) |
| `cantidad` | `INTEGER` | NO | `1` | Cantidad de hechos / víctimas reportadas |
| `codigo_articulo` | `VARCHAR(30)` | NO | - | Artículo penal extraído (ej. 'ARTÍCULO 209') |
| `delito` | `TEXT` | NO | - | Descripción completa y limpia del delito |
| `fecha_descarga_dataset` | `DATE` | NO | `'2026-11-06'` | Fecha inmutable de extracción |
| `origen_datos` | `VARCHAR(150)` | NO | `'Policía Nacional...'`| Entidad oficial proveedora |
| `creado_en` | `TIMESTAMPTZ` | NO | `NOW()` | Fecha y hora de carga a la base de datos |

---

## 🔒 Seguridad y Row Level Security (RLS)

Siguiendo las directrices del skill `supabase-postgres-best-practices`, la tabla principal tiene activado **Row Level Security**:
- **Comando:** `ALTER TABLE delitos_sexuales_atlantico ENABLE ROW LEVEL SECURITY;`
- **Política 1 (`SELECT`):** `"Permitir lectura publica de delitos sexuales"` asignada a los roles `anon`, `authenticated` y `postgres` con `USING (true)`. Permite a Power BI, clientes externos y la API de Supabase leer sin trabas los datos abiertos.
- **Política 2 (`ALL`):** `"Restringir escritura a service_role y postgres"` asignada a `service_role` y `postgres` con `USING (true) WITH CHECK (true)`. Protege el dataset contra modificaciones, eliminaciones o inserciones no autorizadas por parte de usuarios anónimos o no autenticados.

---

## ⚡ Conexión desde Power BI

Para conectar Power BI:
- **Opción A (Recomendada si el Backend está en Render):** Conectar vía conector Web de Power BI a `https://tu-backend.onrender.com/api/v1/delitos/powerbi/dataset`.
- **Opción B (Conexión Directa a BD):** Conectar con el conector nativo de PostgreSQL de Power BI a la cadena directa de Supabase o Neon (puerto 5432 o Session Pooler).

