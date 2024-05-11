
import numpy as np
import matplotlib.pyplot as plt

#f_0=960 Hz and amplitude = 2 for 5 periods sampled with f_A=100 kHz. 
f0 = 960  
A = 2
f_A = 100000 
T = 1 / f0  
n = 5 


spp = int(f_A / f0)

t_one_period = np.linspace(0, T, spp, endpoint=False)
s1p = A * (2 * (t_one_period / T) - 1)  


ss = np.tile(s1p, n)

t = np.linspace(0, n * T, n * spp, endpoint=False)


plt.figure(figsize=(10, 4))
plt.plot(t, ss, label='Sawtooth Wave')
plt.title('Sawtooth Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

