import numpy as np
import matplotlib.pyplot as plt


A0 = 1
f0 = 960
fs = 8000


k = np.arange(0,61)  


t = 1/fs
w = 2 * np.pi *f0
y = np.sin(w*t*k)

plt.stem(k,y)

plt.show()