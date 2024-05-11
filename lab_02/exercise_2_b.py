import numpy as np
import matplotlib.pyplot as plt


f0 = 960 
amplitude = 2
num_periods = 5
fa = 100000 


T = 1 / f0
t_one_period = np.linspace(0, T, int(T * fa), endpoint=False)


w = 2 * np.pi * f0


ss = np.zeros_like(t_one_period)


for n in range(1, 6): 
    ss += 2 * np.pi * np.sin(n * w * t_one_period) * (-1)**(n - 1) / n

t = np.linspace(0, num_periods * T, int(num_periods * T * fa), endpoint=False)
ss = np.tile(ss, num_periods)

plt.figure(figsize=(10, 6))

plt.plot(t, ss, label='Original Sawtooth', color='blue')


plt.title('Sawtooth Signal and Its Fifth Harmonic')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()