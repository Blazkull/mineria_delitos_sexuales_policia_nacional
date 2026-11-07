import React from 'react';
import { Cpu } from 'lucide-react';

export default function TechMatrixSection() {
  const stack = [
    { tech: 'Python', version: '3.11.0', layer: 'Lenguaje Núcleo', role: 'Motor base de cálculo numérico, API REST y computación vectorial.' },
    { tech: 'FastAPI', version: '0.110+', layer: 'Backend REST API', role: 'Framework asíncrono de alto rendimiento con validación OpenAPI y Swagger UI.' },
    { tech: 'Uvicorn', version: '0.28+', layer: 'Servidor ASGI', role: 'Servidor web ultrarrápido para entornos de producción y reload local.' },
    { tech: 'Pandas', version: '3.1.1', layer: 'ETL y Analítica', role: 'Procesamiento de 405,193 filas nacionales a 16,664 de Atlántico con 0 pérdida.' },
    { tech: 'NumPy', version: '2.4.6', layer: 'Cómputo Numérico', role: 'Agrupaciones vectorizadas y cálculo condicional de matrices.' },
    { tech: 'SQLAlchemy', version: '2.1+', layer: 'ORM / Core', role: 'Modelado relacional y consultas SQL compiladas a PostgreSQL.' },
    { tech: 'Psycopg2-binary', version: '2.9.13', layer: 'Driver PostgreSQL', role: 'Conexión binaria eficiente al Transaction Pooler de Supabase.' },
    { tech: 'Streamlit', version: '1.35+', layer: 'Dashboard EDA', role: 'Interfaz interactiva de exploración analítica con 6 pestañas especializadas.' },
    { tech: 'Plotly Express', version: '5.20+', layer: 'Visualización', role: 'Generación de gráficos multivariados dinámicos, matrices de calor y series.' },
    { tech: 'React + Vite', version: '18.3+ / 6.0+', layer: 'Frontend Web', role: 'Portal de documentación técnica con diseño reactivo de alta gama.' },
    { tech: 'Tailwind CSS', version: '3.4+', layer: 'Estilos y UI', role: 'Sistema de diseño utilitario optimizado sin emojis y acelerado por hardware.' },
    { tech: 'PostgreSQL (Supabase)', version: '17.0', layer: 'Base de Datos Cloud', role: 'Persistencia en nube con 8 índices B-Tree y Row Level Security (RLS).' },
    { tech: 'Render', version: 'PaaS Cloud', layer: 'Infraestructura', role: 'Despliegue multi-servicio automático mediante render.yaml (IaC).' },
    { tech: 'Power BI Desktop', version: '2024+', layer: 'Business Intelligence', role: 'Modelado dimensional en estrella y tablero directivo para la toma de decisiones.' },
  ];

  return (
    <section id="tecnologias" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-1">
            <Cpu className="w-3.5 h-3.5" />
            <span>Stack de Ingeniería</span>
          </div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
            Matriz Integral de Tecnologías y Dependencias
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
            Relación de herramientas, versiones estables y justificación técnica en el ciclo de vida de los datos.
          </p>
        </div>

        <div className="border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden bg-white dark:bg-slate-900/40 shadow-xs">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-mono">
              <thead className="bg-slate-100 dark:bg-slate-900 text-slate-700 dark:text-slate-400 uppercase tracking-wider border-b border-slate-200 dark:border-slate-800">
                <tr>
                  <th className="p-3 font-semibold">Tecnología</th>
                  <th className="p-3 font-semibold">Versión</th>
                  <th className="p-3 font-semibold">Capa del Sistema</th>
                  <th className="p-3 font-semibold font-sans">Propósito y Justificación Técnica</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 dark:divide-slate-800/60 text-slate-800 dark:text-slate-200">
                {stack.map((item, idx) => (
                  <tr key={idx} className="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition">
                    <td className="p-3 font-bold text-blue-600 dark:text-blue-400">{item.tech}</td>
                    <td className="p-3 text-slate-600 dark:text-slate-300">{item.version}</td>
                    <td className="p-3 text-slate-500 dark:text-slate-400 font-sans">{item.layer}</td>
                    <td className="p-3 text-slate-600 dark:text-slate-300 font-sans">{item.role}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </section>
  );
}
