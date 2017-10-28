# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import adjustText
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import matplotlib as mpl

data = pd.read_csv('eu_unemployment.csv')

text = []
for i, txt in enumerate(data['Country']):
    text.append(txt + '<br>'
                'Unemployment Rate ' + str(data['Unemployment'][i]) + '%<br>'
                'Youth Unemployment Rate ' + str(data['Youth'][i]) + '%<br>'
                'Avg Yearly Sunshine: ' + str(int(data['Sunshine'][i])) + ' hours<br>')


trace = go.Scatter(
    y = data['Unemployment'],
    x = data['Sunshine'],
    mode = 'markers',
    marker = dict(
        color = data['Youth'],
        colorscale = 'RdBu',
        line = dict(width = 1),
        showscale=True,
        size = 15,
        opacity = 0.8,
        colorbar = dict(
            #titleside = 'top',
            tickvals = [min(data['Youth']),max(data['Youth'])],
            ticktext = ['0%','45%'],
            ticks = 'outside',
            lenmode = 'fraction',
            len = 0.5,
            yanchor = 'top',
            tickfont=dict(
            size=12,
            color='#000'
        	),
        )
    ),
    showlegend= False,
    text = text
)

z = np.polyfit(data['Sunshine'],data['Unemployment'],1)

trend = go.Scatter(
    y = data['Sunshine']*z[0] + z[1],
    x = data['Sunshine'],
    hoverinfo='none',
    mode = 'lines',
    showlegend= False)


data = [trace,trend]
    
layout = go.Layout(
    title='Unemployment vs Sunshine in the EU',
    xaxis=dict(
        title='Average Yearly Sunshine Hours'),
    yaxis=dict(
        title='Unemployment Rate (%)'),
    hovermode='closest',
    orientation="h",
    font=dict(size=14),
    annotations = [
    	dict(
      		showarrow = False,
	      	xref = 'paper',
	      	yref = 'paper',
	        x = 1.105,
	        y = 0.57,
	        text = "Youth <br> Unemployment",
	        textangle = 0,
        	font=dict(
            size=12,
            color='#000'
        	))]
    )

fig = go.Figure(data=data, layout=layout)
py.plot(fig)
