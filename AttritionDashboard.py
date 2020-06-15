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


app.layout = html.Div(children=[
    html.H1(children='IBM HR EDA Dashbord'),
    dcc.Graph(
        figure=go.Figure(
        data=[

        go.Bar(
            x=list(df.month.unique()),
            y=df.loc[df['location'] == 'Brn'].Talks,
            name='Brn',
            marker=go.bar.Marker(
                color='#da202a',
            )
        ),

        go.Bar(
            x=list(df.month.unique()),
            y=df.loc[df['location'] == 'Wrl'].Talks,
            name='Wrl',
            marker=go.bar.Marker(
                color='#2a2a2d',
            )
        ),

        layout=go.Layout(
        title='Conversation Required',
        showlegend=True,
        barmode='stack',
        xaxis = dict(tickvals=df.month.unique())
      )
            )
    

])

if __name__ == '__main__':
    app.run_server(debug=True)