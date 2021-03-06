# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from queries import fig1, fig2, fig3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(
children=[
    html.H1(children='''
        Prototype Dashboard Projet
    ''', style={'textAlign': 'center',
                'color' :'black'}),

    html.Div(children='''
        This research has made use of the NASA Exoplanet Archive,
        which is operated by the California Institute of Technology, 
        under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program..
    ''', style={'textAlign': 'center', 'color' :'black'}),

    dcc.Graph(
        id='graph1',
        figure=fig1
    ),

    dcc.Graph(
        id='graph2',
        figure=fig2
    ),

    dcc.Graph(
        id='graph3',
        figure=fig3
    )
])

if __name__ == '__main__':

    app.run_server(debug=True)