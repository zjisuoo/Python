import matplotlib as plt
import matplotlib import animation
import numpy as np
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(15, 45))
line, = ax.plot([], [], lw=1, c='blue',marker='d',ms=2)
max_points = 50
line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',marker='d',ms=2)

def init():
    return line

h, t = Adafruit_DHT.read_retry(sensor, pin)

def get_y() :    
    h, t = Adafruit_DHT.read_retry(sensor, pin)
    return h


def animate(i):

    y = get_y() 
    
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    print(new_y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)
plt.show()