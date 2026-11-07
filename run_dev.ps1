# =============================================================================
# RUN DEV SERVERS: Minería de Datos - Delitos Sexuales en Atlántico
# Inicia Backend (FastAPI :8000), Analytics (Streamlit :8501) y Frontend (:3000)
# =============================================================================

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "   INICIANDO SERVICIOS DEL SISTEMA (BACKEND + STREAMLIT + FRONT)  " -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""

$RootPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RootPath

$VenvPython = Join-Path $RootPath "backend\.venv\Scripts\python.exe"
$VenvUvicorn = Join-Path $RootPath "backend\.venv\Scripts\uvicorn.exe"
$VenvStreamlit = Join-Path $RootPath "backend\.venv\Scripts\streamlit.exe"

if (-not (Test-Path $VenvPython)) {
    Write-Host "[ERROR] No se encontró el entorno virtual en backend/.venv." -ForegroundColor Red
    Write-Host "Por favor ejecute primero: py -3.11 -m venv backend/.venv" -ForegroundColor Yellow
    exit 1
}

# 1. Iniciar Backend FastAPI en consola independiente
Write-Host "[1/3] Levantando Backend FastAPI en http://localhost:8000 ..." -ForegroundColor Green
$BackendCmd = "cd '$RootPath'; & '$VenvUvicorn' backend.app.main:app --host 0.0.0.0 --port 8000 --reload"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'FastAPI Backend (:8000)'; $BackendCmd"

Start-Sleep -Seconds 2

# 2. Iniciar Analytics Streamlit en consola independiente
Write-Host "[2/3] Levantando Analytics Streamlit en http://localhost:8501 ..." -ForegroundColor Green
$StreamlitCmd = "cd '$RootPath'; & '$VenvStreamlit' run analytics/app.py --server.port 8501"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'Streamlit Analytics (:8501)'; $StreamlitCmd"

Start-Sleep -Seconds 2

# 3. Iniciar Frontend Portal (React + Vite) en consola independiente
Write-Host "[3/3] Levantando Frontend React + Vite en http://localhost:3000 ..." -ForegroundColor Green
$FrontendDir = Join-Path $RootPath "frontend"
$FrontendCmd = "cd '$FrontendDir'; npm run dev"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$Host.UI.RawUI.WindowTitle = 'Frontend React Vite (:3000)'; $FrontendCmd"

Start-Sleep -Seconds 1

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "           TODOS LOS SERVICIOS SE ENCUENTRAN ACTIVOS              " -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host " • Frontend Portal:   http://localhost:3000" -ForegroundColor White
Write-Host " • Analytics EDA:     http://localhost:8501" -ForegroundColor White
Write-Host " • Backend Swagger:   http://localhost:8000/docs" -ForegroundColor White
Write-Host " • Power BI Dataset:  http://localhost:8000/api/v1/delitos/powerbi/dataset" -ForegroundColor White
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""

# Abrir el navegador en el portal de frontend
Start-Process "http://localhost:3000"

