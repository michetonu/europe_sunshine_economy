# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import adjustText
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import matplotlib as mpl

data = pd.read_csv('sunshine_vs_gdp.csv')

text = []
for i, txt in enumerate(data['Country']):
    text.append(txt + '<br>'
                'GDP per capita: ' + str(data['GDP'][i]) + ' $<br>'
                'Total GDP: ' + str(int(data['GDP_tot'][i])) + ' B$<br>'
                'Avg Yearly Temperature: ' + str(int(data['Temperature'][i])) + 'º<br>'
                'Avg Yearly Sunshine: ' + str(int(data['Sunshine'][i])) + ' hours<br>')


trace = go.Scatter(
    y = data['GDP'],
    x = data['Sunshine'],
    mode = 'markers',
    marker = dict(
        color = data['Temperature'],
        colorscale = 'RdBu',
        line = dict(width = 1,
        	color = 'black'),
        showscale=True,
        size = data['GDP_tot']**(0.35)*3,
        colorbar = dict(
            #titleside = 'top',
            tickvals = [min(data['Temperature'])+0.5,max(data['Temperature'])-0.5],
            ticktext = ['Cold (0º)','Hot (20º)'],
            ticks = 'outside',
            lenmode = 'fraction',
            len = 0.5,
            yanchor = 'top',
            tickfont=dict(
            family='sans-serif',
            size=10,
            color='#000'
        	),
        )
    ),
    showlegend= False,
    text = text
)

z = np.polyfit(data['Sunshine'],data['GDP'],1)

trend = go.Scatter(
    y = data['Sunshine']*z[0] + z[1],
    x = data['Sunshine'],
    hoverinfo='none',
    mode = 'lines',
    showlegend= False)

datapoint1 = min(data['GDP_tot'])
legend1 = go.Scatter(
    y = datapoint1,
    x = [1500],
    name = '    1B$',
    visible = 'legendonly',
    mode = 'markers',
    marker = dict(
        color = 'white',
        line = dict(width = 2),
        size = np.sqrt(datapoint1)+5,
    ),
    text = text
)
datapoint2 = (max(data['GDP_tot'])-min(data['GDP_tot']))/2
legend2 = go.Scatter(
    y = datapoint2,
    x = [1500],
    name = '    1000B$',
    visible = 'legendonly',
    mode = 'markers',
    marker = dict(
        color = 'white',
        line = dict(width = 2),
        size = np.sqrt(datapoint2)+150/datapoint2,
    ),
    text = text
)
datapoint3 = max(data['GDP_tot'])
legend3 = go.Scatter(
    y = datapoint3,
    x = [1500],
    name = '    3000B$',
    visible = 'legendonly',
    mode = 'markers',
    marker = dict(
        color = 'white',
        line = dict(width = 2),
        size = np.sqrt(datapoint3)+150/datapoint3,
    ),
    text = text
)

data = [trace,trend,legend1,legend2,legend3]
    
layout = go.Layout(
    title='GDP vs Sunshine in Europe',
    xaxis=dict(
        title='Average Yearly Sunshine Hours'),
    yaxis=dict(
        title='GDP per Capita ($)'),
    hovermode='closest',
    orientation="h",
    font=dict(size=14),
    legend=dict(
    	x=1.01,
     	y=0.86,
     	font=dict(
            size=12,
            color='#000'
        	),
        		),
    annotations = [dict(
      	showarrow = False,
      	xref = 'paper',
      	yref = 'paper',
        x = 1.10,
        y = 0.91,
        text = "Total GDP",
        textangle = 0,
        font=dict(
            size=12,
            color='#000'
        	)),
    	dict(
      		showarrow = False,
	      	xref = 'paper',
	      	yref = 'paper',
	        x = 1.11,
	        y = 0.57,
	        text = "Average <br> Yearly <br> Temperature",
	        textangle = 0,
        	font=dict(
            size=12,
            color='#000'
        	))]
    )

fig = go.Figure(data=data, layout=layout)
py.plot(fig)
