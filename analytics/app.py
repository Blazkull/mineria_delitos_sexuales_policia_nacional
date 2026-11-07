import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_clean_data

# Configuración de Página
st.set_page_config(
    page_title="Minería de Datos - Delitos Sexuales en Atlántico",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .metric-card {
        background-color: #FFFFFF;
        padding: 1.2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-left: 5px solid #1E3A8A;
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E3A8A;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# Título y Contexto
st.title("🛡️ Análisis Exploratorio de Datos (EDA) — Delitos Sexuales en el Atlántico")
st.markdown("""
**Asignatura:** Minería de Datos | **Fuente Oficial:** Policía Nacional de Colombia — Portal de Datos Abiertos (`datos.gov.co`)  
**Periodo Analizado:** 2010 – 2026 | **Fecha de Descarga:** 2026-11-06 | **Población Objetivo:** Departamento del Atlántico (23 Municipios)
""")

# Carga de datos con caché
try:
    df_raw = load_clean_data()
    fuente_datos = df_raw.attrs.get("fuente", "PostgreSQL (Supabase) / CSV Limpio")
except Exception as e:
    st.error(f"Error cargando el dataset limpio: {e}")
    st.stop()

st.caption(f"📡 **Origen Activo:** {fuente_datos} | 🔒 **Estructura:** 19 dimensiones analíticas (Sin columna sintética `id`)")

# -------------------------------------------------------------
# SIDEBAR: FILTROS DINÁMICOS
# -------------------------------------------------------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Coat_of_arms_of_the_National_Police_of_Colombia.svg/200px-Coat_of_arms_of_the_National_Police_of_Colombia.svg.png", width=120)
st.sidebar.title("🎛️ Filtros de Análisis")

# Filtro de Año
min_anio = int(df_raw["anio"].min())
max_anio = int(df_raw["anio"].max())
rango_anios = st.sidebar.slider("Rango de Años:", min_value=min_anio, max_value=max_anio, value=(min_anio, max_anio))

# Filtro de Municipios
todos_municipios = sorted(df_raw["municipio"].unique().tolist())
municipios_seleccionados = st.sidebar.multiselect("Municipios:", options=todos_municipios, default=[])

# Filtro de Género
generos_disponibles = sorted(df_raw["genero"].unique().tolist())
generos_seleccionados = st.sidebar.multiselect("Género de la Víctima:", options=generos_disponibles, default=[])

# Filtro de Grupo Etario
grupos_disponibles = sorted(df_raw["grupo_etario"].unique().tolist())
grupos_seleccionados = st.sidebar.multiselect("Grupo Etario:", options=grupos_disponibles, default=[])

# Aplicación de filtros
df_filtrado = df_raw.copy()
df_filtrado = df_filtrado[(df_filtrado["anio"] >= rango_anios[0]) & (df_filtrado["anio"] <= rango_anios[1])]

if municipios_seleccionados:
    df_filtrado = df_filtrado[df_filtrado["municipio"].isin(municipios_seleccionados)]
if generos_seleccionados:
    df_filtrado = df_filtrado[df_filtrado["genero"].isin(generos_seleccionados)]
if grupos_seleccionados:
    df_filtrado = df_filtrado[df_filtrado["grupo_etario"].isin(grupos_seleccionados)]

# -------------------------------------------------------------
# TARJETAS DE KPIS PRINCIPALES
# -------------------------------------------------------------
total_casos = len(df_filtrado)
total_victimas = int(df_filtrado["cantidad"].sum())
muni_top = df_filtrado["municipio"].value_counts().index[0] if not df_filtrado.empty else "N/A"
delito_top = df_filtrado["codigo_articulo"].value_counts().index[0] if not df_filtrado.empty else "N/A"

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Casos Registrados</div>
        <div class="metric-value">{total_casos:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Víctimas Identificadas</div>
        <div class="metric-value">{total_victimas:,}</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Municipio Mayor Incidencia</div>
        <div class="metric-value" style="font-size: 1.4rem;">{muni_top}</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Artículo Penal Frecuente</div>
        <div class="metric-value" style="font-size: 1.4rem;">{delito_top}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# PESTAÑAS DE CONTENIDO ANALÍTICO
# -------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Tendencia Temporal",
    "👥 Análisis Demográfico",
    "🗺️ Distribución Geográfica",
    "⚖️ Tipología y Armas",
    "🔥 Matriz de Correlación / Calor",
    "📋 Explorador de Datos"
])

# -------------------------------------------------------------
# TAB 1: TENDENCIA TEMPORAL
# -------------------------------------------------------------
with tab1:
    st.subheader("Evolución Temporal de Delitos Sexuales en el Atlántico (2010 - 2026)")
    
    col_t1, col_t2 = st.columns([2, 1])
    with col_t1:
        serie_anual = df_filtrado.groupby("anio")["cantidad"].sum().reset_index()
        fig_anual = px.line(
            serie_anual, x="anio", y="cantidad",
            markers=True,
            title="Total de Casos por Año (2010 a 2026)",
            labels={"anio": "Año del Hecho", "cantidad": "Total Registros"},
            color_discrete_sequence=["#1E3A8A"]
        )
        fig_anual.update_layout(xaxis=dict(tickmode="linear", dtick=1))
        st.plotly_chart(fig_anual, use_container_width=True)
    
    with col_t2:
        serie_mes = df_filtrado.groupby("nombre_mes", as_index=False)["cantidad"].sum()
        orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        serie_mes["orden"] = serie_mes["nombre_mes"].map(lambda x: orden_meses.index(x) if x in orden_meses else 99)
        serie_mes = serie_mes.sort_values("orden")
        
        fig_mes = px.bar(
            serie_mes, x="nombre_mes", y="cantidad",
            title="Estacionalidad Mensual Acumulada",
            labels={"nombre_mes": "Mes", "cantidad": "Casos"},
            color="cantidad",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig_mes, use_container_width=True)

    st.markdown("---")
    st.subheader("Distribución por Día de la Semana")
    dias_orden = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    serie_dia = df_filtrado.groupby("dia_semana")["cantidad"].sum().reindex(dias_orden).reset_index()
    fig_dia = px.bar(
        serie_dia, x="dia_semana", y="cantidad",
        title="Frecuencia de Ocurrencia por Día de la Semana",
        labels={"dia_semana": "Día", "cantidad": "Casos"},
        color_discrete_sequence=["#2563EB"]
    )
    st.plotly_chart(fig_dia, use_container_width=True)

# -------------------------------------------------------------
# TAB 2: ANÁLISIS DEMOGRÁFICO
# -------------------------------------------------------------
with tab2:
    st.subheader("Perfil Demográfico de las Víctimas")
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        df_gen = df_filtrado["genero"].value_counts().reset_index()
        df_gen.columns = ["genero", "total"]
        fig_gen = px.pie(
            df_gen, names="genero", values="total",
            title="Distribución Porcentual por Género",
            color="genero",
            color_discrete_map={"FEMENINO": "#E11D48", "MASCULINO": "#0284C7", "NO REPORTADO": "#94A3B8"},
            hole=0.4
        )
        st.plotly_chart(fig_gen, use_container_width=True)

    with col_d2:
        df_grupo = df_filtrado["grupo_etario"].value_counts().reset_index()
        df_grupo.columns = ["grupo_etario", "total"]
        fig_grupo = px.bar(
            df_grupo, x="grupo_etario", y="total",
            title="Distribución por Grupo Etario",
            labels={"grupo_etario": "Grupo Etario", "total": "Total Víctimas"},
            color="grupo_etario",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        st.plotly_chart(fig_grupo, use_container_width=True)

    st.subheader("Cruce Bivariado: Género vs Grupo Etario")
    cruce_demografico = pd.crosstab(df_filtrado["grupo_etario"], df_filtrado["genero"], values=df_filtrado["cantidad"], aggfunc="sum").fillna(0)
    fig_cruce = px.bar(
        cruce_demografico.reset_index().melt(id_vars="grupo_etario"),
        x="grupo_etario", y="value", color="genero",
        barmode="group",
        title="Comparación Cruzada entre Grupo Etario y Género",
        labels={"value": "Cantidad de Víctimas", "grupo_etario": "Grupo Etario", "genero": "Género"}
    )
    st.plotly_chart(fig_cruce, use_container_width=True)

# -------------------------------------------------------------
# TAB 3: DISTRIBUCIÓN GEOGRÁFICA
# -------------------------------------------------------------
with tab3:
    st.subheader("Concentración Geográfica en los 23 Municipios del Atlántico")
    df_muni = df_filtrado["municipio"].value_counts().reset_index()
    df_muni.columns = ["municipio", "casos"]
    df_muni["porcentaje"] = (df_muni["casos"] / df_muni["casos"].sum()) * 100

    col_g1, col_g2 = st.columns([2, 1])
    with col_g1:
        fig_muni = px.bar(
            df_muni.head(15), x="casos", y="municipio",
            orientation="h",
            title="Top 15 Municipios con Mayor Número de Registros",
            labels={"casos": "Cantidad de Casos", "municipio": "Municipio"},
            color="casos",
            color_continuous_scale="Viridis"
        )
        fig_muni.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_muni, use_container_width=True)

    with col_g2:
        st.markdown("#### Tabla de Concentración Municipal")
        st.dataframe(df_muni.style.format({"porcentaje": "{:.2f}%"}), height=400, use_container_width=True, hide_index=True)

# -------------------------------------------------------------
# TAB 4: TIPOLOGÍA PENAL Y ARMAS
# -------------------------------------------------------------
with tab4:
    st.subheader("Tipificación Jurídica y Medios Empleados")
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        df_art = df_filtrado["codigo_articulo"].value_counts().head(10).reset_index()
        df_art.columns = ["articulo", "casos"]
        fig_art = px.bar(
            df_art, x="articulo", y="casos",
            title="Top 10 Artículos del Código Penal Más Frecuentes",
            labels={"articulo": "Artículo Penal", "casos": "Frecuencia"},
            color="casos",
            color_continuous_scale="Reds"
        )
        st.plotly_chart(fig_art, use_container_width=True)

    with col_p2:
        df_armas = df_filtrado["armas_medios"].value_counts().head(8).reset_index()
        df_armas.columns = ["armas_medios", "casos"]
        fig_armas = px.pie(
            df_armas, names="armas_medios", values="casos",
            title="Armas y Medios Empleados",
            hole=0.3
        )
        st.plotly_chart(fig_armas, use_container_width=True)

# -------------------------------------------------------------
# TAB 5: MATRIZ DE CALOR / ASOCIACIONES
# -------------------------------------------------------------
with tab5:
    st.subheader("Matriz de Calor: Municipio vs Grupo Etario")
    top_8_munis = df_filtrado["municipio"].value_counts().head(8).index.tolist()
    df_heat = df_filtrado[df_filtrado["municipio"].isin(top_8_munis)]
    pivot_heat = pd.crosstab(df_heat["municipio"], df_heat["grupo_etario"])

    fig_heat = px.imshow(
        pivot_heat,
        labels=dict(x="Grupo Etario", y="Municipio", color="Casos"),
        x=pivot_heat.columns,
        y=pivot_heat.index,
        color_continuous_scale="YlOrRd",
        text_auto=True,
        title="Intensidad de Casos por Municipio y Grupo Etario (Top 8 Municipios)"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

# -------------------------------------------------------------
# TAB 6: EXPLORADOR DE DATOS Y EXPORTACIÓN
# -------------------------------------------------------------
with tab6:
    st.subheader("Explorador Interactivo del Dataset Limpio")
    st.info(f"Mostrando {len(df_filtrado):,} registros resultantes de los filtros aplicados (Base completa inmutable: {len(df_raw):,}). Total columnas: {len(df_filtrado.columns)} atributos canónicos (Sin columna sintética `id`).")
    
    st.dataframe(df_filtrado.head(500), use_container_width=True, height=400, hide_index=True)
    
    csv_bytes = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar Datos Filtrados en CSV",
        data=csv_bytes,
        file_name="delitos_sexuales_atlantico_filtrado.csv",
        mime="text/csv"
    )

st.sidebar.markdown("---")
st.sidebar.info("💡 **Nota Académica:** Para el artículo científico en Word, capture las pantallas de este tablero numerándolas secuencialmente con título y fuente según normas APA.")

