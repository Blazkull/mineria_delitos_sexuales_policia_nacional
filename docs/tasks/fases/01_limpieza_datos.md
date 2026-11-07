# 🧹 Fase 1: Limpieza de Datos y Pipeline ETL

> **Estado:** COMPLETADO (100%)  
> **Fecha de ejecución:** 2026-11-06  
> **Script principal:** `backend/scripts/clean_and_filter_atlantico.py`  
> **Dataset resultante:** `docs/data_set/delitos_sexuales_atlantico_limpio.csv`  

---

## 📋 Lista de Tareas y Checklists

- [x] **1.1. Inspección Exploratoria del Dataset Original**
  - [x] Lectura de metadatos del archivo `Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv`.
  - [x] Identificación de volumen nacional (405,193 filas) y columnas originales.
  - [x] Detección de codificación y caracteres especiales (Mojibake tipográfico).

- [x] **1.2. Configuración del Entorno de Procesamiento**
  - [x] Creación de entorno virtual `backend/.venv` con Python 3.11.
  - [x] Instalación de librerías base: `pandas 3.1.1`, `numpy`, `python-dotenv`, `openpyxl`.

- [x] **1.3. Desarrollo del Script ETL (`clean_and_filter_atlantico.py`)**
  - [x] Filtrado exclusivo por el departamento del Atlántico (`DEPARTAMENTO == 'ATLÁNTICO'`).
  - [x] Verificación de la regla no negociable: Cero registros eliminados (exactamente 16,664 filas preservadas).
  - [x] Reparación de caracteres tipográficos Mojibake (`ARTÍCULO`, `AÑOS`, etc.).
  - [x] Normalización de municipios: Remoción de sufijos administrativos `(CT)`.
  - [x] Imputación controlada de valores nulos o vacíos en `GENERO` (113 casos) a `'NO REPORTADO'`.
  - [x] Imputación controlada de valores nulos en `GRUPO ETARIO` (26 casos) a `'NO REPORTADO'`.
  - [x] Estandarización de `ARMAS MEDIOS` y `CANTIDAD` (mínimo 1).
  - [x] Parseo de fechas `DD/MM/YYYY` a formato ISO `YYYY-MM-DD`.
  - [x] Enriquecimiento temporal analítico: `anio`, `mes`, `nombre_mes`, `dia`, `dia_semana`, `trimestre`, `semestre`.
  - [x] Incorporación de columnas fijas de auditoría: `fecha_descarga_dataset = '2026-11-06'` y `origen_datos`.

- [x] **1.4. Control de Calidad y Validación**
  - [x] Verificación de 0 nulos finales en todas las columnas.
  - [x] Validación de rango de años (2010 a 2026).
  - [x] Confirmación de 23 municipios únicos del Atlántico.
  - [x] Exportación exitosa a `docs/data_set/delitos_sexuales_atlantico_limpio.csv` (3.86 MB).

