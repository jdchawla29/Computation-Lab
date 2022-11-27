import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import sympy
# (A)

# 1. Reading the data and plot it
L, E = np.loadtxt("C_1.dat", delimiter=None, unpack=True)
plt.plot(L, E, ".")
plt.xlabel("Lattice_parameter, L (A)")
plt.xlabel("Energy, E (ev)")


# 2. Finding the best fit

# let's try a quadratic fit
# coeffs = np.polyfit(L, E, 2)
# Lfit = np.linspace(min(L), max(L), 100)
# Vfit = coeffs[0] * Lfit ** 2 + coeffs[1] * Lfit + coeffs[2]
# plt.plot(Lfit, Vfit)
# plt.show()
# Fit is not that good so we can try a cubic one

def func(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


popt, pconv = opt.curve_fit(func, L, E)
plt.plot(L, func(L, *popt))
plt.show()

# Cubic fit is nice so let's proceed with the next part

# 3. Lattice Parameter and Ground State Energy

E_val = func(L, *popt)
E0 = min(E_val)
print("Ground state energy is", E0, "eV")

pair = list(zip(L, E_val))
L0 = 0
for i in range(len(pair)):
    if pair[i][1] == min(E_val):
        L0 = pair[i][0]
        print("Lattice Parameter is", L0, "A")

# (B)

# 1. Plotting Energy difference vs Strain
Es = E-E0
S = (L-L0)/L
plt.plot(S, Es,".", label="data")
plt.xlabel("Strain, S = L-L0")
plt.ylabel("Energy_difference, Es = E - E0 (eV)")

# 2. Finding the best fit

# let's try cubic fit again

popt, pconv = opt.curve_fit(func, S, Es)
plt.plot(S, func(S, *popt), label="opt_plot")
plt.show()

# it works :), let's move to the next part

# (3)
# clearly all we need to do write the derivative of our func (which is quadratic) with the optimized parameters.

S_val = np.linspace(min(S), max(S), 100)
dEsdS = []
for i in S_val:
    dEsdS.append(3*popt[0]*i**2+2*popt[1]*i+popt[2])

plt.plot(S_val, dEsdS)
plt.xlabel("Strain, S")
plt.ylabel("dEs/dS")
plt.show()

# to determine the strength we make use of slope near origin
print(popt[2])  # put S = 0
