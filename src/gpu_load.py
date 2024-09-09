import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd

def plotGPULoad(filename, nameofGame):
	filecsv = pd.read_csv(filename)
	gpuTemp = filecsv['/nvidiagpu/0/load/0']
	testTime = filecsv['/time']
	gpu=[]
	time=[]
	testTim = []
	for counter in range(len(gpuTemp)):
		if counter ==0:
			continue
		else:
			gpu.append(int(gpuTemp[counter]))
			#time.append(counter)
			time.append(testTime[counter])

	traceZero = go.Scatter(y = gpu, x = time, mode = 'lines+markers', name='Main GPU')
	
	name = nameofGame
	layout = dict(title = name, xaxis = dict(title = "Time"), yaxis = dict(title ="GPU Load"))
	data =[traceZero]
	figure = dict(data = data, layout = layout)
	ply.plot(figure, filename = name + '_GPU_Load.html')