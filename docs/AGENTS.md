# AGENTS.md — Contexto de IA para el Módulo de Documentación y Tareas

> Este archivo proporciona contexto específico para cualquier IA o agente que trabaje en el directorio `docs/`.
> El contexto global del sistema está en el archivo raíz: `../AGENTS.md`.

---

## 📌 Identidad de este Módulo

| Campo | Valor |
|---|---|
| **Nombre** | Documentación Técnica, Gestión de Tareas y Soporte Académico |
| **Fuente de la Verdad** | `docs/tasks/MASTER_STATUS.md` |
| **Normativa Académica** | Normas APA (7ª edición), rigor científico, redacción en voz impersonal |
| **Entregables Vinculados** | Artículo científico (Word), Script SQL Neon/Supabase, PBIX Power BI, evidencias gráficas |

---

## 🏗️ Arquitectura Interna de `docs/`

```
docs/
├── tasks/
│   ├── MASTER_STATUS.md        → Tablero central con checkboxes, progreso y control Git Flow
│   └── fases/                  → Detalle por fase operativa (01 a 05)
├── architecture/
│   └── ARCHITECTURE.md         → Diagramas de arquitectura, flujo de datos y componentes (Mermaid)
├── database/
│   ├── DATABASE_SCHEMA.md      → DDL SQL, tipos de datos, índices y justificación técnica
│   └── supabase_ddl.sql        → Script ejecutable en SQL Editor de Supabase / Neon
├── paper/
│   └── PLAN_ARTICULO.md        → Esquema del artículo de 4.000 palabras, referencias APA 7ª y figuras
├── powerbi/
│   └── POWERBI_GUIDE.md        → Guía de conexión a PostgreSQL/Supabase, modelo estrella y medidas DAX
├── data_set/                   → Repositorio de datasets crudos y limpios
├── AGENTS.md                   → Este archivo
└── README.md                   → Índice general de documentación
```

---

## 🚨 Reglas Críticas para la IA en `docs/`

1. **Actualización Mandatoria de `MASTER_STATUS.md`:** Cada vez que se culmine una tarea o fase, se DEBE marcar la casilla `[x]` correspondiente y actualizar la fecha de última modificación.
2. **Inmutabilidad del Dataset Original:** No modificar `Reporte__Delitos_sexuales_Policía_Nacional_20261106.csv`.
3. **Control de Originalidad y Detección de IA:** Los borradores y textos para el artículo científico deben mantener un rigor formal y analítico para cumplir con el límite máximo de 15% de similitud / detección de IA exigido por la universidad.
4. **Referencias Académicas:** Mínimo 15 referencias en normas APA 7ª edición de los últimos tres años (2024, 2025, 2026).

