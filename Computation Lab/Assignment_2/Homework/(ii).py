import matplotlib.pyplot as plt
import numpy as np

import sympy


def diff_func(r, A, B):
    r = sympy.symbols('r')
    V = (B / r ** 12) - (A / r ** 6)
    F = -(sympy.diff(V, r))
    return V, F


r = sympy.symbols('r')
A = 1.024 / 1.381
B = 1.586e-3 / 1.381
V, F = diff_func(r, A, B)

# (a) Plotting V(r)

v = []
for i in np.linspace(0.3, 0.8):
    v.append(V.evalf(subs={r: i}))

plt.plot(np.linspace(0.3, 0.8), v)
plt.title("Plot of LJ Potential vs Separation (in terms of Boltzmann Constant)")
plt.ylabel('V(r)/kb (unit: K)')
plt.xlabel('r in nm')
plt.show()

# (b) Plotting F(r)

f = []
for i in np.linspace(0.3, 0.8):
    f.append(F.evalf(subs={r: i}))

plt.plot(np.linspace(0.3, 0.8), f)
plt.title("Plot of Force vs Separation (in terms of Boltzmann Constant)")
plt.ylabel('F(r)/kb (unit: K/m)')
plt.xlabel('r in nm')
plt.show()

# (c) Equilibrium separation
r = np.linspace(0.3, 0.8)
data = list(zip(r, v))
for i in range(len(data)):
    if data[i][1] == min(v):
        print("Equilibrium Separation is", data[i][0], "nm")
