# 🚀 Guía de Arranque de Servicios (Startup Guide)

> **Proyecto:** Minería de Delitos Sexuales en el Atlántico (2010–2026)  
> **Puertos de Red:**  
> - **Backend FastAPI (Swagger UI):** `http://localhost:8000` (Docs: `http://localhost:8000/docs`)  
> - **Analytics Streamlit (Dashboard EDA):** `http://localhost:8501`  
> - **Base de Datos Cloud:** PostgreSQL 17 en **Supabase** (`aws-0-us-east-2.pooler.supabase.com:6543`)  
> - **Estructura de Datos:** Sin columna sintética `id` (100% fiel a las 19 dimensiones limpias del dataset)  

---

## ⚡ 1. Arranque con Un Solo Comando (Recomendado)

Puede iniciar **todos los servicios simultáneamente** (Backend FastAPI en `:8000`, Streamlit EDA en `:8501`, y Frontend Web en `:3000`) con una sola línea o haciendo doble clic:

### Opción A: Doble clic en Windows o ejecutar en CMD
```cmd
run_dev.bat
```

### Opción B: Ejecutar en PowerShell
```powershell
.\run_dev.ps1
```
*Este comando abre tres consolas independientes debidamente tituladas y redirige automáticamente su navegador a `http://localhost:3000`.*

---

## 🖥️ 2. Comandos de Arranque Manual (Consolas Separadas)

### Terminal 1: Backend FastAPI (API REST & Swagger)
```powershell
# Ubicarse en la raíz del proyecto
cd e:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional

# Iniciar servidor Uvicorn en el puerto 8000 con recarga automática
.\backend\.venv\Scripts\uvicorn.exe backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```
- **Swagger UI Interactivo:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc (Especificación OpenAPI):** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Endpoint para Power BI Desktop:** [http://localhost:8000/api/v1/delitos/powerbi/dataset](http://localhost:8000/api/v1/delitos/powerbi/dataset)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

### Terminal 2: Analytics Streamlit (Dashboard EDA)
```powershell
# Ubicarse en la raíz del proyecto
cd e:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional

# Iniciar servidor interactivo de Streamlit en el puerto 8501
.\backend\.venv\Scripts\streamlit.exe run analytics/app.py --server.port 8501
```
- **Dashboard EDA en el Navegador:** [http://localhost:8501](http://localhost:8501)

---

## 🗄️ 2. Scripts de Base de Datos y Pipeline ETL

Si requiere recrear la base de datos, validar la conexión o recargar los registros limpios en Supabase:

### A. Probar Conexión con Supabase
Valida que la cadena de conexión del pooler y las credenciales funcionen correctamente:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/test_db_connection.py
```
*Salida esperada: `[SUCCESS] DATABASE_URL conectó correctamente! Total registros: 16664`*

### B. Ejecutar Script DDL (Crear Tablas, Índices y Vistas en Supabase)
Ejecuta `docs/database/supabase_ddl.sql` directamente contra la base de datos de Supabase:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/execute_ddl.py
```
*Crea la tabla `delitos_sexuales_atlantico`, los 8 índices B-Tree y las vistas `vista_resumen_anual_municipio` y `vista_perfil_demografico_anual`.*

### C. Habilitar y Configurar Row Level Security (RLS)
Aplica seguridad a nivel de filas y políticas de acceso para Supabase:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/enable_rls.py
```
*Habilita RLS en la tabla, permitiendo lectura pública a `anon`, `authenticated` y `postgres`, y restringiendo escritura a `service_role`.*

### C. Ejecutar Pipeline ETL de Limpieza de Datos
Procesa el dataset crudo nacional (405,193 filas) y genera el CSV limpio del Atlántico con 16,664 registros:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/clean_and_filter_atlantico.py
```
*Genera: `docs/data_set/delitos_sexuales_atlantico_limpio.csv` (0 pérdidas, 0 nulos).*

### D. Cargar Datos en Lotes a Supabase
Inserta los 16,664 registros limpios por lotes de 2,000 filas:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/upload_to_supabase.py
```

---

## 🧪 3. Script de Pruebas Automatizadas de la API
Para verificar que los 9 endpoints de FastAPI respondan código HTTP 200 con tipos y filtros válidos:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/test_api_endpoints.py
```

---

## ☁️ 4. Despliegue en la Nube (Render)
Para desplegar el backend en **Render**:
1. Conecte su repositorio GitHub a [Render](https://dashboard.render.com).
2. Render detectará automáticamente el archivo `render.yaml`.
3. Configure la variable de entorno `DATABASE_URL` en el dashboard de Render con la cadena del pooler de Supabase:
   ```
   postgresql+psycopg2://postgres.cqmofowalebzthxjhfes:[PASSWORD]@aws-0-us-east-2.pooler.supabase.com:6543/postgres
   ```
4. El servicio quedará disponible públicamente en:
   `https://api-delitos-sexuales-atlantico.onrender.com/docs`
