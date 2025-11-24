import falcon
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

# Dados importados
falcon_data = falcon.df

# Filtro lateral
filtro = st.sidebar.selectbox(
    "Tipo do Documento", falcon_data['TipoDoDocumento'].unique())

# Filtrar dados conforme escolha
filtrado = falcon_data[falcon_data['TipoDoDocumento'] == filtro]

# ===================================================
# TABELAS
# ===================================================

# Definir colunas lado a lado para tabelas ( layout pagina )
col_t1, col_t2 = st.columns(2)

with col_t1:
    st.subheader("Tabela - Status")
    contagem_status = filtrado['Status'].value_counts().reset_index()
    contagem_status.columns = ['Status', 'Quantidade']
    contagem_status['Percentual'] = (
        contagem_status['Quantidade'] / contagem_status['Quantidade'].sum()) * 100
    contagem_status['Percentual'] = contagem_status['Percentual'].round(2)
    st.dataframe(contagem_status)

with col_t2:
    st.subheader("Tabela - Fila")
    contagem_fila = filtrado['Fila'].value_counts().reset_index()
    contagem_fila.columns = ['Fila', 'Quantidade']
    contagem_fila['Percentual'] = (
        contagem_fila['Quantidade'] / contagem_fila['Quantidade'].sum()) * 100
    contagem_fila['Percentual'] = contagem_fila['Percentual'].round(2)
    st.dataframe(contagem_fila)

# Layout para gráficos lado a lado
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

# Estilização do texto
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

# Deixar rótulos (text) em negrito
grafico_status.update_traces(
    textfont=dict(
        size=14,
        color="white",
        family="Arial"
    )
)

# Aplicar <b>...</b> aos valores dos rótulos
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

# Estilização do texto
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

# Deixar rótulos (text) em negrito
grafico_fila.update_traces(
    textfont=dict(
        size=14,
        color="white",
        family="Arial"
    )
)

# Aplicar <b>...</b> aos valores dos rótulos
grafico_fila.for_each_trace(
    lambda t: t.update(text=[f"<b>{int(float(v))}</b>" for v in t.text])
)

col2.plotly_chart(grafico_fila, use_container_width=True)


st.subheader("Tabela")
falcon_data
