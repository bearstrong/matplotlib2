import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

plt.figure(dpi=200)
plt.errorbar(x, y, color='r', xerr=0.2, yerr=0.4, borders=6, uplims=True);

plt.show()