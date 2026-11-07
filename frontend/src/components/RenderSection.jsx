import React from 'react';
import { Cloud, Server } from 'lucide-react';

export default function RenderSection() {
  return (
    <section id="render" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-1">
            <Cloud className="w-3.5 h-3.5" />
            <span>Infraestructura como Código (IaC)</span>
          </div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
            Despliegue Multi-Servicio en Render (render.yaml)
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
            Configuración unificada para desplegar automáticamente el Backend FastAPI y el Dashboard
            Streamlit en la nube con monitoreo de salud y recarga continua.
          </p>
        </div>

        {/* Comparativa de los 2 Servicios */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          {/* Servicio Backend */}
          <div className="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3 shadow-xs">
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono font-bold text-blue-600 dark:text-blue-400 flex items-center gap-1.5">
                <Server className="w-4 h-4" />
                Web Service 1: Backend FastAPI
              </span>
              <span className="text-[11px] font-mono text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded">Python 3.11</span>
            </div>
            
            <div className="space-y-2 text-xs font-mono text-slate-700 dark:text-slate-300">
              <div className="p-2 rounded bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800/80">
                <span className="text-slate-500 block text-[10px] uppercase font-sans">Nombre del Servicio</span>
                <span className="font-semibold text-slate-900 dark:text-slate-100">api-delitos-sexuales-atlantico</span>
              </div>
              <div className="p-2 rounded bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800/80">
                <span className="text-slate-500 block text-[10px] uppercase font-sans">Build & Start Commands</span>
                <span className="text-emerald-600 dark:text-emerald-400 font-semibold">pip install -r backend/requirements.txt</span><br/>
                <span className="text-blue-600 dark:text-blue-400 font-semibold">uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT</span>
              </div>
              <div className="p-2 rounded bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800/80">
                <span className="text-slate-500 block text-[10px] uppercase font-sans">Health Check Path</span>
                <span className="text-amber-600 dark:text-amber-400 font-semibold">/health</span>
              </div>
            </div>
          </div>

          {/* Servicio Analytics */}
          <div className="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3 shadow-xs">
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono font-bold text-emerald-600 dark:text-emerald-400 flex items-center gap-1.5">
                <Server className="w-4 h-4" />
                Web Service 2: Analytics Streamlit
              </span>
              <span className="text-[11px] font-mono text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded">Python 3.11</span>
            </div>
            
            <div className="space-y-2 text-xs font-mono text-slate-700 dark:text-slate-300">
              <div className="p-2 rounded bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800/80">
                <span className="text-slate-500 block text-[10px] uppercase font-sans">Nombre del Servicio</span>
                <span className="font-semibold text-slate-900 dark:text-slate-100">analytics-delitos-sexuales-atlantico</span>
              </div>
              <div className="p-2 rounded bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800/80">
                <span className="text-slate-500 block text-[10px] uppercase font-sans">Build & Start Commands</span>
                <span className="text-emerald-600 dark:text-emerald-400 font-semibold">pip install -r analytics/requirements.txt</span><br/>
                <span className="text-blue-600 dark:text-blue-400 font-semibold">streamlit run analytics/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true</span>
              </div>
              <div className="p-2 rounded bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800/80">
                <span className="text-slate-500 block text-[10px] uppercase font-sans">Health Check Path</span>
                <span className="text-amber-600 dark:text-amber-400 font-semibold">/_stcore/health</span>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
