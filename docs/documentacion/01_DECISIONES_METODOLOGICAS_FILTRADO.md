# 📋 Documento Metodológico: Decisiones de Filtrado, Limpieza y Normalización

> **Proyecto:** Minería de Delitos Sexuales en el Atlántico (2010–2026)  
> **Fuente Original:** Policía Nacional de Colombia — Portal de Datos Abiertos (`datos.gov.co`)  
> **Fecha de Descarga Oficial:** 2026-11-06  
> **Archivo Fuente Crudo:** `docs/data_set/Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv` (405,193 registros)  
> **Archivo Limpio Generado:** `docs/data_set/delitos_sexuales_atlantico_limpio.csv` (16,664 registros)  

---

## 1. Justificación de la Política No Negociable: "Cero Eliminación de Registros"

En el análisis criminológico y judicial de delitos contra la integridad sexual, la eliminación de registros por incompletitud introduce sesgos muestrales severos conocidos en la literatura científica como **sesgo de supervivencia de datos** (*survivorship bias*) o **subestimación de la cifra oculta** (*dark figure of crime*).

- **Población Total en Atlántico:** 16,664 registros.
- **Registros Eliminados:** **0 (CERO)**.
- **Tasa de Retención de Registros:** **100.0%**.

Cualquier registro faltante en género (113 filas) o en grupo etario (26 filas) representa un hecho punible formalmente denunciado ante la autoridad policial. Descartar estas filas distorsionaría el total absoluto de víctimas y la severidad penal en los municipios afectados.

---

## 2. Tratamiento Riguroso de Valores Nulos y Vacíos

En lugar de eliminar registros o utilizar métodos de imputación probabilística sintética (como la moda o KNN, que inventarían el sexo biológico o la edad de una víctima real sin sustento fáctico), se adoptó la **imputación explícita por categoría nula informada**:

| Variable Original | Registros Vacíos / Nulos | Técnica Aplicada | Valor Imputado Final | Justificación Metodológica |
|---|---|---|---|---|
| `GENERO` | 113 filas vacías + 'NO REPORTA' | Estandarización léxica e Imputación categórica | `'NO REPORTADO'` | Mantiene la integridad del conteo global sin atribuir un género ficticio a la víctima. |
| `GRUPO ETARIO` | 26 filas vacías / None | Imputación categórica explícita | `'NO REPORTADO'` | Evita calificar a un adulto como menor o viceversa sin soporte documental primario. |
| `ARMAS MEDIOS` | Múltiples formatos y vacíos | Normalización a mayúsculas limpias | `'NO REPORTADO'` | Agrupa la ausencia de especificación del arma empleada. |
| `CANTIDAD` | Posibles valores no numéricos | Conversión segura con fallback | `1` (entero positivo) | Todo reporte registrado corresponde al menos a una víctima formalmente individualizada. |

---

## 3. Corrección de Artefactos Tipográficos y Caracteres Corruptos (*Mojibake*)

El dataset crudo original descargado de la plataforma gubernamental presentaba problemas comunes de transcodificación (UTF-8 interpretado como ISO-8859-1 / Windows-1252). Se construyó un diccionario determinístico de sustitución en `clean_and_filter_atlantico.py`:

```python
reemplazos = {
    "ARTÃ CULO": "ARTÍCULO",
    "ARTÃ\x8dCULO": "ARTÍCULO",
    "AGRAVACIÃ“N": "AGRAVACIÓN",
    "AÃ‘OS": "AÑOS",
    "MonterÃ\xada": "Montería",
    "MonterÃ­a": "Montería",
    "CÃ“RDOBA": "CÓRDOBA",
    "Ã\x81": "Á", "Ã‰": "É", "Ã\x8d": "Í", "Ã“": "Ó", "Ãš": "Ú",
    "Ã¡": "á", "Ã©": "é", "Ã­": "í", "Ã³": "ó", "Ãº": "ú",
    "Ã±": "ñ", "Ã‘": "Ñ",
}
```
Esto garantiza que tanto en el motor de base de datos como en los reportes de Power BI y Streamlit los textos se visualicen con ortografía correcta.

---

## 4. Normalización Territorial de los 23 Municipios del Atlántico

En el dataset original, las capitales de departamento o distritos especiales contenían sufijos administrativos como `"Barranquilla (CT)"` (CT = Cabecera / Capital).
- Se aplicó una expresión regular: `re.sub(r"\s*\([Cc][Tt]\)", "", municipio)` para remover dicho sufijo.
- Se preservó el código oficial DANE de 8 dígitos con ceros a la izquierda (`08001000` para Barranquilla, `08758000` para Soledad, etc.), permitiendo la vinculación geoespacial con capas Shapefile / TopoJSON de Colombia.

---

## 5. Enriquecimiento de Dimensiones Temporales

La columna original `FECHA HECHO` contenía fechas en formato textual `DD/MM/YYYY`. Para maximizar la velocidad analítica se descompuso en:
1. `fecha_hecho`: Formato estándar ISO-8601 `YYYY-MM-DD`.
2. `anio`: Entero `SMALLINT` (2010 a 2026).
3. `mes`: Entero `SMALLINT` (1 a 12).
4. `nombre_mes`: Cadena en español (`Enero` a `Diciembre`).
5. `dia`: Entero `SMALLINT` (1 a 31).
6. `dia_semana`: Cadena en español (`Lunes` a `Domingo`).
7. `trimestre`: Entero `SMALLINT` (1 a 4).
8. `semestre`: Entero `SMALLINT` (1 a 2).

---

## 6. Variables de Auditoría Inmutable

Cumpliendo con los requerimientos académicos:
- `fecha_descarga_dataset = '2026-11-06'`: Constante histórica que certifica la fecha exacta del corte de información.
- `origen_datos = 'Policía Nacional de Colombia - Datos Abiertos'`: Trazabilidad institucional de la fuente primaria.

