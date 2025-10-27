import pandas as pd
import plotly.express as px

# DataFrame base
dados = pd.DataFrame({
    "produto": ["A", "B", "C", "D", "E"],
    "vendas": [150, 200, 300, 250, 400],
    "lucro": [30, 70, 120, 90, 160],
    "categoria": ["Eletrônicos", "Roupas", "Roupas", "Alimentos", "Eletrônicos"]
})

# Gráfico com cores personalizadas
fig = px.bar(
    dados,
    x="produto",
    y="vendas",
    color="categoria",
    title="Vendas por Produto e Categoria",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
fig.show()

# Gráfico com rótulos e layout customizado
fig = px.bar(
    dados,
    x="produto",
    y="lucro",
    text="lucro",
    color="categoria",
    title="Lucro por Produto"
)
fig.update_traces(textposition="outside")
fig.update_layout(
    title_font=dict(size=22, color="darkblue"),
    xaxis_title="Produto",
    yaxis_title="Lucro (R$)",
    plot_bgcolor="rgba(240,240,240,0.5)",
    paper_bgcolor="white",
    title_x=0.5
)
fig.show()

# Tema escuro e estilo de linha
fig = px.line(
    dados,
    x="produto",
    y="vendas",
    color="categoria",
    title="Tendência de Vendas por Categoria",
    template="plotly_dark"
)
fig.show()
