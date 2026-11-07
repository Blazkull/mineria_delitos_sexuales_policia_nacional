import os
from typing import Optional, List, Dict, Any
from datetime import date
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, asc, text
from backend.app.models.delito import DelitoSexualAtlantico
from backend.app.core.config import settings

class DelitoService:
    @staticmethod
    def _get_csv_fallback_df() -> Optional[pd.DataFrame]:
        possible_paths = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", settings.DATASET_CLEAN_PATH)),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "data_set", "delitos_sexuales_atlantico_limpio.csv")),
            "docs/data_set/delitos_sexuales_atlantico_limpio.csv"
        ]
        for p in possible_paths:
            if os.path.exists(p):
                df = pd.read_csv(p)
                if "id" in df.columns:
                    df = df.drop(columns=["id"])
                return df
        return None

    @staticmethod
    def get_delitos(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        fecha_desde: Optional[date] = None,
        fecha_hasta: Optional[date] = None,
        anio: Optional[int] = None,
        anio_desde: Optional[int] = None,
        anio_hasta: Optional[int] = None,
        mes: Optional[int] = None,
        trimestre: Optional[int] = None,
        semestre: Optional[int] = None,
        dia_semana: Optional[str] = None,
        municipio: Optional[str] = None,
        codigo_dane: Optional[str] = None,
        armas_medios: Optional[str] = None,
        genero: Optional[str] = None,
        grupo_etario: Optional[str] = None,
        codigo_articulo: Optional[str] = None,
        delito_buscar: Optional[str] = None,
        cantidad_min: Optional[int] = None,
        cantidad_max: Optional[int] = None,
        ordenar_por: str = "fecha_hecho",
        orden_dir: str = "desc"
    ) -> Dict[str, Any]:
        """
        Consulta flexible con múltiples filtros y paginación (sin columna id).
        """
        usar_db = False
        try:
            total_db = db.query(func.count(DelitoSexualAtlantico.municipio)).scalar()
            if total_db and total_db > 0:
                usar_db = True
        except Exception:
            usar_db = False

        if usar_db:
            query = db.query(DelitoSexualAtlantico)
            
            # Filtros temporales
            if fecha_desde:
                query = query.filter(DelitoSexualAtlantico.fecha_hecho >= fecha_desde)
            if fecha_hasta:
                query = query.filter(DelitoSexualAtlantico.fecha_hecho <= fecha_hasta)
            if anio:
                query = query.filter(DelitoSexualAtlantico.anio == anio)
            if anio_desde:
                query = query.filter(DelitoSexualAtlantico.anio >= anio_desde)
            if anio_hasta:
                query = query.filter(DelitoSexualAtlantico.anio <= anio_hasta)
            if mes:
                query = query.filter(DelitoSexualAtlantico.mes == mes)
            if trimestre:
                query = query.filter(DelitoSexualAtlantico.trimestre == trimestre)
            if semestre:
                query = query.filter(DelitoSexualAtlantico.semestre == semestre)
            if dia_semana:
                query = query.filter(func.lower(DelitoSexualAtlantico.dia_semana) == dia_semana.lower().strip())

            # Filtros geográficos y demográficos
            if municipio:
                query = query.filter(func.lower(DelitoSexualAtlantico.municipio) == municipio.lower().strip())
            if codigo_dane:
                query = query.filter(DelitoSexualAtlantico.codigo_dane == str(codigo_dane).strip().zfill(8))
            if armas_medios:
                query = query.filter(func.lower(DelitoSexualAtlantico.armas_medios).contains(armas_medios.lower().strip()))
            if genero:
                query = query.filter(DelitoSexualAtlantico.genero == genero.upper().strip())
            if grupo_etario:
                query = query.filter(DelitoSexualAtlantico.grupo_etario == grupo_etario.upper().strip())

            # Filtros jurídicos y búsqueda de texto
            if codigo_articulo:
                query = query.filter(func.upper(DelitoSexualAtlantico.codigo_articulo).contains(codigo_articulo.upper().strip()))
            if delito_buscar:
                query = query.filter(func.lower(DelitoSexualAtlantico.delito).contains(delito_buscar.lower().strip()))

            # Filtro de cantidad
            if cantidad_min is not None:
                query = query.filter(DelitoSexualAtlantico.cantidad >= cantidad_min)
            if cantidad_max is not None:
                query = query.filter(DelitoSexualAtlantico.cantidad <= cantidad_max)

            total = query.count()

            # Ordenamiento
            campo_orden = getattr(DelitoSexualAtlantico, ordenar_por, DelitoSexualAtlantico.fecha_hecho)
            if orden_dir.lower() == "asc":
                query = query.order_by(asc(campo_orden))
            else:
                query = query.order_by(desc(campo_orden))

            data = query.offset(skip).limit(limit).all()
            return {
                "total": total,
                "limit": limit,
                "offset": skip,
                "fuente": "PostgreSQL (Supabase)",
                "data": data
            }

        # Fallback a pandas si DB no tiene registros
        df = DelitoService._get_csv_fallback_df()
        if df is None:
            return {"total": 0, "limit": limit, "offset": skip, "fuente": "None", "data": []}

        if fecha_desde:
            df = df[df["fecha_hecho"] >= str(fecha_desde)]
        if fecha_hasta:
            df = df[df["fecha_hecho"] <= str(fecha_hasta)]
        if anio:
            df = df[df["anio"] == anio]
        if anio_desde:
            df = df[df["anio"] >= anio_desde]
        if anio_hasta:
            df = df[df["anio"] <= anio_hasta]
        if mes:
            df = df[df["mes"] == mes]
        if trimestre:
            df = df[df["trimestre"] == trimestre]
        if semestre:
            df = df[df["semestre"] == semestre]
        if dia_semana:
            df = df[df["dia_semana"].str.lower() == dia_semana.lower().strip()]
        if municipio:
            df = df[df["municipio"].str.lower() == municipio.lower().strip()]
        if codigo_dane:
            df = df[df["codigo_dane"].astype(str) == str(codigo_dane).strip().zfill(8)]
        if armas_medios:
            df = df[df["armas_medios"].str.lower().str.contains(armas_medios.lower().strip(), na=False)]
        if genero:
            df = df[df["genero"] == genero.upper().strip()]
        if grupo_etario:
            df = df[df["grupo_etario"] == grupo_etario.upper().strip()]
        if codigo_articulo:
            df = df[df["codigo_articulo"].str.upper().str.contains(codigo_articulo.upper().strip(), na=False)]
        if delito_buscar:
            df = df[df["delito"].str.lower().str.contains(delito_buscar.lower().strip(), na=False)]
        if cantidad_min is not None:
            df = df[df["cantidad"] >= cantidad_min]
        if cantidad_max is not None:
            df = df[df["cantidad"] <= cantidad_max]

        total = len(df)
        col_sort = ordenar_por if ordenar_por in df.columns else "fecha_hecho"
        df = df.sort_values(by=col_sort, ascending=(orden_dir.lower() == "asc"))
        paged_df = df.iloc[skip:skip+limit]

        return {
            "total": total,
            "limit": limit,
            "offset": skip,
            "fuente": "CSV Limpio (Fallback de Alta Disponibilidad)",
            "data": paged_df.to_dict(orient="records")
        }

    @staticmethod
    def get_opciones_filtros(db: Session) -> Dict[str, Any]:
        """Retorna todas las opciones disponibles en el dataset para selectores."""
        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            return {
                "total_registros": int(len(df)),
                "anios_disponibles": sorted([int(x) for x in df["anio"].dropna().unique()]),
                "meses_disponibles": sorted([int(x) for x in df["mes"].dropna().unique()]),
                "dias_semana": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                "municipios": sorted(df["municipio"].dropna().unique().tolist()),
                "generos": sorted(df["genero"].dropna().unique().tolist()),
                "grupos_etarios": sorted(df["grupo_etario"].dropna().unique().tolist()),
                "codigos_articulo": sorted(df["codigo_articulo"].dropna().unique().tolist()),
                "armas_medios": sorted(df["armas_medios"].dropna().unique().tolist()),
                "fecha_minima": str(df["fecha_hecho"].min()),
                "fecha_maxima": str(df["fecha_hecho"].max()),
                "fecha_descarga_dataset": "2026-11-06"
            }
        return {}

    @staticmethod
    def get_powerbi_full_dataset(db: Session) -> List[Dict[str, Any]]:
        """Retorna el dataset completo de los 16,664 registros sin columna id para Power BI Desktop."""
        try:
            from backend.app.core.database import engine
            with engine.connect() as conn:
                result = conn.execute(text("SELECT * FROM delitos_sexuales_atlantico ORDER BY fecha_hecho ASC"))
                rows = result.mappings().all()
                if rows and len(rows) > 0:
                    data = []
                    for r in rows:
                        d = dict(r)
                        if "id" in d:
                            del d["id"]
                        if "creado_en" in d:
                            del d["creado_en"]
                        if hasattr(d.get("fecha_hecho"), "strftime"):
                            d["fecha_hecho"] = d["fecha_hecho"].strftime("%Y-%m-%d")
                        if hasattr(d.get("fecha_descarga_dataset"), "strftime"):
                            d["fecha_descarga_dataset"] = d["fecha_descarga_dataset"].strftime("%Y-%m-%d")
                        data.append(d)
                    return data
        except Exception:
            pass

        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            if "id" in df.columns:
                df = df.drop(columns=["id"])
            return df.to_dict(orient="records")
        return []

    @staticmethod
    def get_resumen_anual(db: Session) -> List[Dict[str, Any]]:
        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            res = df.groupby("anio").agg(
                total_casos=("cantidad", "count"),
                total_victimas=("cantidad", "sum")
            ).reset_index()
            return res.to_dict(orient="records")
        return []

    @staticmethod
    def get_resumen_municipios(db: Session, limit: int = 25) -> List[Dict[str, Any]]:
        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            total_global = len(df)
            res = df["municipio"].value_counts().head(limit).reset_index()
            res.columns = ["municipio", "total_casos"]
            res["porcentaje"] = (res["total_casos"] / total_global * 100).round(2)
            return res.to_dict(orient="records")
        return []

    @staticmethod
    def get_resumen_genero(db: Session) -> List[Dict[str, Any]]:
        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            total_global = len(df)
            res = df["genero"].value_counts().reset_index()
            res.columns = ["genero", "total_casos"]
            res["porcentaje"] = (res["total_casos"] / total_global * 100).round(2)
            return res.to_dict(orient="records")
        return []

    @staticmethod
    def get_resumen_grupo_etario(db: Session) -> List[Dict[str, Any]]:
        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            total_global = len(df)
            res = df["grupo_etario"].value_counts().reset_index()
            res.columns = ["grupo_etario", "total_casos"]
            res["porcentaje"] = (res["total_casos"] / total_global * 100).round(2)
            return res.to_dict(orient="records")
        return []

    @staticmethod
    def get_resumen_articulos(db: Session, limit: int = 15) -> List[Dict[str, Any]]:
        df = DelitoService._get_csv_fallback_df()
        if df is not None:
            res = df["codigo_articulo"].value_counts().head(limit).reset_index()
            res.columns = ["codigo_articulo", "total_casos"]
            return res.to_dict(orient="records")
        return []
