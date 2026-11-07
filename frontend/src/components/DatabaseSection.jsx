import React from 'react';
import { Database, ShieldCheck, ListTree, CheckCircle } from 'lucide-react';

export default function DatabaseSection() {
  const columns = [
    { name: 'departamento', type: 'VARCHAR(50)', constraint: 'NOT NULL', desc: "Constante inmutable: 'ATLÁNTICO'" },
    { name: 'municipio', type: 'VARCHAR(100)', constraint: 'PRIMARY KEY', desc: 'Nombre oficial normalizado (23 municipios)' },
    { name: 'codigo_dane', type: 'VARCHAR(20)', constraint: 'NOT NULL', desc: "Código DANE 8 dígitos (ej. '08001000')" },
    { name: 'armas_medios', type: 'VARCHAR(100)', constraint: 'NOT NULL', desc: 'Arma o medio empleado en la conducta' },
    { name: 'fecha_hecho', type: 'DATE', constraint: 'PRIMARY KEY', desc: 'Fecha estándar (YYYY-MM-DD)' },
    { name: 'anio', type: 'SMALLINT', constraint: 'PRIMARY KEY', desc: 'Año del hecho (2010 a 2026)' },
    { name: 'mes', type: 'SMALLINT', constraint: 'NOT NULL', desc: 'Mes numérico (1 a 12)' },
    { name: 'nombre_mes', type: 'VARCHAR(20)', constraint: 'NOT NULL', desc: 'Nombre del mes en español' },
    { name: 'dia', type: 'SMALLINT', constraint: 'NOT NULL', desc: 'Día del mes (1 a 31)' },
    { name: 'dia_semana', type: 'VARCHAR(20)', constraint: 'NOT NULL', desc: 'Día de la semana (Lunes a Domingo)' },
    { name: 'trimestre', type: 'SMALLINT', constraint: 'NOT NULL', desc: 'Trimestre calendario (1 a 4)' },
    { name: 'semestre', type: 'SMALLINT', constraint: 'NOT NULL', desc: 'Semestre calendario (1 a 2)' },
    { name: 'genero', type: 'VARCHAR(30)', constraint: 'PRIMARY KEY', desc: 'FEMENINO, MASCULINO o NO REPORTADO' },
    { name: 'grupo_etario', type: 'VARCHAR(30)', constraint: 'PRIMARY KEY', desc: 'ADULTOS, MENORES, ADOLESCENTES, NO REPORTADO' },
    { name: 'cantidad', type: 'INTEGER', constraint: 'PRIMARY KEY', desc: 'Cantidad de víctimas (mínimo 1)' },
    { name: 'codigo_articulo', type: 'VARCHAR(30)', constraint: 'NOT NULL', desc: "Artículo penal (ej. 'ARTÍCULO 209')" },
    { name: 'delito', type: 'TEXT', constraint: 'PRIMARY KEY', desc: 'Descripción penal completa corregida' },
    { name: 'fecha_descarga_dataset', type: 'DATE', constraint: 'NOT NULL', desc: "Auditoría inmutable: '2026-11-06'" },
    { name: 'origen_datos', type: 'VARCHAR(150)', constraint: 'NOT NULL', desc: 'Policía Nacional de Colombia - Datos Abiertos' },
  ];

  return (
    <section id="database" className="py-12 border-b border-slate-200 dark:border-slate-900 transition-colors duration-200">
      <div className="space-y-6">
        
        <div>
          <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-1">
            <Database className="w-3.5 h-3.5" />
            <span>Almacenamiento Estructurado</span>
          </div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">
            Modelo Relacional PostgreSQL en Supabase
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-400 mt-1 max-w-[65ch]">
            Tabla <code className="text-blue-600 dark:text-blue-400 font-mono">delitos_sexuales_atlantico</code> optimizada
            con 8 índices B-Tree, seguridad a nivel de filas (RLS) y sin claves artificiales redundantes.
          </p>
        </div>

        {/* Regla de Dominio: Cero ID */}
        <div className="p-4 rounded-xl bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-800/60 text-xs sm:text-sm text-blue-900 dark:text-blue-200 flex items-start gap-3 shadow-xs">
          <CheckCircle className="w-5 h-5 text-blue-600 dark:text-blue-400 shrink-0 mt-0.5" />
          <div>
            <strong className="text-slate-900 dark:text-white">Regla de Integridad de Dominio:</strong> La tabla no contiene columna sintética <code className="bg-blue-100 dark:bg-blue-900/60 px-1 py-0.5 rounded text-blue-900 dark:text-white font-mono">id</code>.
            Toda la analítica se ejecuta sobre las 19 dimensiones canónicas oficiales garantizando cero dispersión de llaves.
          </div>
        </div>

        {/* Tabla de Diccionario */}
        <div className="border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden bg-white dark:bg-slate-900/50 shadow-xs">
          <div className="overflow-x-auto max-h-96">
            <table className="w-full text-left text-xs font-mono">
              <thead className="bg-slate-100 dark:bg-slate-900 text-slate-700 dark:text-slate-400 uppercase tracking-wider border-b border-slate-200 dark:border-slate-800 sticky top-0 z-10">
                <tr>
                  <th className="p-3 font-semibold">Columna</th>
                  <th className="p-3 font-semibold">Tipo SQL</th>
                  <th className="p-3 font-semibold">Restricción</th>
                  <th className="p-3 font-semibold font-sans">Descripción del Atributo</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 dark:divide-slate-800/60 text-slate-800 dark:text-slate-200">
                {columns.map((col, idx) => (
                  <tr key={idx} className="hover:bg-slate-50 dark:hover:bg-slate-800/30 transition">
                    <td className="p-3 font-bold text-blue-600 dark:text-blue-400">{col.name}</td>
                    <td className="p-3 text-slate-600 dark:text-slate-300">{col.type}</td>
                    <td className="p-3 text-slate-500 dark:text-slate-400">{col.constraint}</td>
                    <td className="p-3 text-slate-600 dark:text-slate-300 font-sans">{col.desc}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Índices y RLS */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 shadow-xs">
            <div className="flex items-center gap-2 text-xs font-bold text-amber-700 dark:text-amber-400 uppercase tracking-wider mb-2">
              <ListTree className="w-3.5 h-3.5" />
              <span>8 Índices B-Tree Compuestos y Simples</span>
            </div>
            <ul className="text-xs font-mono text-slate-600 dark:text-slate-400 space-y-1">
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_anio</span> (anio)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_municipio</span> (municipio)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_fecha_hecho</span> (fecha_hecho)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_codigo_articulo</span> (codigo_articulo)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_genero</span> (genero)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_grupo_etario</span> (grupo_etario)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_anio_municipio</span> (anio, municipio)</li>
              <li>• <span className="text-slate-900 dark:text-slate-200 font-semibold">idx_delitos_genero_grupo</span> (genero, grupo_etario)</li>
            </ul>
          </div>

          <div className="p-4 rounded-xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 shadow-xs">
            <div className="flex items-center gap-2 text-xs font-bold text-emerald-700 dark:text-emerald-400 uppercase tracking-wider mb-2">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>Políticas de Seguridad Row Level Security (RLS)</span>
            </div>
            <div className="text-xs text-slate-600 dark:text-slate-400 space-y-2">
              <p>
                <strong className="text-slate-900 dark:text-slate-200 font-sans">Lectura Pública (SELECT):</strong> Habilitada para roles <code className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-emerald-700 dark:text-emerald-400 font-mono">anon</code> y <code className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-emerald-700 dark:text-emerald-400 font-mono">authenticated</code>.
              </p>
              <p>
                <strong className="text-slate-900 dark:text-slate-200 font-sans">Escritura Protegida (ALL):</strong> Confinada exclusivamente a roles de servicio administrativo <code className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-rose-700 dark:text-rose-400 font-mono">service_role</code> y <code className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-rose-700 dark:text-rose-400 font-mono">postgres</code>.
              </p>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}
