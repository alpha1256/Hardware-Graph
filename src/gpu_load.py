import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd

def plotGPULoad(filename):
	filecsv = pd.read_csv(filename)
	gpuTemp = filecsv['/nvidiagpu/0/load/0']
	gpu=[]
	time=[]
	for counter in range(len(gpuTemp)):
		if counter ==0:
			continue
		else:
			gpu.append(int(gpuTemp[counter]))
			time.append(counter)

	traceZero = go.Scatter(y = gpu, x = time, mode = 'lines+markers', name='Main GPU')
	
	name = "Escape From Tarkov"
	layout = dict(title = name, xaxis = dict(title = "Time"), yaxis = dict(title ="GPU Load"))
	data =[traceZero]
	figure = dict(data = data, layout = layout)
	ply.plot(figure, filename = 'GpuLoad.html')