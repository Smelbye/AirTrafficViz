import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from jupyter_dash import JupyterDash
import pandas as pd

data = pd.read_excel("NorwayFlights.xlsx")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Norwegian Airport Passenger Traffic 2022", style={'textAlign': 'center'}),
            html.P("A dashboard for visualizing total passenger traffic in 2022 at the four biggest airports in Norway.", style={'textAlign': 'center'}),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Select Airport", style={'textAlign': 'center'}),
            dcc.Dropdown(
                id="airport-dropdown",
                options=[
                    {"label": "Oslo Gardermoen", "value": "Oslo Gardermoen"},
                    {"label": "Stavanger Sola", "value": "Stavanger Sola"},
                    {"label": "Bergen Flesland", "value": "Bergen Flesland"},
                    {"label": "Trondheim Værnes", "value": "Trondheim Værnes"}
                ],
                value=["Oslo Gardermoen", "Stavanger Sola", "Bergen Flesland", "Trondheim Værnes"],
                multi=True,
                clearable=False,
                style={"width": "100%"}
            ),
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="airport-graph")
        ]),
    ]),
])

# Callback
@app.callback(
    Output("airport-graph", "figure"),
    [Input("airport-dropdown", "value")]
)
def update_graph(airports):
    fig = px.line(
        data,
        x="Month 2022",
        y=airports,
        title="Monthly Passenger Traffic at Selected Airports",
        labels={"Month 2022": "Month", "value": "Number of Passengers"},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            title="Month",
            showgrid=True,
            gridcolor='rgba(200, 200, 200, 0.2)',
        ),
        yaxis=dict(
            title="Number of Passengers",
            showgrid=True,
            gridcolor='rgba(200, 200, 200, 0.2)',
        )
    )
    return fig

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)
