from typing import Optional, List, Dict, Any, Union
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator

class DelitoBaseSchema(BaseModel):
    departamento: str = Field("ATLÁNTICO", description="Nombre del departamento", example="ATLÁNTICO")
    municipio: str = Field(..., description="Nombre oficial del municipio normalizado", example="Barranquilla")
    codigo_dane: str = Field(..., description="Código DANE estandarizado de 8 dígitos", example="08001000")
    armas_medios: str = Field(..., description="Arma o medio empleado", example="NO REPORTADO")
    fecha_hecho: date = Field(..., description="Fecha de comisión o denuncia (YYYY-MM-DD)", example="2023-05-18")
    anio: int = Field(..., description="Año del hecho (2010 - 2026)", example=2023)
    mes: int = Field(..., description="Mes numérico (1 a 12)", example=5)
    nombre_mes: str = Field(..., description="Nombre del mes en español", example="Mayo")
    dia: int = Field(..., description="Día del mes (1 a 31)", example=18)
    dia_semana: str = Field(..., description="Día de la semana en español", example="Jueves")
    trimestre: int = Field(..., description="Trimestre del año (1 a 4)", example=2)
    semestre: int = Field(..., description="Semestre del año (1 a 2)", example=1)
    genero: str = Field(..., description="Género de la víctima", example="FEMENINO")
    grupo_etario: str = Field(..., description="Grupo etario de la víctima", example="MENORES")
    cantidad: int = Field(1, description="Cantidad de víctimas asociadas al registro", example=1)
    codigo_articulo: str = Field(..., description="Referencia del artículo penal", example="ARTÍCULO 209")
    delito: str = Field(..., description="Descripción jurídica completa del delito", example="ARTÍCULO 209. ACTOS SEXUALES CON MENOR DE 14 AÑOS")
    fecha_descarga_dataset: date = Field(..., description="Fecha fija de captura del dataset", example="2026-11-06")
    origen_datos: str = Field(..., description="Fuente oficial de los datos", example="Policía Nacional de Colombia - Datos Abiertos")

    @field_validator("codigo_dane", mode="before")
    @classmethod
    def validar_codigo_dane(cls, v: Any) -> str:
        if v is None:
            return "08001000"
        return str(v).strip().zfill(8)

class DelitoResponseSchema(DelitoBaseSchema):
    creado_en: Optional[datetime] = Field(None, description="Fecha de inserción en base de datos", example="2026-11-06T16:50:00Z")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "departamento": "ATLÁNTICO",
                "municipio": "Barranquilla",
                "codigo_dane": "08001000",
                "armas_medios": "NO REPORTADO",
                "fecha_hecho": "2023-05-18",
                "anio": 2023,
                "mes": 5,
                "nombre_mes": "Mayo",
                "dia": 18,
                "dia_semana": "Jueves",
                "trimestre": 2,
                "semestre": 1,
                "genero": "FEMENINO",
                "grupo_etario": "MENORES",
                "cantidad": 1,
                "codigo_articulo": "ARTÍCULO 209",
                "delito": "ARTÍCULO 209. ACTOS SEXUALES CON MENOR DE 14 AÑOS",
                "fecha_descarga_dataset": "2026-11-06",
                "origen_datos": "Policía Nacional de Colombia - Datos Abiertos",
                "creado_en": "2026-11-06T21:50:00Z"
            }
        }
    )

