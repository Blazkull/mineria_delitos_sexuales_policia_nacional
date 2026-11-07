---
name: run-dev-servers
description: Levanta todos los proyectos de la monorepo en consolas individuales.
---

# Run Dev Servers

Esta skill permite levantar los servidores de desarrollo de todas las aplicaciones (`rsvp-admin`, `web`, `landing`) en consolas de PowerShell individuales para facilitar el monitoreo de logs de manera independiente.

## Instrucciones de uso

Para levantar los proyectos, el agente debe ejecutar el script de PowerShell `scripts/start-all.ps1` usando la herramienta `run_command`.

```powershell
.\scripts\start-all.ps1
```

Si necesitas levantar únicamente un frontend específico en segundo plano para análisis, puedes ejecutar el comando directo de npm, por ejemplo:
`npm run dev --workspace=rsvp-admin`
