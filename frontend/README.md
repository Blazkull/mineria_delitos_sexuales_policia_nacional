# 🌐 Frontend: Portal Web de Documentación & Arquitectura

> **Tecnología:** React 18 + Vite + Tailwind CSS + Lucide Icons  
> **Puerto Local:** `http://localhost:3000`  
> **Diseño:** Directivas de alta gama UI/UX (`design-taste-frontend`), tipografía Geist, sin emojis, layout asimétrico y soporte para Vercel.

---

## 📌 1. Propósito del Portal

Este portal web actúa como el centro de mando y documentación técnica del proyecto:
1. **Guía de Arranque Rápido:** Comandos interactivos con botón de copia (`run_dev.bat` y `run_dev.ps1`).
2. **Diagramas de Arquitectura:** Renderizados con Mermaid.js (Pipeline ETL y Topología en Render).
3. **Modelo Relacional:** Diccionario de datos de 19 columnas, 8 índices B-Tree y políticas de seguridad RLS.
4. **Consola en Vivo:** Peticiones HTTP en tiempo real contra los endpoints de FastAPI en `:8000`.
5. **Guía de Handoff para Power BI:** Código Power Query M, modelado en estrella y fórmulas DAX para el desarrollador del tablero.
6. **Módulos de Streamlit:** Detalle de las 6 pestañas de analítica exploratoria.
7. **Infraestructura Render:** Manifiesto multi-servicio `render.yaml`.

---

## 🚀 2. Ejecución en Modo Desarrollo

```bash
# Ubicarse en frontend/
cd frontend

# Instalar dependencias (React, Lucide, Tailwind, Vite)
npm install

# Iniciar servidor de desarrollo en http://localhost:3000
npm run dev
```

---

## 📦 3. Compilación para Producción & Despliegue en Vercel

```bash
# Compilar bundle estático optimizado en dist/
npm run build

# Previsualizar el bundle localmente en :3000
npm run preview
```

### ☁️ Despliegue en Vercel:
1. Conectar el repositorio de GitHub en [Vercel](https://vercel.com).
2. Configurar:
   - **Root Directory:** `frontend`
   - **Framework Preset:** `Vite`
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
3. ¡Despliegue automático instantáneo!