class DelitoPaginationSchema(BaseModel):
    total: int = Field(..., description="Total de registros coincidentes con los filtros aplicados", example=16664)
    limit: int = Field(..., description="Límite de registros solicitados por página", example=50)
    offset: int = Field(..., description="Desplazamiento inicial de paginación", example=0)
    fuente: Optional[str] = Field("PostgreSQL (Supabase)", description="Fuente de provisión del dato", example="PostgreSQL (Supabase)")
    data: List[DelitoResponseSchema]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total": 181,
                "limit": 1,
                "offset": 0,
                "fuente": "PostgreSQL (Supabase)",
                "data": [
                    {
                        "departamento": "ATLÁNTICO",
                        "municipio": "Soledad",
                        "codigo_dane": "08758000",
                        "armas_medios": "NO REPORTADO",
                        "fecha_hecho": "2024-03-12",
                        "anio": 2024,
                        "mes": 3,
                        "nombre_mes": "Marzo",
                        "dia": 12,
                        "dia_semana": "Martes",
                        "trimestre": 1,
                        "semestre": 1,
                        "genero": "FEMENINO",
                        "grupo_etario": "ADULTOS",
                        "cantidad": 1,
                        "codigo_articulo": "ARTÍCULO 206",
                        "delito": "ARTÍCULO 206. ACTO SEXUAL VIOLENTO",
                        "fecha_descarga_dataset": "2026-11-06",
                        "origen_datos": "Policía Nacional de Colombia - Datos Abiertos"
                    }
                ]
            }
        }
    )

class OpcionesFiltrosSchema(BaseModel):
    total_registros: int = Field(..., example=16664)
    anios_disponibles: List[int] = Field(..., example=[2010, 2011, 2012, 2024, 2025, 2026])
    meses_disponibles: List[int] = Field(..., example=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    dias_semana: List[str] = Field(..., example=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    municipios: List[str] = Field(..., example=["Baranoa", "Barranquilla", "Galapa", "Malambo", "Puerto Colombia", "Soledad"])
    generos: List[str] = Field(..., example=["FEMENINO", "MASCULINO", "NO REPORTADO"])
    grupos_etarios: List[str] = Field(..., example=["ADOLESCENTES", "ADULTOS", "MENORES", "NO REPORTADO"])
    codigos_articulo: List[str] = Field(..., example=["ARTÍCULO 205", "ARTÍCULO 206", "ARTÍCULO 209", "ARTÍCULO 210"])
    armas_medios: List[str] = Field(..., example=["ARMA BLANCA / CORTOPUNZANTE", "ARMA DE FUEGO", "CONTUNDENTE", "NO REPORTADO"])
    fecha_minima: str = Field(..., example="2010-01-01")
    fecha_maxima: str = Field(..., example="2026-10-31")
    fecha_descarga_dataset: str = Field(..., example="2026-11-06")

class MetricaAnualSchema(BaseModel):
    anio: int = Field(..., example=2024)
    total_casos: int = Field(..., example=1180)
    total_victimas: int = Field(..., example=1185)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "anio": 2024,
                "total_casos": 1180,
                "total_victimas": 1185
            }
        }
    )

class MetricaMunicipioSchema(BaseModel):
    municipio: str = Field(..., example="Barranquilla")
    total_casos: int = Field(..., example=8778)
    porcentaje: float = Field(..., example=52.68)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "municipio": "Barranquilla",
                "total_casos": 8778,
                "porcentaje": 52.68
            }
        }
    )

class MetricaGeneroSchema(BaseModel):
    genero: str = Field(..., example="FEMENINO")
    total_casos: int = Field(..., example=14184)
    porcentaje: float = Field(..., example=85.12)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "genero": "FEMENINO",
                "total_casos": 14184,
                "porcentaje": 85.12
            }
        }
    )

class MetricaGrupoEtarioSchema(BaseModel):
    grupo_etario: str = Field(..., example="ADULTOS")
    total_casos: int = Field(..., example=11151)
    porcentaje: float = Field(..., example=66.92)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "grupo_etario": "ADULTOS",
                "total_casos": 11151,
                "porcentaje": 66.92
            }
        }
    )

class MetricaArticuloSchema(BaseModel):
    codigo_articulo: str = Field(..., example="ARTÍCULO 209")
    total_casos: int = Field(..., example=6840)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "codigo_articulo": "ARTÍCULO 209",
                "total_casos": 6840
            }
        }
    )
