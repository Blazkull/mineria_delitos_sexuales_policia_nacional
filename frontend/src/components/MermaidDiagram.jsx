import React, { useEffect, useRef, useState } from 'react';

export default function MermaidDiagram({ chart, id, theme = 'light' }) {
  const containerRef = useRef(null);
  const [svgContent, setSvgContent] = useState('');

  useEffect(() => {
    let isMounted = true;
    if (window.mermaid && chart) {
      const isDark = theme === 'dark';
      
      window.mermaid.initialize({
        startOnLoad: false,
        theme: isDark ? 'dark' : 'default',
        themeVariables: isDark
          ? {
              darkMode: true,
              background: '#0B132B',
              primaryColor: '#1E3A8A',
              primaryTextColor: '#F1F5F9',
              primaryBorderColor: '#3B82F6',
              lineColor: '#60A5FA',
              secondaryColor: '#1E293B',
              tertiaryColor: '#0F172A'
            }
          : {
              darkMode: false,
              background: '#F8FAFC',
              primaryColor: '#EFF6FF',
              primaryTextColor: '#0F172A',
              primaryBorderColor: '#2563EB',
              lineColor: '#3B82F6',
              secondaryColor: '#F1F5F9',
              tertiaryColor: '#E2E8F0'
            },
        flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' }
      });

      const uniqueId = `mermaid-${id || Math.random().toString(36).substring(2, 9)}-${Date.now()}`;
      window.mermaid
        .render(uniqueId, chart)
        .then(({ svg }) => {
          if (isMounted) {
            setSvgContent(svg);
          }
        })
        .catch((err) => {
          console.error('Mermaid render error:', err);
        });
    }
    return () => {
      isMounted = false;
    };
  }, [chart, id, theme]);

  return (
    <div
      ref={containerRef}
      className="overflow-x-auto p-4 rounded-xl bg-white dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 flex justify-center text-xs shadow-xs transition-colors duration-200"
      dangerouslySetInnerHTML={{ __html: svgContent }}
    />
  );
}
