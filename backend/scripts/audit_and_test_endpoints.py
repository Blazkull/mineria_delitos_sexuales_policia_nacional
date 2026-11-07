import sys
import json
import urllib.request
import urllib.parse

BASE_URL = "http://localhost:8000"

def log(msg, status="INFO"):
    colors = {
        "INFO": "\033[94m",
        "SUCCESS": "\033[92m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "RESET": "\033[0m"
    }
    print(f"{colors.get(status, '')}[{status}] {msg}{colors['RESET']}")

def check_openapi_spec():
    log("Examinando la especificación OpenAPI (Swagger)...", "INFO")
    url = f"{BASE_URL}/api/v1/openapi.json"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    # 1. Verificar si algún parámetro de consulta, path o header se llama 'id'
    found_id_params = []
    for path, methods in data.get("paths", {}).items():
        for method, details in methods.items():
            for param in details.get("parameters", []):
                pname = param.get("name", "")
                if pname.lower() == "id":
                    found_id_params.append((path, method, pname))

    # 2. Verificar si algún esquema del modelo contiene un campo 'id'
    found_id_schema_fields = []
    schemas = data.get("components", {}).get("schemas", {})
    for sname, sdef in schemas.items():
        properties = sdef.get("properties", {})
        if "id" in properties:
            found_id_schema_fields.append((sname, "id"))

    if found_id_params:
        log(f"¡Alerta! Se encontraron parámetros 'id': {found_id_params}", "ERROR")
    else:
        log("CERO parámetros 'id' recibidos en todos los endpoints de Swagger.", "SUCCESS")

    if found_id_schema_fields:
        log(f"¡Alerta! Se encontraron campos 'id' en los esquemas: {found_id_schema_fields}", "ERROR")
    else:
        log("CERO campos 'id' definidos en los esquemas Pydantic/OpenAPI.", "SUCCESS")

    return len(found_id_params) == 0 and len(found_id_schema_fields) == 0

def test_endpoint(url_path, description, expected_keys_should_not_have=["id"]):
    url = f"{BASE_URL}{url_path}"
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            status_code = resp.getcode()
            body = json.loads(resp.read().decode("utf-8"))
            
            # Validar ausencia de id
            has_id = False
            sample = None
            if isinstance(body, dict):
                if "id" in body:
                    has_id = True
                if "data" in body and isinstance(body["data"], list) and len(body["data"]) > 0:
                    sample = body["data"][0]
                    if "id" in sample:
                        has_id = True
            elif isinstance(body, list) and len(body) > 0:
                sample = body[0]
                if isinstance(sample, dict) and "id" in sample:
                    has_id = True

            if status_code == 200 and not has_id:
                count_info = f"({len(body)} items)" if isinstance(body, list) else f"(total: {body.get('total', 'N/A')})"
                log(f"OK (HTTP {status_code}) - {description} {count_info} | ¿Lleva 'id'?: NO", "SUCCESS")
                return True
            else:
                log(f"FALLO en {url_path}: HTTP {status_code}, ¿Lleva 'id'?: {has_id}", "ERROR")
                return False
    except Exception as e:
        log(f"Error consultando {url_path}: {e}", "ERROR")
        return False

def main():
    print("=" * 70)
    print(" AUDITORÍA Y TEST DE ENDPOINTS: CONTROL DE COLUMNA ID Y DISPONIBILIDAD ")
    print("=" * 70)

    all_passed = True

    # 1. Inspección estricta de OpenAPI / Swagger
    if not check_openapi_spec():
        all_passed = False

    print("-" * 70)
    print(" PROBANDO TODOS LOS ENDPOINTS REST EN VIVO")
    print("-" * 70)

    tests = [
        ("/health", "Health check del sistema"),
        ("/api/v1/delitos?limit=5", "Listado general paginado (limit=5)"),
        ("/api/v1/delitos?municipio=Soledad&genero=FEMENINO&anio=2024&limit=3", "Filtro multidimensional (Municipio + Género + Año)"),
        ("/api/v1/delitos?delito_buscar=acoso&limit=3", "Búsqueda textual de delito ('acoso')"),
        ("/api/v1/delitos?fecha_desde=2023-01-01&fecha_hasta=2023-06-30&limit=3", "Filtro por rango de fechas exactas"),
        ("/api/v1/delitos?codigo_articulo=ART%C3%8DCULO%20209&limit=3", "Filtro por artículo penal (Artículo 209)"),
        ("/api/v1/delitos/filtros/opciones", "Catálogo dinámico de opciones para selectores"),
        ("/api/v1/delitos/powerbi/dataset", "Dataset completo para Power BI Desktop (16,664 registros)"),
        ("/api/v1/delitos/metricas/anual", "Serie temporal métrica anual"),
        ("/api/v1/delitos/metricas/municipios?top=5", "Top 5 municipios con mayor incidencia"),
        ("/api/v1/delitos/metricas/genero", "Distribución por género"),
        ("/api/v1/delitos/metricas/grupo-etario", "Distribución por grupo etario"),
        ("/api/v1/delitos/metricas/articulos?top=5", "Top 5 artículos del Código Penal")
    ]

    for path, desc in tests:
        res = test_endpoint(path, desc)
        if not res:
            all_passed = False

    print("=" * 70)
    if all_passed:
        log("TODAS LAS PRUEBAS COMPLETADAS CON ÉXITO: CERO 'id' EN ENTRADAS Y SALIDAS.", "SUCCESS")
    else:
        log("ALGUNAS PRUEBAS FALLARON. REVISAR LOGS ANTERIORES.", "ERROR")
    print("=" * 70)

if __name__ == "__main__":
    main()
