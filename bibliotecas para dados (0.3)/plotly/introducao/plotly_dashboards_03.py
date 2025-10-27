import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

dados = pd.DataFrame({
    "mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "vendas": [150, 200, 300, 250, 400, 380],
    "lucro": [30, 70, 120, 90, 160, 150]
})

# Subplots lado a lado
fig = make_subplots(rows=1, cols=2, subplot_titles=("Vendas", "Lucro"))
fig.add_trace(go.Bar(x=dados["mês"], y=dados["vendas"], name="Vendas", marker_color="royalblue"), row=1, col=1)
fig.add_trace(go.Scatter(x=dados["mês"], y=dados["lucro"], name="Lucro", mode="lines+markers", line=dict(color="green")), row=1, col=2)
fig.update_layout(title_text="Painel de Indicadores Mensais", title_x=0.5)
fig.show()

# Barras + linha (eixo duplo)
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Bar(x=dados["mês"], y=dados["vendas"], name="Vendas", marker_color="skyblue"), secondary_y=False)
fig.add_trace(go.Scatter(x=dados["mês"], y=dados["lucro"], name="Lucro", mode="lines+markers", line=dict(color="darkgreen")), secondary_y=True)
fig.update_layout(title="Vendas x Lucro (Eixo Duplo)", title_x=0.5)
fig.update_xaxes(title_text="Mês")
fig.update_yaxes(title_text="Vendas (R$)", secondary_y=False)
fig.update_yaxes(title_text="Lucro (R$)", secondary_y=True)
fig.show()
