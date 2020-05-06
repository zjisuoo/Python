import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dht_fn import sensor

PADDING = 5
disdata = []
timeplot = 0
fig, ax = plt.subplots()
line = ax.plot(dispdata)

def update(data) :
    global dispdata, timeplot
    timeplot += 1
    disdata.append(data[0])
    ax.set_xlim(0, timeplot)
    ymin = min(dispdata)-PADDING
    ymax = max(dispdata)+PADDING
    ax.sett_ylim(ymin, ymax)
    line.set_data(range(timeplot), dispdata)

def data_gen() :
    while True :
        val = sensor()
        if val == None :
            continue
        yield val

ani = animation.FuncAnimation(fig, update, data_gen, interval = 1000)

plt.show()