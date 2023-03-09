import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd

def plotCPUTemp(filename, nameofGame):
	filecsv = pd.read_csv(filename)
	cpuZero=filecsv['/intelcpu/0/temperature/0']
	cpuOne = filecsv['/intelcpu/0/temperature/1']
	cpuTwo = filecsv['/intelcpu/0/temperature/2']
	cpuThree = filecsv['/intelcpu/0/temperature/3']
	cpu0 =[]
	cpu1 =[]
	cpu2 =[]
	cpu3 =[]
	time=[]
	for counter in range(len(cpuZero)):
		if counter ==0:
			continue
		else:
			cpu0.append(int(cpuZero[counter]))
			cpu1.append(int(cpuOne[counter]))
			cpu2.append(int(cpuTwo[counter]))
			cpu3.append(int(cpuThree[counter]))
			time.append(counter)

	traceZero = go.Scatter(y = cpu0, x = time, mode = 'lines+markers', name='CPU Zero')
	traceOne = go.Scatter(y = cpu1, x = time, mode = 'lines+markers', name='CPU One')
	traceTwo = go.Scatter(y = cpu2, x = time, mode = 'lines+markers', name='CPU Two')
	traceThree = go.Scatter(y = cpu3, x = time, mode = 'lines+markers', name='CPU Three')
	name = nameofGame
	layout = dict(title = name, xaxis = dict(title = "Time"), yaxis = dict(title ="CPU Temp in C"))
	data =[traceZero, traceOne, traceTwo, traceThree]
	figure = dict(data = data, layout = layout)
	ply.plot(figure, filename = name + '_CPU_Temp.html')

