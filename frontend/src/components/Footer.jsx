import React from 'react';
import { Shield } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="py-10 border-t border-slate-200 dark:border-slate-900 bg-white dark:bg-slate-950 text-slate-500 dark:text-slate-400 text-xs font-mono transition-colors duration-200">
      <div className="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap justify-between items-center gap-4">
        
        <div className="space-y-1">
          <div className="flex items-center gap-2 text-slate-800 dark:text-slate-200 font-semibold font-sans">
            <Shield className="w-4 h-4 text-blue-600 dark:text-blue-500" />
            <span>Observatorio de Delitos Sexuales — Departamento del Atlántico (2010–2026)</span>
          </div>
          <p className="text-[11px] text-slate-500 dark:text-slate-400">
            Fuente Oficial: Policía Nacional de Colombia · Portal de Datos Abiertos (datos.gov.co) · Descarga: 2026-11-06
          </p>
        </div>

        <div className="flex items-center space-x-4 text-[11px]">
          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-600 dark:hover:text-slate-200 transition"
          >
            Swagger API (:8000)
          </a>
          <span>·</span>
          <a
            href="http://localhost:8501"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-emerald-600 dark:hover:text-slate-200 transition"
          >
            Streamlit EDA (:8501)
          </a>
          <span>·</span>
          <a
            href="http://localhost:8000/health"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-600 dark:hover:text-slate-200 transition"
          >
            Health Check
          </a>
        </div>

      </div>
    </footer>
  );
}
