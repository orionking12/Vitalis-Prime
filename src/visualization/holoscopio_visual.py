import time
import requests
import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# =====================================================================
# VITALIS-PRIME: HOLOSCOPE 3D
# ARCHITECT: JORGE HUMBERTO DAVALOS GONZALEZ
# =====================================================================

def run_holoscope():
    URL = "http://127.0.0.1:5000/api/v1/sistema/estado"
    app = dash.Dash(__name__, title="Holoscopio Vitalis-Prime")

    app.layout = html.Div(style={'backgroundColor': '#050505', 'color': '#00ffcc', 'fontFamily': 'monospace', 'height': '100vh'}, children=[
        html.H1("VITALIS-PRIME // HOLOSCOPIO 3D", style={'textAlign': 'center', 'padding': '10px'}),
        html.Div(id='hud', style={'position': 'absolute', 'top': '80px', 'left': '20px', 'zIndex': '10', 'background': 'rgba(0,10,10,0.8)', 'padding': '15px', 'border': '1px solid #00ffcc'}),
        dcc.Graph(id='graph', style={'height': '80vh'}),
        dcc.Interval(id='timer', interval=1000)
    ])

    mx, my = np.meshgrid(np.linspace(-5, 5, 40), np.linspace(-5, 5, 40))

    @app.callback([Output('graph', 'figure'), Output('hud', 'children')], [Input('timer', 'n_intervals')])
    def update(n):
        try:
            r = requests.get(URL, timeout=1).json()
            m = r['metricas_motor_hibrido']
            at_g, at_r, loss, lotes = m['atencion_promedio_gen'], m['atencion_promedio_rf'], m['loss_actual'], m['lotes_procesados']
        except:
            at_g, at_r, loss, lotes = 0.5, 0.5, 0.05, 0

        pos_g, pos_r = np.array([0, 3, 2]), np.array([0, -3, 2])
        pos_p = pos_r + (pos_g - pos_r) * at_g
        z_mesh = np.sin(mx + time.time()) * np.cos(my + time.time()) * (loss * 2)

        fig = go.Figure(data=[
            go.Scatter3d(x=[pos_g[0]], y=[pos_g[1]], z=[pos_g[2]], name="GEN", marker=dict(size=10, color='#00aaff')),
            go.Scatter3d(x=[pos_r[0]], y=[pos_r[1]], z=[pos_r[2]], name="RF", marker=dict(size=10, color='#ffaa00')),
            go.Scatter3d(x=[pos_p[0]], y=[pos_p[1]], z=[pos_p[2]], name="ESTADO", marker=dict(size=8, color='white', symbol='cross')),
            go.Surface(x=mx, y=my, z=z_mesh, colorscale='GnBu', opacity=0.5, showscale=False)
        ])
        fig.update_layout(scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), bgcolor='#050505'), margin=dict(l=0,r=0,b=0,t=0), paper_bgcolor='#050505')

        hud = [html.P(f"LOTES: {lotes}"), html.P(f"ATN NEURONAL: {at_g*100:.1f}%"), html.P(f"ATN CLÁSICA: {at_r*100:.1f}%"), html.P(f"LOSS: {loss:.4f}", style={'color': 'red' if loss > 0.8 else '#00ffcc'})]
        return fig, hud

    print("🌌 Holoscopio en http://127.0.0.1:8050")
    app.run_server(port=8050, debug=False)

if __name__ == "__main__":
    run_holoscope()
