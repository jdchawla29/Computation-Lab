import matplotlib.pyplot as plt
import numpy as np
import sympy


def diff_func(x):
    x = sympy.symbols("x")
    fn1 = 4 * x ** 2 + 2
    fn2 = 50 * sympy.sin(x)
    dfn1 = sympy.diff(fn1, x)
    dfn2 = sympy.diff(fn2, x)
    return fn1, fn2, dfn1, dfn2


x = sympy.symbols("x")
fn1, fn2, dfn1, dfn2 = diff_func(x)

fx1 = []
diffx1 = []
fx2 = []
diffx2 = []
for i in np.linspace(-6, 6):
    x = sympy.symbols('x')
    fx1.append(fn1.evalf(subs={x: i}))
    diffx1.append(dfn1.evalf(subs={x: i}))
    fx2.append(fn2.evalf(subs={x: i}))
    diffx2.append(dfn2.evalf(subs={x: i}))

x = np.linspace(-6, 6)
plt.plot(x, fx1)
plt.plot(x, diffx1)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, fx2)
plt.plot(x, diffx2)
plt.legend(('fx1', 'dfx1', 'fx2', 'dfx2'))
plt.savefig('symb_diff.png')
plt.show()
