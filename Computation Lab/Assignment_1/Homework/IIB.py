import numpy as np
import matplotlib.pyplot as plt

import IIA

x_list, y_list, vx, vy, t = IIA.projectile(np.pi / 3, 30, 30)

plt.plot(t, vx, "r")
plt.plot(t, vy, "g")
plt.xlabel("time (s)")
plt.legend(["vx (m/s)", "vy (m/s)"])
plt.show()
