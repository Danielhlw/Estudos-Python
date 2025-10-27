import pandas as pd
import plotly.express as px

# DataFrame base
dados = pd.DataFrame({
    "produto": ["A", "B", "C", "D"],
    "vendas": [150, 200, 300, 250],
    "lucro": [30, 70, 120, 90]
})

print(dados)

# Gráfico de barras
fig = px.bar(dados, x="produto", y="vendas", title="Vendas por Produto")
fig.show()

# Gráfico de linha
fig = px.line(dados, x="produto", y="lucro", title="Lucro por Produto", markers=True)
fig.show()

# Gráfico de dispersão
fig = px.scatter(dados, x="vendas", y="lucro", color="produto", size="lucro",
                 title="Correlação entre Vendas e Lucro")
fig.show()
