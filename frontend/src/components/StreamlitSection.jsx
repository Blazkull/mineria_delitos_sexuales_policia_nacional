import React from 'react';
import { BarChart2, Calendar, Users, MapPin, Scale, Grid, Download, ExternalLink } from 'lucide-react';

export default function StreamlitSection() {
  const tabs = [
    { title: 'Temporal', icon: Calendar, color: 'text-blue-600 dark:text-blue-400', desc: 'Evolución interanual (2010 a 2026), estacionalidad por meses y días críticos de la semana.' },
    { title: 'Demografía', icon: Users, color: 'text-rose-600 dark:text-rose-400', desc: 'Distribución por género, análisis de infancia/adolescencia y matriz cruzada Género vs Edad.' },
    { title: 'Geografía', icon: MapPin, color: 'text-indigo-600 dark:text-indigo-400', desc: 'Concentración en los 23 municipios del Atlántico y porcentaje de criticidad del Área Metropolitana.' },
    { title: 'Tipología Penal', icon: Scale, color: 'text-purple-600 dark:text-purple-400', desc: 'Frecuencia por artículos del Código Penal (ej. Artículo 209) y medios o armas empleadas.' },
    { title: 'Matriz de Calor', icon: Grid, color: 'text-amber-600 dark:text-amber-400', desc: 'Mapa de calor interactivo que cruza municipios de mayor incidencia contra grupos etarios.' },
    { title: 'Explorador y Descarga', icon: Download, color: 'text-emerald-600 dark:text-emerald-400', desc: 'Filtro en tiempo real de registros con botón de descarga del subconjunto resultante en CSV.' },
  ];

  return (
    <section id="analytics" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-emerald-600 dark:text-emerald-400 mb-1">
              <BarChart2 className="w-3.5 h-3.5" />
              <span>Analítica Exploratoria (EDA)</span>
            </div>
            <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
              Dashboard Interactivo de Datos en Streamlit
            </h2>
            <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
              Aplicación de ciencia de datos construida en Python con Plotly Express, sincronizada con Supabase
              y provista de filtros dinámicos en barra lateral.
            </p>
          </div>

          <a
            href="http://localhost:8501"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-medium transition active:scale-[0.98] shadow-xs"
          >
            Abrir Streamlit EDA (:8501)
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>

        {/* Grilla de Módulos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          {tabs.map((tab, idx) => {
            const Icon = tab.icon;
            return (
              <div key={idx} className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 space-y-2 shadow-xs">
                <div className="flex items-center gap-2">
                  <Icon className={`w-4 h-4 ${tab.color}`} />
                  <span className="text-xs font-bold font-mono text-slate-800 dark:text-slate-200">
                    Pestaña {idx + 1}: {tab.title}
                  </span>
                </div>
                <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed font-sans">
                  {tab.desc}
                </p>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}
