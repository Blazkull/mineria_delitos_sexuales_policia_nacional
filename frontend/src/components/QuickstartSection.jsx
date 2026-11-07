import React, { useState } from 'react';
import { Terminal, Copy, Check, Zap, Play, Layers } from 'lucide-react';

export default function QuickstartSection() {
  const [copiedKey, setCopiedKey] = useState(null);

  const copyToClipboard = (text, key) => {
    navigator.clipboard.writeText(text);
    setCopiedKey(key);
    setTimeout(() => setCopiedKey(null), 2000);
  };

  return (
    <section id="quickstart" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        {/* Encabezado */}
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-1">
            <Zap className="w-3.5 h-3.5" />
            <span>Despliegue Rápido</span>
          </div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
            Guía de Arranque y Ejecución de Servicios
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
            Levante la arquitectura completa (Backend FastAPI en :8000, Streamlit EDA en :8501 y Frontend en :3000)
            mediante el lanzador unificado o siguiendo el procedimiento paso a paso.
          </p>
        </div>

        {/* Tarjeta de Comando Unificado */}
        <div className="p-6 rounded-2xl bg-gradient-to-r from-blue-50 to-indigo-50/60 dark:from-blue-950/60 dark:to-slate-900 border border-blue-200 dark:border-blue-500/30 shadow-xs">
          <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
            <div className="flex items-center gap-2">
              <span className="w-6 h-6 rounded-md bg-blue-600 text-white flex items-center justify-center text-xs font-bold font-mono">
                1
              </span>
              <span className="text-sm font-semibold text-slate-900 dark:text-white">
                Método Inmediato: Lanzador Unificado en 1 Sola Línea
              </span>
            </div>
            <span className="text-xs font-mono text-slate-600 dark:text-slate-400 bg-white/80 dark:bg-slate-900/80 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-800">
              Abre 3 consolas individuales
            </span>
          </div>

          <p className="text-xs text-slate-600 dark:text-slate-300 mb-4">
            Ejecute en la raíz del proyecto para validar el entorno virtual, levantar FastAPI, Streamlit y Frontend,
            y abrir automáticamente el navegador:
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            
            {/* Opción A: BAT */}
            <div className="p-3 rounded-lg bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 flex items-center justify-between font-mono text-xs shadow-xs">
              <div>
                <span className="text-slate-500 block text-[10px] uppercase font-sans">CMD o Doble Clic en Windows</span>
                <span className="text-emerald-600 dark:text-emerald-400 font-bold">run_dev.bat</span>
              </div>
              <button
                onClick={() => copyToClipboard('run_dev.bat', 'bat')}
                className="p-2 rounded bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 transition active:scale-95"
                title="Copiar comando"
              >
                {copiedKey === 'bat' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
              </button>
            </div>

            {/* Opción B: PowerShell */}
            <div className="p-3 rounded-lg bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 flex items-center justify-between font-mono text-xs shadow-xs">
              <div>
                <span className="text-slate-500 block text-[10px] uppercase font-sans">PowerShell</span>
                <span className="text-blue-600 dark:text-blue-400 font-bold">.\run_dev.ps1</span>
              </div>
              <button
                onClick={() => copyToClipboard('.\\run_dev.ps1', 'ps1')}
                className="p-2 rounded bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 transition active:scale-95"
                title="Copiar comando"
              >
                {copiedKey === 'ps1' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
              </button>
            </div>

          </div>
        </div>

        {/* Despliegue Manual Paso a Paso */}
        <div className="space-y-3">
          <div className="text-xs font-mono uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
            <Layers className="w-3.5 h-3.5" />
            <span>Procedimiento Manual por Consolas</span>
          </div>

          <div className="space-y-3">
            
            {/* Paso 1 */}
            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200">1. Crear y Activar Entorno Virtual Python 3.11</span>
                <button
                  onClick={() => copyToClipboard('py -3.11 -m venv backend/.venv\n.\\backend\\.venv\\Scripts\\Activate.ps1', 'step1')}
                  className="text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white text-xs flex items-center gap-1 transition"
                >
                  {copiedKey === 'step1' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              </div>
              <pre className="bg-slate-900 p-2.5 rounded font-mono text-xs text-slate-200 overflow-x-auto">
py -3.11 -m venv backend/.venv
.\backend\.venv\Scripts\Activate.ps1
              </pre>
            </div>

            {/* Paso 2 */}
            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200">2. Instalar Requerimientos de Backend y Analytics</span>
                <button
                  onClick={() => copyToClipboard('.\\backend\\.venv\\Scripts\\pip install -r backend/requirements.txt -r analytics/requirements.txt', 'step2')}
                  className="text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white text-xs flex items-center gap-1 transition"
                >
                  {copiedKey === 'step2' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              </div>
              <pre className="bg-slate-900 p-2.5 rounded font-mono text-xs text-slate-200 overflow-x-auto">
.\backend\.venv\Scripts\pip install -r backend/requirements.txt -r analytics/requirements.txt
              </pre>
            </div>

            {/* Paso 3 */}
            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200">3. Validar Conexión Supabase y Esquema DDL</span>
                <button
                  onClick={() => copyToClipboard('.\\backend\\.venv\\Scripts\\python.exe backend/scripts/test_db_connection.py\n.\\backend\\.venv\\Scripts\\python.exe backend/scripts/execute_ddl.py', 'step3')}
                  className="text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white text-xs flex items-center gap-1 transition"
                >
                  {copiedKey === 'step3' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              </div>
              <pre className="bg-slate-900 p-2.5 rounded font-mono text-xs text-slate-200 overflow-x-auto">
.\backend\.venv\Scripts\python.exe backend/scripts/test_db_connection.py
.\backend\.venv\Scripts\python.exe backend/scripts/execute_ddl.py
              </pre>
            </div>

            {/* Paso 4 */}
            <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800/80 shadow-xs">
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200">4. Iniciar Servidores de Aplicación</span>
                <button
                  onClick={() => copyToClipboard('# Terminal 1: Backend\n.\\backend\\.venv\\Scripts\\uvicorn.exe backend.app.main:app --host 0.0.0.0 --port 8000 --reload\n\n# Terminal 2: Streamlit\n.\\backend\\.venv\\Scripts\\streamlit.exe run analytics/app.py --server.port 8501\n\n# Terminal 3: Frontend React\ncd frontend; npm run dev', 'step4')}
                  className="text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white text-xs flex items-center gap-1 transition"
                >
                  {copiedKey === 'step4' ? <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              </div>
              <pre className="bg-slate-900 p-2.5 rounded font-mono text-xs text-slate-200 overflow-x-auto">
# Terminal 1: FastAPI Swagger (Puerto 8000)
.\backend\.venv\Scripts\uvicorn.exe backend.app.main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Streamlit EDA (Puerto 8501)
.\backend\.venv\Scripts\streamlit.exe run analytics/app.py --server.port 8501

# Terminal 3: Frontend React + Vite (Puerto 3000)
cd frontend; npm run dev
              </pre>
            </div>

          </div>
        </div>

      </div>
    </section>
  );
}
