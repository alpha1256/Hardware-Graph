import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd


def fanSpeedPlot(filename,nameOfGame):
	filecsv = pd.read_csv(filename)
	fanZero=filecsv['/lpc/nct6795d/fan/1']
	fanOne = filecsv['/lpc/nct6795d/fan/5']
	fan0 =[]
	fan1 =[]
	time=[]
	for counter in range(len(fanZero)):
		if counter ==0:
			continue
		else:
			fan0.append(float(fanZero[counter]))
			fan1.append(float(fanOne[counter]))
			time.append(counter)

	traceZero = go.Scatter(y = fan0, x = time, mode = 'lines+markers', name='Fan Zero')
	traceOne = go.Scatter(y = fan1, x = time, mode = 'lines+markers', name='Fan One')
	name = nameOfGame
	layout = dict(title = name, xaxis = dict(title = "Time"), yaxis = dict(title ="Fan Speed in RPM"))
	data =[traceZero, traceOne]
	figure = dict(data = data, layout = layout)
	ply.plot(figure, filename = name +'_Fan_Speed.html')