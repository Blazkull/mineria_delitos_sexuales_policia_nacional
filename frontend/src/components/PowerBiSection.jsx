import React, { useState } from 'react';
import { BarChart, Copy, Check, Code, Calculator } from 'lucide-react';

export default function PowerBiSection() {
  const [copiedKey, setCopiedKey] = useState(null);

  const copyToClipboard = (text, key) => {
    navigator.clipboard.writeText(text);
    setCopiedKey(key);
    setTimeout(() => setCopiedKey(null), 2000);
  };

  const powerQueryM = `let
    // 1. Ingestión directa del endpoint REST (16,664 registros limpios sin ID)
    Origen = Json.Document(Web.Contents("http://localhost:8000/api/v1/delitos/powerbi/dataset")),
    TablaConvertida = Table.FromList(Origen, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    
    // 2. Expansión canónica de los 19 atributos de negocio
    ColumnasExpandidas = Table.ExpandRecordColumn(TablaConvertida, "Column1", 
        {"departamento", "municipio", "codigo_dane", "armas_medios", "fecha_hecho", "anio", "mes", 
         "nombre_mes", "dia", "dia_semana", "trimestre", "semestre", "genero", "grupo_etario", 
         "cantidad", "codigo_articulo", "delito", "fecha_descarga_dataset", "origen_datos"}),
         
    // 3. Tipado estricto para optimización del motor VertiPaq
    TiposCambiados = Table.TransformColumnTypes(ColumnasExpandidas,{
        {"fecha_hecho", type date},
        {"anio", Int64.Type},
        {"mes", Int64.Type},
        {"dia", Int64.Type},
        {"trimestre", Int64.Type},
        {"semestre", Int64.Type},
        {"cantidad", Int64.Type},
        {"codigo_dane", type text},
        {"fecha_descarga_dataset", type date}
    })
in
    TiposCambiados`;

  return (
    <section id="powerbi" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-amber-600 dark:text-amber-400 mb-1">
            <BarChart className="w-3.5 h-3.5" />
            <span>Guía de Handoff para el Desarrollador de BI</span>
          </div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
            Especificación Técnica para Power BI Desktop (.pbix)
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
            Todo lo necesario para que el colega o desarrollador encargado de Power BI ensamble
            el tablero directivo con conexión directa al Backend o a PostgreSQL en Supabase.
          </p>
        </div>

        {/* Tarjeta del Endpoint Web */}
        <div className="p-6 rounded-2xl bg-gradient-to-r from-amber-50 via-orange-50/50 to-slate-50 dark:from-amber-950/40 dark:via-slate-900 dark:to-slate-900 border border-amber-200 dark:border-amber-500/30 shadow-xs">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs uppercase font-mono tracking-wider text-amber-700 dark:text-amber-400 font-bold">
              Conector Web en Power BI Desktop
            </span>
            <span className="text-xs font-mono text-slate-500 dark:text-slate-400">16,664 registros limpios</span>
          </div>
          <p className="text-xs text-slate-700 dark:text-slate-300 mb-4">
            En Power BI Desktop, seleccione <strong className="text-slate-900 dark:text-white">Obtener datos → Web</strong> y pegue la siguiente URL:
          </p>

          <div className="p-3 rounded-lg bg-white dark:bg-slate-950 border border-amber-200 dark:border-slate-800 flex items-center justify-between font-mono text-xs shadow-xs">
            <span className="text-amber-800 dark:text-amber-300 select-all overflow-x-auto mr-2 font-semibold">
              http://localhost:8000/api/v1/delitos/powerbi/dataset
            </span>
            <button
              onClick={() => copyToClipboard('http://localhost:8000/api/v1/delitos/powerbi/dataset', 'pbi-url')}
              className="p-2 rounded bg-amber-600 hover:bg-amber-500 text-white transition active:scale-95 shrink-0"
            >
              {copiedKey === 'pbi-url' ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
            </button>
          </div>
          <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-2">
            *Una vez desplegado en Render, la URL se actualiza a <code className="text-slate-800 dark:text-slate-300">https://api-delitos-sexuales-atlantico.onrender.com/api/v1/delitos/powerbi/dataset</code>.
          </p>
        </div>

        {/* Código M de Power Query */}
        <div className="space-y-2">
          <div className="flex items-center justify-between text-xs font-mono text-slate-700 dark:text-slate-300">
            <span className="flex items-center gap-1.5 font-bold text-amber-700 dark:text-amber-400">
              <Code className="w-4 h-4" />
              Código M para el Editor Avanzado de Power Query
            </span>
            <button
              onClick={() => copyToClipboard(powerQueryM, 'm-code')}
              className="text-xs text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white flex items-center gap-1 transition"
            >
              {copiedKey === 'm-code' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
              <span>Copiar Script M</span>
            </button>
          </div>
          <pre className="p-4 rounded-xl bg-slate-900 border border-slate-800 font-mono text-xs text-slate-200 overflow-x-auto leading-relaxed">
            {powerQueryM}
          </pre>
        </div>

        {/* Fórmulas DAX Fundamentales */}
        <div className="space-y-3">
          <div className="flex items-center gap-2 text-xs font-mono text-slate-800 dark:text-slate-300 font-bold">
            <Calculator className="w-4 h-4 text-blue-600 dark:text-blue-400" />
            <span>Fórmulas DAX Obligatorias del Modelo</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs font-mono">
            
            <div className="p-3 rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
              <span className="text-slate-500 dark:text-slate-400 text-[11px] block font-sans">Volumen Total de Hechos</span>
              <span className="text-blue-600 dark:text-blue-400 font-bold block mt-1">Total Casos = COUNTROWS('Fact_Delitos')</span>
            </div>

            <div className="p-3 rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
              <span className="text-slate-500 dark:text-slate-400 text-[11px] block font-sans">Proporción de Víctimas Femeninas</span>
              <span className="text-rose-600 dark:text-rose-400 font-bold block mt-1">% Casos Femenino = DIVIDE(CALCULATE([Total Casos], 'Fact_Delitos'[genero] = "FEMENINO"), [Total Casos], 0)</span>
            </div>

            <div className="p-3 rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
              <span className="text-slate-500 dark:text-slate-400 text-[11px] block font-sans">Vulnerabilidad de Infancia y Adolescencia</span>
              <span className="text-amber-600 dark:text-amber-400 font-bold block mt-1">% Vulnerabilidad Infantil = DIVIDE(CALCULATE([Total Casos], 'Fact_Delitos'[grupo_etario] IN &#123;"MENORES", "ADOLESCENTES"&#125;), [Total Casos], 0)</span>
            </div>

            <div className="p-3 rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
              <span className="text-slate-500 dark:text-slate-400 text-[11px] block font-sans">Concentración en el Área Metropolitana</span>
              <span className="text-indigo-600 dark:text-indigo-400 font-bold block mt-1">% Area Metro = DIVIDE(CALCULATE([Total Casos], 'Fact_Delitos'[municipio] IN &#123;"Barranquilla", "Soledad", "Malambo", "Galapa", "Puerto Colombia"&#125;), [Total Casos], 0)</span>
            </div>

          </div>
        </div>

        {/* Las 5 Páginas del Reporte */}
        <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2 shadow-xs">
          <div className="text-xs font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold">
            Estructura Recomendada de las 5 Páginas del Tablero
          </div>
          <ol className="text-xs text-slate-700 dark:text-slate-300 space-y-1.5 list-decimal list-inside font-sans">
            <li><strong className="text-slate-900 dark:text-white">Página 1: Resumen Ejecutivo y KPIs Directivos</strong> (Tarjetas de métricas, distribución por género y velocímetros).</li>
            <li><strong className="text-slate-900 dark:text-white">Página 2: Análisis Histórico y Estacionalidad Temporal</strong> (Línea de tendencia 2010–2026, heatmap de meses y días).</li>
            <li><strong className="text-slate-900 dark:text-white">Página 3: Vulnerabilidad Demográfica e Infancia</strong> (Pirámide de grupos etarios y cruce Género vs Edad).</li>
            <li><strong className="text-slate-900 dark:text-white">Página 4: Focalización Geográfica y Territorial</strong> (Top municipios, mapa del Atlántico y concentración metropolitana).</li>
            <li><strong className="text-slate-900 dark:text-white">Página 5: Tipificación Penal y Armas Empleadas</strong> (Artículos del Código Penal y gráfico de medios utilizados).</li>
          </ol>
        </div>

      </div>
    </section>
  );
}
