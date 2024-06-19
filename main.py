import matplotlib.pyplot as plt
import numpy as np


def Sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


x = np.arange(-10, 10, 0.1)
h = Sigmoid(x)
plt.plot(x, h)
plt.axvline(0.0, color='k')
plt.axhline(y=0.5, ls='dotted', color='k')
plt.yticks([0.0, 0.5, 1.0])
plt.title(r'Sigmoid curve', fontsize=15)
plt.text(5, 0.8, r'$y=\frac{1}{1+e{-z}}$', fontsize=18)
plt.show()
