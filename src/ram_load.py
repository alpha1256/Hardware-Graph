import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd

def plotRAMLoad(filename, nameofGame):
    filecsv = pd.read_csv(filename)
    ramLoad = filecsv['/ram/data/0']
    ram = []
    time = []
    for counter in range(len(ramLoad)):
        if counter == 0:
            continue
        else:
            ram.append(int(float(ramLoad[counter])))
            time.append(counter)
        
    name = nameofGame
    traceZero = go.Scatter(y = ram, x = time, mode = 'lines+markers', name='RAM Load')
    layout = dict(title = name, xaxis = dict(title = "Time"), yaxis = dict(title ="RAM Load in GB"))
    data =[traceZero]
    figure = dict(data = data, layout = layout)
    ply.plot(figure, filename = name+ '_RAM_Load.html')
