import React from 'react';
import MermaidDiagram from './MermaidDiagram';
import { Network, Workflow, GitBranch } from 'lucide-react';

export default function ArchitectureSection({ theme = 'light' }) {
  const etlChart = `flowchart TD
    subgraph S1["1. Ingestión Oficial"]
        RAW["Reporte Oficial Policía Nacional<br/>(405,193 registros Colombia)"]
    end

    subgraph S2["2. Pipeline ETL Python / Pandas"]
        FILTER["Filtrado Departamental<br/>DEPARTAMENTO == 'ATLÁNTICO'<br/>(16,664 registros)"]
        CLEAN["Limpieza & Imputación:<br/>- Sin eliminar registros<br/>- Imputación 'NO REPORTADO'<br/>- Normalización de tildes y nombres"]
        ENRICH["Enriquecimiento Temporal:<br/>- anio, mes, dia, dia_semana<br/>- trimestre, semestre<br/>- Auditoría: 2026-11-06"]
        CSV_CLEAN["docs/data_set/<br/>delitos_sexuales_atlantico_limpio.csv"]
    end

    subgraph S3["3. Persistencia Cloud"]
        SUPABASE[("PostgreSQL 17 en Supabase<br/>aws-0-us-east-2.pooler.supabase.com:6543<br/>19 Dimensiones | Sin ID | RLS")]
    end

    subgraph S4["4. Consumo y Distribución"]
        API["Backend FastAPI (:8000)<br/>Swagger & OpenAPI Docs"]
        STREAMLIT["Streamlit EDA (:8501)<br/>Dashboard Exploratorio"]
        POWERBI["Power BI Desktop (.pbix)<br/>Web Connector JSON"]
        FRONTEND["Frontend React (:3000)<br/>Documentación Técnica"]
    end

    RAW --> FILTER
    FILTER --> CLEAN
    CLEAN --> ENRICH
    ENRICH --> CSV_CLEAN
    CSV_CLEAN --> SUPABASE
    SUPABASE --> API
    SUPABASE --> STREAMLIT
    API --> POWERBI
    API --> FRONTEND`;

  const renderChart = `flowchart LR
    subgraph REPO["Monorepo GitHub"]
        YAML["render.yaml<br/>(IaC Manifiesto)"]
        BK_CODE["backend/"]
        ST_CODE["analytics/"]
    end

    subgraph RENDER["Plataforma Render Cloud"]
        SRV_BK["Web Service: api-delitos-sexuales<br/>FastAPI en Uvicorn (:10000)"]
        SRV_ST["Web Service: analytics-delitos-sexuales<br/>Streamlit Server (:10000)"]
    end

    subgraph CLOUD_DB["Persistencia Nube"]
        DB_POOL["Supabase Transaction Pooler<br/>IPv4 Puerto 6543"]
    end

    YAML --> RENDER
    BK_CODE --> SRV_BK
    ST_CODE --> SRV_ST
    SRV_BK --> DB_POOL
    SRV_ST --> DB_POOL`;

  return (
    <section id="arquitectura" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-1">
            <Network className="w-3.5 h-3.5" />
            <span>Topología y Flujo del Dato</span>
          </div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
            Diagramas de Arquitectura del Sistema
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
            Diseño modular desacoplado que garantiza trazabilidad desde la fuente original de la Policía Nacional
            hasta los destinos analíticos sin alteración del volumen muestral.
          </p>
        </div>

        {/* Diagrama 1 */}
        <div className="space-y-3">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-700 dark:text-slate-300">
            <Workflow className="w-4 h-4 text-blue-600 dark:text-blue-400" />
            <span className="font-bold">Diagrama 1: Flujo ETL de Procesamiento y Consumo Desacoplado</span>
          </div>
          <MermaidDiagram chart={etlChart} id="etl" theme={theme} />
        </div>

        {/* Diagrama 2 */}
        <div className="space-y-3 pt-4">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-700 dark:text-slate-300">
            <GitBranch className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
            <span className="font-bold">Diagrama 2: Despliegue Multi-Servicio en Render (IaC)</span>
          </div>
          <MermaidDiagram chart={renderChart} id="render" theme={theme} />
        </div>

      </div>
    </section>
  );
}
