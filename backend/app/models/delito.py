from sqlalchemy import Column, Integer, SmallInteger, String, Text, Date, DateTime, func, Index
from backend.app.core.database import Base

class DelitoSexualAtlantico(Base):
    __tablename__ = "delitos_sexuales_atlantico"

    # Columnas del dataset limpio sin columna id
    departamento = Column(String(50), nullable=False, default="ATLÁNTICO", index=True)
    municipio = Column(String(100), primary_key=True, nullable=False, index=True)
    codigo_dane = Column(String(20), nullable=False, index=True)
    armas_medios = Column(String(100), nullable=False)
    fecha_hecho = Column(Date, primary_key=True, nullable=False, index=True)
    
    # Atributos temporales derivados para analítica
    anio = Column(SmallInteger, primary_key=True, nullable=False, index=True)
    mes = Column(SmallInteger, nullable=False, index=True)
    nombre_mes = Column(String(20), nullable=False)
    dia = Column(SmallInteger, nullable=False)
    dia_semana = Column(String(20), nullable=False)
    trimestre = Column(SmallInteger, nullable=False)
    semestre = Column(SmallInteger, nullable=False)
    
    # Variables demográficas
    genero = Column(String(30), primary_key=True, nullable=False, index=True)
    grupo_etario = Column(String(30), primary_key=True, nullable=False, index=True)
    cantidad = Column(Integer, primary_key=True, nullable=False, default=1)
    
    # Tipificación jurídica
    codigo_articulo = Column(String(30), nullable=False, index=True)
    delito = Column(Text, primary_key=True, nullable=False)
    
    # Auditoría de origen
    fecha_descarga_dataset = Column(Date, nullable=False, default="2026-11-06")
    origen_datos = Column(String(150), nullable=False, default="Policía Nacional de Colombia - Datos Abiertos")
    creado_en = Column(DateTime(timezone=True), primary_key=True, server_default=func.now(), nullable=False)

    __table_args__ = (
        Index("idx_delitos_anio_municipio", "anio", "municipio"),
        Index("idx_delitos_anio_articulo", "anio", "codigo_articulo"),
        Index("idx_delitos_genero_grupo", "genero", "grupo_etario"),
    )
