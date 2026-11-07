# **Artículo Científico** 

# **Asignatura:** Minería de Datos 

# **Presentación** 

La presente guía establece los lineamientos, requisitos técnicos, criterios académicos y condiciones de entrega que los estudiantes deben cumplir en la elaboración de un artículo científico basado en el conjunto de datos suministrado por el docente. La actividad integra competencias de gestión de datos, análisis exploratorio, visualización, interpretación crítica y comunicación científica, de modo que el estudiante transite por el ciclo completo de un proyecto analítico: desde el almacenamiento de los datos hasta la formulación de recomendaciones sustentadas en evidencia. 

Se espera que el trabajo trascienda la mera ejecución de herramientas. El valor de la actividad radica en la capacidad del estudiante para formular preguntas pertinentes, justificar decisiones metodológicas, interpretar resultados con rigor y argumentar su aporte a la toma de decisiones. 

# **Objetivo** 

Desarrollar un artículo científico que permita aplicar técnicas de almacenamiento, exploración, análisis y visualización de datos sobre el conjunto de datos suministrado, con el propósito de identificar patrones, tendencias y hallazgos relevantes que aporten valor al proceso de toma de decisiones. 

# **Requisitos técnicos obligatorios** 

# **Gestión y almacenamiento de datos** 

- El conjunto de datos debe almacenarse **obligatoriamente en PostgreSQL utilizando la plataforma Neon o similar** . 

- Debe evidenciarse el proceso de creación de la base de datos, la definición de las tablas y la carga de los datos. 

- Se deben incluir capturas de pantalla que demuestren el uso de PostgreSQL Neon (por ejemplo, el panel del proyecto, el editor SQL, la estructura de las tablas y la verificación de los registros cargados). 

- Se recomienda documentar las decisiones de diseño: tipos de datos, claves primarias, restricciones e índices, así como el esquema resultante. 

# **Análisis Exploratorio de Datos (EDA)** 

- No se borra ningún registros en el conjunto de datos original 

- **El EDA** debe realizarse con **Python con Streamlit** . 

- Se deben aplicar técnicas de limpieza, transformación y exploración de datos, justificando cada decisión (imputación, eliminación, codificación, normalización, entre otras). 

- Es obligatorio identificar y analizar: valores faltantes, valores atípicos, distribuciones, correlaciones y variables relevantes. 

- Se deben incorporar estadísticas descriptivas y análisis visual (histogramas, diagramas de caja, mapas de calor de correlación, gráficos de dispersión, entre otros). 

- Se deben incluir capturas de pantalla del desarrollo (código) y de la ejecución de la aplicación en Streamlit. 

# **Visualización de datos** 

- Se deben diseñar dashboards e informes interactivos en **Power BI** . 

- Las visualizaciones deben estar orientadas al análisis y al descubrimiento de conocimiento, no a la mera decoración. 

- Se deben incorporar indicadores, gráficos y métricas (KPI) que permitan comprender el comportamiento de los datos. 

- Se deben incluir capturas de pantalla del entorno de Power BI (modelo, conexión a los datos, medidas) y del dashboard desarrollado. 

- Se recomienda aplicar buenas prácticas de diseño: jerarquía visual, selección adecuada del tipo de gráfico, uso coherente del color, filtros y segmentadores que faciliten la exploración. 

# **Analítica y hallazgos** 

- Se debe realizar un análisis de los resultados obtenidos. 

- Se deben identificar patrones, tendencias, comportamientos, oportunidades, riesgos o problemáticas relevantes. 

- Todo hallazgo debe sustentarse con evidencia derivada de los análisis realizados (tablas, gráficos, estadísticas). 

- Se deben formular recomendaciones basadas en datos, coherentes con los hallazgos y viables en el contexto del conjunto de datos. 

# **Evidencias obligatorias** 

# **Importante: No será válido ningún artículo que no presente evidencias gráficas del uso de todas las herramientas tecnológicas exigidas.** 

El artículo debe contener imágenes y capturas de pantalla que evidencien claramente el uso de las siguientes herramientas: 

- **PostgreSQL Neon.** 

- **Python.** 

- **Streamlit.** 

- **Power BI.** 

# Recomendaciones para las evidencias: 

- Las capturas deben ser legibles, estar numeradas y llevar título y fuente (por ejemplo, «Figura 3. Estructura de la tabla principal en PostgreSQL Neon. Elaboración propia»). 

- Cada figura debe ser mencionada y comentada en el texto; una captura sin análisis asociado no constituye evidencia suficiente. 

- Se debe evitar mostrar credenciales, cadenas de conexión completas o información sensible en las imágenes. 

# **Criterios académicos** 

- **Extensión:** mínimo de **4.000 palabras** , sin incluir las referencias bibliográficas. 

- **Referencias:** mínimo de **15 referencias bibliográficas** . 

- **Tipo de fuentes:** artículos científicos, libros, documentos académicos, informes técnicos o publicaciones especializadas. Se recomienda priorizar bases de datos académicas indexadas. 

- **Actualidad:** las fuentes consultadas **no deben superar los últimos tres (3) años de publicación** . 

- **Formato de citación:** normas **APA, última edición** , con correspondencia estricta entre las citas del texto y la lista de referencias. 

- **Calidad de la redacción:** rigor académico, coherencia, cohesión y argumentación científica; uso de voz impersonal o tercera persona, y terminología técnica precisa. 

# **Política de originalidad** 

- El trabajo será sometido a herramientas de revisión de similitud y de detección de contenido generado por inteligencia artificial. 

- Se espera que el documento presente un **porcentaje máximo del 15 %** de similitud total y de detección de IA. 

- Los estudiantes deberán realizar **análisis propios, interpretación crítica y discusión fundamentada** de los resultados obtenidos. 

- Los textos copiados, parafraseados incorrectamente o generados sin revisión académica podrán generar la **no aprobación de la actividad** . 

La integridad académica es una condición indispensable. Se recomienda que cada estudiante conserve los registros de su proceso de trabajo (versiones del código, consultas SQL, avances del dashboard), pues podrán ser solicitados como soporte de autoría. 

# **Entregables** 

1. Artículo científico en formato **WORD** . 

2. Base de datos implementada en **PostgreSQL Neon** (SCRIPT) 

3. Código fuente utilizado en **Python y Streamlit** . 

4. Archivo de **Power BI (.pbix)** . 

5. Copia de conjunto de datos original (csv) ya que puede cambiar con el tiempo. 

6. Evidencias gráficas de todas las herramientas utilizadas. 

# **Recomendaciones para la entrega:** 

- Organizar los archivos en una estructura clara y nombrarlos de forma coherente (por ejemplo, <mark>Apellido_Nombre_Articulo.docx</mark> ). 

- Incluir un archivo de instrucciones (README) con los pasos para ejecutar la aplicación de Streamlit y las dependencias necesarias. 

- Verificar que el acceso a la base de datos en Neon y los archivos entregados funcionen antes del envío, sin exponer credenciales en documentos públicos. 

# 23 de noviembre entrega 

