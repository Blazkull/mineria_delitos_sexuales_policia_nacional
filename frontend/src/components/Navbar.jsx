import React from 'react';
import { Shield, ExternalLink, Terminal, Database, BarChart3, Code2, Sun, Moon } from 'lucide-react';

export default function Navbar({ theme, onToggleTheme }) {
  return (
    <header className="sticky top-0 z-50 bg-white/80 dark:bg-slate-950/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800/80 transition-colors duration-200">
      <div className="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand / Logo */}
        <div className="flex items-center space-x-3">
          <div className="w-9 h-9 rounded-lg bg-blue-50 dark:bg-blue-600/20 border border-blue-200 dark:border-blue-500/40 flex items-center justify-center text-blue-600 dark:text-blue-400">
            <Shield className="w-5 h-5" />
          </div>
          <div>
            <span className="font-bold text-sm sm:text-base text-slate-900 dark:text-white tracking-tight block leading-tight">
              Observatorio de Delitos Sexuales
            </span>
            <span className="text-xs text-slate-500 dark:text-slate-400 font-mono">
              Atlántico (2010–2026) · Manual Técnico
            </span>
          </div>
        </div>

        {/* Live Service Links & Theme Toggle */}
        <div className="flex items-center space-x-2 text-xs font-medium">
          
          <a
            href="http://localhost:8501"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-50 dark:bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-500/30 hover:bg-emerald-100 dark:hover:bg-emerald-500/20 transition active:scale-[0.98]"
          >
            <BarChart3 className="w-3.5 h-3.5" />
            Streamlit (:8501)
            <ExternalLink className="w-3 h-3 text-emerald-600/60 dark:text-emerald-500/60" />
          </a>

          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-blue-50 dark:bg-blue-500/10 text-blue-700 dark:text-blue-400 border border-blue-200 dark:border-blue-500/30 hover:bg-blue-100 dark:hover:bg-blue-500/20 transition active:scale-[0.98]"
          >
            <Code2 className="w-3.5 h-3.5" />
            Swagger (:8000)
            <ExternalLink className="w-3 h-3 text-blue-600/60 dark:text-blue-500/60" />
          </a>

          <a
            href="http://localhost:8000/api/v1/delitos/powerbi/dataset"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-50 dark:bg-amber-500/10 text-amber-700 dark:text-amber-400 border border-amber-200 dark:border-amber-500/30 hover:bg-amber-100 dark:hover:bg-amber-500/20 transition active:scale-[0.98]"
          >
            <Database className="w-3.5 h-3.5" />
            Power BI JSON
            <ExternalLink className="w-3 h-3 text-amber-600/60 dark:text-amber-500/60" />
          </a>

          {/* Botón de Cambio de Tema (Light / Dark) */}
          <button
            onClick={onToggleTheme}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-100 dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-800 transition active:scale-[0.98]"
            title={theme === 'dark' ? 'Cambiar a modo Claro' : 'Cambiar a modo Oscuro'}
          >
            {theme === 'dark' ? (
              <>
                <Sun className="w-3.5 h-3.5 text-amber-400" />
                <span className="hidden sm:inline font-mono text-[11px]">Claro</span>
              </>
            ) : (
              <>
                <Moon className="w-3.5 h-3.5 text-slate-600" />
                <span className="hidden sm:inline font-mono text-[11px]">Oscuro</span>
              </>
            )}
          </button>

        </div>
      </div>
    </header>
  );
}
