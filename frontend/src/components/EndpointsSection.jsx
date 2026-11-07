import React, { useState } from 'react';
import { Terminal, Play, Loader2, ExternalLink } from 'lucide-react';

export default function EndpointsSection() {
  const [output, setOutput] = useState('// Seleccione un endpoint y presione "Consultar en Vivo"');
  const [loading, setLoading] = useState(false);
  const [activeEndpoint, setActiveEndpoint] = useState('/api/v1/delitos/metricas/anual');
  const [statusBadge, setStatusBadge] = useState({ text: 'Listo para consultar', type: 'idle' });

  const endpoints = [
    { path: '/api/v1/delitos/metricas/anual', label: 'Métricas Anuales (2010–2026)', desc: 'Serie temporal interanual de hechos y víctimas' },
    { path: '/api/v1/delitos/metricas/municipios?top=5', label: 'Top 5 Municipios', desc: 'Ranking de concentración territorial y porcentajes' },
    { path: '/api/v1/delitos/metricas/genero', label: 'Distribución por Género', desc: 'Desglose porcentual y absolutos por género' },
    { path: '/api/v1/delitos/metricas/grupo-etario', label: 'Distribución por Grupo Etario', desc: 'Segmentación entre menores, adolescentes y adultos' },
    { path: '/api/v1/delitos/filtros/opciones', label: 'Catálogo de Filtros', desc: 'Listados únicos de 23 municipios, artículos y fechas' },
    { path: '/api/v1/delitos?municipio=Soledad&genero=FEMENINO&anio=2024&limit=3', label: 'Filtro Multidimensional', desc: 'Consulta en Soledad con género femenino en 2024' },
    { path: '/health', label: 'Health Check', desc: 'Estado operativo del backend FastAPI y versión' },
  ];

  const handleTest = async (endpointPath, label) => {
    setActiveEndpoint(endpointPath);
    setLoading(true);
    setStatusBadge({ text: `Consultando ${label}...`, type: 'loading' });
    setOutput(`Conectando con http://localhost:8000${endpointPath} ...`);

    try {
      const response = await fetch(`http://localhost:8000${endpointPath}`);
      const data = await response.json();
      setLoading(false);
      setStatusBadge({ text: `HTTP ${response.status} OK · Respuesta Recibida`, type: 'success' });
      const formatted = JSON.stringify(data, null, 2);
      setOutput(formatted.length > 2500 ? formatted.slice(0, 2500) + '\n\n... [Truncado para vista previa]' : formatted);
    } catch (err) {
      setLoading(false);
      setStatusBadge({ text: 'Error al contactar Backend', type: 'error' });
      setOutput(`Error de conexión con http://localhost:8000${endpointPath}.\nVerifique que el backend esté corriendo en otra terminal:\n\nrun_dev.bat o .\\run_dev.ps1`);
    }
  };

  return (
    <section id="endpoints" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-1">
              <Terminal className="w-3.5 h-3.5" />
              <span>API REST & Swagger</span>
            </div>
            <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
              Catálogo de Endpoints y Consola de Pruebas en Vivo
            </h2>
            <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
              Todos los endpoints responden en JSON estándar, operan sin requerir ni enviar la columna sintética ID
              y están documentados interactivamente con OpenAPI y Swagger UI.
            </p>
          </div>

          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-medium transition active:scale-[0.98] shadow-xs"
          >
            Abrir Swagger UI Completo (:8000/docs)
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>

        {/* Consola Interactiva */}
        <div className="rounded-2xl bg-slate-900 border border-slate-800 p-5 space-y-4 shadow-sm text-white">
          
          <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-800">
            <span className="text-xs font-mono font-bold text-blue-400 flex items-center gap-1.5">
              <Terminal className="w-4 h-4" />
              Consola de Petición HTTP en Tiempo Real
            </span>

            <span className={`text-xs font-mono px-2 py-0.5 rounded ${
              statusBadge.type === 'success' ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' :
              statusBadge.type === 'error' ? 'bg-rose-950 text-rose-400 border border-rose-800' :
              statusBadge.type === 'loading' ? 'bg-blue-950 text-blue-400 border border-blue-800' :
              'bg-slate-800 text-slate-400'
            }`}>
              {statusBadge.text}
            </span>
          </div>

          {/* Botones de Consulta */}
          <div className="flex flex-wrap gap-2">
            {endpoints.map((ep, idx) => (
              <button
                key={idx}
                onClick={() => handleTest(ep.path, ep.label)}
                disabled={loading}
                className={`text-xs font-mono px-3 py-1.5 rounded-lg border transition active:scale-95 flex items-center gap-1.5 ${
                  activeEndpoint === ep.path
                    ? 'bg-blue-600 text-white border-blue-500 shadow-sm'
                    : 'bg-slate-950 text-slate-300 border-slate-800 hover:border-slate-700'
                }`}
              >
                {loading && activeEndpoint === ep.path ? (
                  <Loader2 className="w-3 h-3 animate-spin text-white" />
                ) : (
                  <Play className="w-3 h-3 text-blue-400" />
                )}
                {ep.label}
              </button>
            ))}
          </div>

          {/* Salida JSON */}
          <pre className="p-4 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-emerald-400 max-h-72 overflow-y-auto leading-relaxed">
            {output}
          </pre>

        </div>

      </div>
    </section>
  );
}
