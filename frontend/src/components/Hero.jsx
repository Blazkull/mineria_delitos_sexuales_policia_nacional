import React from 'react';
import { ShieldAlert, Database, Calendar, Users, MapPin, Lock } from 'lucide-react';

export default function Hero() {
  return (
    <section className="relative pt-10 pb-16 px-4 sm:px-6 lg:px-8 border-b border-slate-200 dark:border-slate-900 bg-gradient-to-b from-slate-100/80 via-white to-slate-50 dark:from-slate-950 dark:via-slate-900/60 dark:to-slate-950 transition-colors duration-200">
      <div className="max-w-[1400px] mx-auto">
        
        {/* Badges de estado superior */}
        <div className="flex flex-wrap items-center gap-2.5 mb-6 text-xs font-mono">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800/50">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            Supabase PostgreSQL Activo (Pooler :6543)
          </div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800">
            <Calendar className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400" />
            Descarga Oficial: 2026-11-06 (Inmutable)
          </div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800">
            <Lock className="w-3.5 h-3.5 text-purple-600 dark:text-purple-400" />
            RLS Habilitado · 0 Columnas ID
          </div>
        </div>

        {/* Layout Asimétrico: Izquierda Contexto | Derecha Métricas Canónicas */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <div className="lg:col-span-7 space-y-4">
            <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-tight">
              Minería de Datos y Analítica Territorial de Delitos Sexuales
            </h1>
            <p className="text-slate-600 dark:text-slate-400 text-base leading-relaxed max-w-[65ch]">
              Sistema de ingeniería analítica para el procesamiento histórico (2010–2026) en los 23 municipios
              del Departamento del Atlántico. Basado en registros oficiales de la Policía Nacional de Colombia,
              garantizando una política estricta de <strong className="text-slate-900 dark:text-slate-200">cero pérdida de información</strong>,
              persistencia relacional en Supabase, API REST en FastAPI y tableros interactivos desacoplados.
            </p>

            <div className="pt-2 flex flex-wrap gap-3">
              <a
                href="#quickstart"
                className="px-4 py-2.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-medium text-xs sm:text-sm transition shadow-sm active:scale-[0.98]"
              >
                Guía de Arranque Rápido
              </a>
              <a
                href="#powerbi"
                className="px-4 py-2.5 rounded-lg bg-amber-50 dark:bg-amber-500/10 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-500/30 hover:bg-amber-100 dark:hover:bg-amber-500/20 font-medium text-xs sm:text-sm transition active:scale-[0.98]"
              >
                Especificación para Power BI
              </a>
              <a
                href="#arquitectura"
                className="px-4 py-2.5 rounded-lg bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 font-medium text-xs sm:text-sm transition active:scale-[0.98] shadow-xs"
              >
                Diagramas de Arquitectura
              </a>
            </div>
          </div>

          {/* Panel Lateral de Métricas Clave */}
          <div className="lg:col-span-5 grid grid-cols-2 gap-3">
            
            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="text-xs uppercase font-mono tracking-wider text-slate-500 dark:text-slate-400 flex items-center justify-between">
                <span>Registros Atlántico</span>
                <Database className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400" />
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-blue-600 dark:text-blue-400 font-mono mt-2">16,664</div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">100% preservados (0 nulos)</div>
            </div>

            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="text-xs uppercase font-mono tracking-wider text-slate-500 dark:text-slate-400 flex items-center justify-between">
                <span>Víctimas Femeninas</span>
                <Users className="w-3.5 h-3.5 text-rose-600 dark:text-rose-400" />
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-rose-600 dark:text-rose-400 font-mono mt-2">85.12%</div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">14,184 hechos documentados</div>
            </div>

            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="text-xs uppercase font-mono tracking-wider text-slate-500 dark:text-slate-400 flex items-center justify-between">
                <span>Infancia y Juventud</span>
                <ShieldAlert className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-amber-600 dark:text-amber-400 font-mono mt-2">32.93%</div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">5,487 menores de 18 años</div>
            </div>

            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="text-xs uppercase font-mono tracking-wider text-slate-500 dark:text-slate-400 flex items-center justify-between">
                <span>Distrito Central</span>
                <MapPin className="w-3.5 h-3.5 text-indigo-600 dark:text-indigo-400" />
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-indigo-600 dark:text-indigo-400 font-mono mt-2">52.68%</div>
              <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">Barranquilla (8,778 casos)</div>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}
