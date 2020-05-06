import numpy as np
import matplotlib.pyplot as plt

filename = "data.log"
OFFSET = 2
with open(filename) as f :
    header = f.readline().split('/t')

data = np.genfromtxt(filename, delimiter = '/t', skip_header =1, name = ['sample', 'date', 'DATA0', 'DATA1'])
fig = plt.figure(1)
ax1 = fig.add_subplot(211) # numrows, numcols, fignum
ax2 = fig.add_subplot(212)
ax1.plot(data['sample'], data['DATA0'], 'r', label = header[OFFSET + 0])
ax2.plot(data['sample'], data['DATA1'], 'b', label = header[OFFSET + 1])
ax1.set_title("Sensor Samples")
ax1.set_xlabel('Samples')
ax1.set_ylabel('Reading')
ax2.set_xlabel('Samples')
ax2.set_ylabel('Reading')

leg1 = ax1.legend()
leg2 = ax2.legend()

plt.show()