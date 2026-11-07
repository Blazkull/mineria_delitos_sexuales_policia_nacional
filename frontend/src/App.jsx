import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import QuickstartSection from './components/QuickstartSection';
import ArchitectureSection from './components/ArchitectureSection';
import DatabaseSection from './components/DatabaseSection';
import TechMatrixSection from './components/TechMatrixSection';
import EndpointsSection from './components/EndpointsSection';
import PowerBiSection from './components/PowerBiSection';
import StreamlitSection from './components/StreamlitSection';
import RenderSection from './components/RenderSection';
import Footer from './components/Footer';
import { 
  Play, 
  Network, 
  Database, 
  Cpu, 
  Terminal, 
  BarChart, 
  BarChart2, 
  Cloud 
} from 'lucide-react';

export default function App() {
  // 1. REGLA: El tema base/default es CLARO ('light')
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem('theme') || 'light';
  });

  // 2. Control de sección activa dinámica por scroll o clic manual
  const [activeSection, setActiveSection] = useState('quickstart');

  // Sincronización del tema en la raíz del documento HTML
  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => (prev === 'dark' ? 'light' : 'dark'));
  };

  const navItems = [
    { id: 'quickstart', href: '#quickstart', label: '1. Arranque Rápido', icon: Play },
    { id: 'arquitectura', href: '#arquitectura', label: '2. Arquitectura', icon: Network },
    { id: 'database', href: '#database', label: '3. PostgreSQL Supabase', icon: Database },
    { id: 'tecnologias', href: '#tecnologias', label: '4. Stack y Librerías', icon: Cpu },
    { id: 'endpoints', href: '#endpoints', label: '5. Endpoints & Swagger', icon: Terminal },
    { id: 'powerbi', href: '#powerbi', label: '6. Handoff Power BI', icon: BarChart },
    { id: 'analytics', href: '#analytics', label: '7. Streamlit EDA', icon: BarChart2 },
    { id: 'render', href: '#render', label: '8. Despliegue Render', icon: Cloud },
  ];

  // Observador de scroll para actualizar la sección activa dinámicamente
  useEffect(() => {
    const sectionIds = navItems.map(item => item.id);

    const handleScroll = () => {
      const scrollPosition = window.scrollY + 220; // Margen para cabecera fija
      for (let i = sectionIds.length - 1; i >= 0; i--) {
        const sectionEl = document.getElementById(sectionIds[i]);
        if (sectionEl && sectionEl.offsetTop <= scrollPosition) {
          setActiveSection(sectionIds[i]);
          break;
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNavClick = (id, href) => {
    setActiveSection(id);
    const targetEl = document.querySelector(href);
    if (targetEl) {
      targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <div className="min-h-[100dvh] bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-200 flex flex-col font-sans transition-colors duration-200">
      
      {/* Barra de Navegación Fija con Selector de Tema */}
      <Navbar theme={theme} onToggleTheme={toggleTheme} />

      {/* Hero Principal Asimétrico */}
      <Hero />

      {/* Cuerpo Principal con Sidebar de Índice Dinámico */}
      <div className="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-grow w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Sidebar Izquierda: Tabla de Contenidos Dinámica */}
          <aside className="hidden lg:block lg:col-span-3 sticky top-24">
            <div className="p-4 rounded-2xl bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 shadow-xs space-y-3 transition-colors duration-200">
              <span className="text-[11px] font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-bold block">
                Contenidos del Sistema
              </span>
              
              <nav className="space-y-1 text-xs font-mono">
                {navItems.map((item) => {
                  const Icon = item.icon;
                  const isActive = activeSection === item.id;
                  return (
                    <a
                      key={item.id}
                      href={item.href}
                      onClick={(e) => {
                        e.preventDefault();
                        handleNavClick(item.id, item.href);
                      }}
                      className={`flex items-center gap-2.5 px-3 py-2.5 rounded-lg transition-all duration-150 active:scale-[0.98] ${
                        isActive
                          ? 'bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 font-bold border-l-4 border-blue-600 dark:border-blue-500 shadow-xs pl-2.5'
                          : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60'
                      }`}
                    >
                      <Icon className={`w-3.5 h-3.5 shrink-0 ${isActive ? 'text-blue-600 dark:text-blue-400' : 'text-slate-400 dark:text-slate-500'}`} />
                      <span>{item.label}</span>
                    </a>
                  );
                })}
              </nav>

              <div className="pt-3 border-t border-slate-200 dark:border-slate-800/80">
                <span className="text-[10px] text-slate-500 dark:text-slate-400 block mb-1">Lanzador Automático</span>
                <code className="block bg-slate-100 dark:bg-slate-950 text-emerald-700 dark:text-emerald-400 p-2 rounded text-[11px] font-mono select-all border border-slate-200 dark:border-slate-800">
                  run_dev.bat
                </code>
              </div>
            </div>
          </aside>

          {/* Área de Secciones Técnicas */}
          <main className="lg:col-span-9 space-y-8">
            <QuickstartSection />
            <ArchitectureSection theme={theme} />
            <DatabaseSection />
            <TechMatrixSection />
            <EndpointsSection />
            <PowerBiSection />
            <StreamlitSection />
            <RenderSection />
          </main>

        </div>
      </div>

      {/* Pie de Página Institucional */}
      <Footer />
    </div>
  );
}
