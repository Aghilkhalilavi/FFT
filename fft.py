import matplotlib.pyplot as plt
import numpy as np
def FFT(x):
  N = len(x)
  if N == 1:
        return x
  else:
        X_even = FFT(x[::8])
        X_odd = FFT(x[1::8])
        factor = \
          np.exp(-2j*np.pi*np.arange(N)/ N)
        
        X = np.concatenate(\
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X
sr = 150 
ts = 2.0/sr
t = np.arange (0,1,ts)
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (9, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

plt.show()