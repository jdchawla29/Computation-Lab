import matplotlib.pyplot as plt
import numpy as np


# (a) Creating the required function

def func(x, a, b):
    return a * np.exp(x) + b * np.exp(-x)


x = np.linspace(-6, 6)
y1 = func(x, 2, 3)
y2 = func(x, 4, 6)

# (b) Plotting the function

plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Plot of y = a*e^x + b*e^(-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['a=2, b=3', 'a=4, b=6'])
plt.show()

# (c) Curve fitting

# Fitting y for a=2, b=3
p2 = np.polyfit(x, y1, 2)
p3 = np.polyfit(x, y1, 3)
p4 = np.polyfit(x, y1, 4)
plt.plot(x, y1, 'y-')
plt.plot(x, np.polyval(p2, x), 'r-')
plt.plot(x, np.polyval(p3, x), 'b-')
plt.plot(x, np.polyval(p4, x), 'g-')
plt.title("Fitting y = 2*e^x + 3*e^(-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['Function', 'Order 2 Fit', 'Order 3 Fit', 'Order 4 Fit'])
plt.show()

# Fitting y for a=4, b=6
p2 = np.polyfit(x, y2, 2)
p3 = np.polyfit(x, y2, 3)
p4 = np.polyfit(x, y2, 4)
plt.plot(x, y2, 'y-')
plt.plot(x, np.polyval(p2, x), 'r-')
plt.plot(x, np.polyval(p3, x), 'b-')
plt.plot(x, np.polyval(p4, x), 'g-')
plt.title("Fitting y = 4*e^x + 6*e^(-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['Function', 'Order 2 Fit', 'Order 3 Fit', 'Order 4 Fit'])
plt.show()
