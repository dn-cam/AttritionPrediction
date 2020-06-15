import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()


def readData():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    return df;

df = readData()

trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

app.layout = html.Div(children=[
    html.H1(children='IBM HR EDA Dashbord'),
    dcc.Graph(
    id='example',    
    figure={
        'data': [
            {'x': df.JobSatisfaction, 'y': df.Attrition, 'type': 'bar', 'name': 'JobSatisfaction', 'barmode':'group'},
        ],
        'layout': {
            'title': 'Job Satisfaction vs Attrition'
        }
    }
)
])

if __name__ == '__main__':
    app.run_server(debug=True)