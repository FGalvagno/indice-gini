import dash
from dash import html, dcc, Input, Output
import requests
import pandas as pd
import plotly.express as px
from gini import lib
# Inicializamos la instancia de Dash
app = dash.Dash(__name__)

# Interactuamos con la restAPI para obtener los datos del índice GINI
def fetch_gini_data(country_code):
    api_url = f'https://api.worldbank.org/v2/en/country/{country_code}/indicator/SI.POV.GINI?format=json&per_page=1000'
    response = requests.get(api_url)
    if response.status_code != 200 or len(response.json()) < 2:
        return pd.DataFrame(columns=['date', 'value'])
    data = response.json()[1]
    df = pd.DataFrame(data)
    df = df[['date', 'value']].dropna()
    df['date'] = df['date'].astype(int)
    df['value'] = df['value'].astype(float)
    return df.sort_values('date')

# Data inicial de la app
initial_country = 'ARG'
df = fetch_gini_data(initial_country)

# Layout
app.layout = html.Div([
    html.H1("Índice GINI a lo largo del tiempo", style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(id='gini-graph', style={'flex': '3', 'height': '100%'}),

        html.Div([
            html.Label("Seleccionar País:"),
            dcc.Dropdown(
                id='country-selector',
                options=[
                    {'label': 'Argentina', 'value': 'ARG'},
                    {'label': 'Brazil', 'value': 'BR'},
                    {'label': 'India', 'value': 'IN'},
                    {'label': 'Estados Unidos', 'value': 'US'},
                    {'label': 'Alemania', 'value': 'DE'}
                ],
                value='ARG'
            )
        ], style={'flex': '1', 'padding': '20px'})
    ], style={'display': 'flex', 'height': '80vh'}),

    html.Div([
        html.Label("Rango de años:"),
        dcc.RangeSlider(
            id='year-slider',
            min=df['date'].min() if not df.empty else 2000,
            max=df['date'].max() if not df.empty else 2020,
            value=[df['date'].min() if not df.empty else 2000, df['date'].max() if not df.empty else 2020],
            marks={str(year): str(year) for year in range(1960, 2023, 5)},
            step=1
        )
    ], style={'padding': '20px'})
])

# Callback para los años y pais
@app.callback(
    Output('year-slider', 'min'),
    Output('year-slider', 'max'),
    Output('year-slider', 'value'),
    Input('country-selector', 'value')
)
def update_slider(country_code):
    df = fetch_gini_data(country_code)
    if df.empty:
        return 2000, 2020, [2000, 2020]
    return df['date'].min(), df['date'].max(), [df['date'].min(), df['date'].max()]

# Callback para actualizar el gráfico
@app.callback(
    Output('gini-graph', 'figure'),
    Input('country-selector', 'value'),
    Input('year-slider', 'value')
)
def update_graph(country_code, year_range):
    df = fetch_gini_data(country_code)
    if df.empty:
        fig = px.line(title="Sin datos disponibles")
        return fig

    filtered_df = df[(df['date'] >= year_range[0]) & (df['date'] <= year_range[1])]
    filtered_df['value'] = df['value'].apply(lib.convert_and_increment)
    fig = px.line(
        filtered_df,
        x='date',
        y='value',
        title=f'Índice de GINI para {country_code.upper()}',
        labels={'date': 'Año', 'value': 'Índice de GINI'}
    )

    return fig

# Corremos la app
if __name__ == '__main__':
    app.run(debug=True)
