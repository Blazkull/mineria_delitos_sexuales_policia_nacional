# AGENTS.md — Contexto de IA para el Módulo Frontend

> Este archivo proporciona contexto específico para cualquier IA o agente que trabaje en el directorio `frontend/`.
> El contexto global del sistema está en el archivo raíz: `../AGENTS.md`.

---

## 📌 Identidad de este Microservicio

| Campo | Valor |
|---|---|
| **Nombre** | Frontend — Portal Web Institucional / Dashboard Interactivo |
| **Tecnología Planificada** | React / Next.js o Vite + Tailwind CSS + Lucide Icons |
| **Rol en el Proyecto** | Capa visual complementaria y de consulta directa para investigadores y usuarios finales |
| **Consumo de Datos** | Consume la API REST del backend (`http://localhost:8000/api/v1`) |

---

## 🏗️ Arquitectura Prevista

```
frontend/
├── public/                 → Recursos estáticos (logos, imágenes, favicon)
├── src/
│   ├── components/         → Componentes UI reutilizables (Cards, Nav, KPIWidgets)
│   ├── pages/              → Vistas del portal (Dashboard, Reportes, Metodología)
│   ├── services/           → Clientes HTTP (Axios / Fetch) hacia Backend FastAPI
│   └── App.tsx             → Punto de entrada y enrutamiento
├── package.json            → Dependencias Node.js
├── AGENTS.md               → Este archivo
└── README.md               → Documentación del módulo
```

---

## 🚨 Reglas Críticas para la IA en `frontend/`

1. **Desacoplamiento Estricto:** Toda petición de datos se realiza a través de `backend/` (`API_BASE_URL`). NUNCA consultar la base de datos PostgreSQL de forma directa en el cliente.
2. **Diseño Responsivo e Institucional:** Usar colores institucionales sobrios (Azul marino `#1E3A8A`, Pizarra `#0F172A`, Blanco `#FFFFFF`).
3. **Manejo de Errores y Loading:** Todos los componentes con llamadas asíncronas deben contar con estados de carga (`Skeleton` o `Spinner`) y tratamiento amigable de excepciones de red.

