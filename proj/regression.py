
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,26.5,0.1) # r<25 범위
y_3 = (-0.0012)*(x**3) + (0.1378)*(x**2) -5.3419*(x) + 169.53
plt.plot(x,y_3, label = '3 order')
plt.legend()

x = np.arange(26.5,55,0.1) # r>25 범위
y_4 = (-0.0000001)*(x**4) - (0.0004)*(x**3) + (0.0611)*(x**2) -3.1901*(x) + 152.57
plt.plot(x,y_4, label = '4 order')
plt.legend()

plt.show()