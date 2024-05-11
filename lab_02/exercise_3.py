import numpy as np
import matplotlib.pyplot as plt


def DFT(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, signal)

def sawtooth_wave(f0, samples):
    t = np.arange(samples)
    omega_0 = 2 * np.pi * f0
    sawtooth = (2/np.pi) * (np.sin(omega_0 * t) + np.sin(2 * omega_0 * t) / 2 + np.sin(3 * omega_0 * t) / 3 - np.sin(4 * omega_0 * t) / 4)
    
    return sawtooth

f0 = 400  
fA_1 = 8000  
fA_2 = 16000  

samples_1 = 400
samples_2 = 16000
sawtooth_1 = sawtooth_wave(f0, samples_1)
sawtooth_2 = sawtooth_wave(f0, samples_2)

dft_sawtooth_1 = DFT(sawtooth_1)
dft_sawtooth_2 = DFT(sawtooth_2)



freq_1 = np.fft.fftfreq(samples_1, 1/fA_1)
freq_2 = np.fft.fftfreq(samples_2, 1/fA_2)


plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(freq_1, np.abs(dft_sawtooth_1))
plt.title('Amplitude Response of DFT (400 samples)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freq_2, np.abs(dft_sawtooth_2))
plt.title('Amplitude Response of DFT (16000 samples)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
