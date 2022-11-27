import matplotlib.pyplot as plt
import numpy as np


def sincos(x):
    return np.cos(x), np.sin(x)


def combo(x, a, b):
    return a * np.sin(x) + b * np.cos(x)


xdata = np.linspace(-np.pi, np.pi, 300)
print(xdata)

cos, sin = sincos(xdata)
comb_har = combo(xdata, 2, 3)

plt.plot(xdata, sin, ".", label="sin");
plt.plot(xdata, cos, ".", label="cos");
plt.plot(xdata, comb_har, ".", label="Data");
plt.xlabel("x")
plt.ylabel("y")
plt.legend(( 'sin(x)', 'cos(x)','harmonics(x)'))
plt.savefig('harmonics.png')
plt.show()
