import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd

def plotCPULoad(filename,nameOfGame):
	filecsv = pd.read_csv(filename)
	cpuZero=filecsv['/intelcpu/0/load/1']
	cpuOne = filecsv['/intelcpu/0/load/2']
	cpuTwo = filecsv['/intelcpu/0/load/3']
	cpuThree = filecsv['/intelcpu/0/load/4']
	cpu0 =[]
	cpu1 =[]
	cpu2 =[]
	cpu3 =[]
	time=[]
	for counter in range(len(cpuZero)):
		if counter ==0:
			continue
		else:
			cpu0.append(float(cpuZero[counter]))
			cpu1.append(float(cpuOne[counter]))
			cpu2.append(float(cpuTwo[counter]))
			cpu3.append(float(cpuThree[counter]))
			time.append(counter)

	traceZero = go.Scatter(y = cpu0, x = time, mode = 'lines+markers', name='CPU Zero')
	traceOne = go.Scatter(y = cpu1, x = time, mode = 'lines+markers', name='CPU One')
	traceTwo = go.Scatter(y = cpu2, x = time, mode = 'lines+markers', name='CPU Two')
	traceThree = go.Scatter(y = cpu3, x = time, mode = 'lines+markers', name='CPU Three')
	name = nameOfGame
	layout = dict(title = name, xaxis = dict(title = "Time"), yaxis = dict(title ="CPU Load"))
	data =[traceZero, traceOne, traceTwo, traceThree]
	figure = dict(data = data, layout = layout)
	ply.plot(figure, filename = name +'_CPU_Load.html')