@echo off
TITLE Lanzador Unificado - Delitos Sexuales Atlantico
echo ==================================================================
echo   EJECUTANDO LANZADOR DE SERVICIOS (BACKEND, STREAMLIT, FRONTEND)
echo ==================================================================
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_dev.ps1"
pause

