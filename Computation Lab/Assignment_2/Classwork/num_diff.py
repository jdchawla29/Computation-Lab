import matplotlib.pyplot as plt
import numpy as np


def func(x):
    fn1 = 4 * x ** 2 + 2
    fn2 = np.sin(x)
    return fn1, fn2


def nd_func(x):
    h = 1e-5
    ndfn1 = (func(x + h)[0] - func(x - h)[0]) / (2 * h)
    ndfn2 = (func(x + h)[1] - func(x - h)[1]) / (2 * h)
    return ndfn1, ndfn2


x = np.linspace(-6, 6)
fn1, fn2 = func(x)
ndfn1, ndfn2 = nd_func(x)
set = list(zip(x, fn1, ndfn1))
for i in range(len(set)):
    if set[i][1] == min(fn1):
        print(set[i][0], set[i][1])

x = np.linspace(-6, 6)
plt.plot(x, func(x)[0])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, nd_func(x)[0])
plt.legend(('fn(x)', 'd_fn(x)'))
plt.savefig('num_diff_fx.png')
plt.show()
x = np.linspace(-2 * np.pi, 2 * np.pi)
plt.plot(x, func(x)[1])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, nd_func(x)[1])
plt.legend(('sin(x)', 'cos(x)'))
plt.savefig('num_diff_harmonics.png')
plt.show()
