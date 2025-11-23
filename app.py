import falcon
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

# Dados importados
falcon_data = falcon.df

# Filtro lateral
filtro = st.sidebar.selectbox("Tipo do Documento", falcon_data['TipoDoDocumento'].unique())

# Filtrar dados conforme escolha
filtrado = falcon_data[falcon_data['TipoDoDocumento'] == filtro]

# Layout
col1, col2 = st.columns(2)

# ===========================
# GRÁFICO 1 – CONTAGEM POR STATUS
# ===========================
contagem_status = filtrado['Status'].value_counts().reset_index()
contagem_status.columns = ['Status', 'Quantidade']

grafico_status = px.bar(
    contagem_status,
    x="Status",
    y="Quantidade",
    title="Contagem por Status",
    text="Quantidade",
    color_discrete_sequence=["#853def"]  # cor das barras
)

# --- estilização do texto ---
grafico_status.update_layout(
    title_font_color="white",
    xaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    ),
    yaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    )
)

# --- estilização do texto ---
grafico_status.update_layout(
    title_font_color="white",
    xaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    ),
    yaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    )
)

# --- estilização do texto ---
grafico_status.update_layout(
    title_font_color="white",
    xaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    ),
    yaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    )
)

# --- deixar rótulos (text) em negrito ---
grafico_status.update_traces(
    textfont=dict(
        size=14,
        color="white",
        family="Arial"
    )
)

# aplicar <b>...</b> aos valores dos rótulos
grafico_status.for_each_trace(
    lambda t: t.update(text=[f"<b>{int(float(v))}</b>" for v in t.text])
)

col1.plotly_chart(grafico_status, use_container_width=True)

# ===========================
# GRÁFICO 2 – CONTAGEM POR FILA
# ===========================
contagem_fila = filtrado['Fila'].value_counts().reset_index()
contagem_fila.columns = ['Fila', 'Quantidade']

grafico_fila = px.bar(
    contagem_fila,
    x="Fila",
    y="Quantidade",
    title="Contagem por Fila",
    text="Quantidade",
    color_discrete_sequence=["#853def"]  # cor das barras
)

# --- estilização do texto ---
grafico_fila.update_layout(
    title_font_color="white",
    xaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    ),
    yaxis=dict(
        title_font_color="white",
        tickfont=dict(color="white")
    )
)

# --- deixar rótulos (text) em negrito ---
grafico_fila.update_traces(
    textfont=dict(
        size=14,
        color="white",
        family="Arial"
    )
)

# aplicar <b>...</b> aos valores dos rótulos
grafico_fila.for_each_trace(
    lambda t: t.update(text=[f"<b>{int(float(v))}</b>" for v in t.text])
)

col2.plotly_chart(grafico_fila, use_container_width=True)
