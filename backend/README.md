# ⚙️ Backend & ETL — Minería de Datos de Delitos Sexuales

Módulo de backend y procesamiento de datos para la extracción, limpieza, normalización, carga (ETL) y exposición de servicios REST sobre el dataset de delitos sexuales de la Policía Nacional para el Departamento del Atlántico.

---

## 🚀 Requisitos y Configuración

### 1. Activar Entorno Virtual
```powershell
# En Windows PowerShell
.\backend\.venv\Scripts\Activate.ps1
```

### 2. Instalar Dependencias (si no están instaladas)
```powershell
.\backend\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
```

### 3. Configurar Variables de Entorno
Copie el archivo de ejemplo y configure su conexión a Supabase / Neon:
```powershell
cp backend/.env.example backend/.env
```

---

## 🧹 Ejecución del Pipeline de Limpieza ETL

Para ejecutar el pipeline de filtrado regional por Atlántico, imputación de nulos y enriquecimiento temporal:
```powershell
.\backend\.venv\Scripts\python.exe backend/scripts/clean_and_filter_atlantico.py
```

**Resultado esperado:**
- Lectura de 405,193 registros a nivel nacional.
- Filtrado exacto de **16,664 registros** correspondientes al Atlántico.
- Imputación de campos nulos (`GENERO`, `GRUPO ETARIO`).
- Creación de columnas temporales (`anio`, `mes`, `nombre_mes`, `dia_semana`, `trimestre`).
- Exportación del archivo limpio a `docs/data_set/delitos_sexuales_atlantico_limpio.csv`.

---

## 📡 Ejecución de la API REST (FastAPI)

Para iniciar el servidor de desarrollo:
```powershell
cd backend
..\backend\.venv\Scripts\uvicorn.exe app.main:app --reload --port 8000
```
- **Documentación Interactiva (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Especificación OpenAPI (ReDoc):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

