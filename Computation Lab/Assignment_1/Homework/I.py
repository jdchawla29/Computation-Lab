import numpy as np
from matplotlib.pylab import plt


def projectile(angle, v0, time):
    t = np.linspace(0, time, 300)
    dt = t[1] - t[0]  # s
    g = 9.8  # m/s2
    # m = 1  # kg
    # Distribute initial velocity to x and y.
    v0 = v0  # m/s
    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)
    y0 = 0
    x0 = 0
    vg = 0
    y_list = [y0]
    x_list = [x0]
    # ax = 0
    ay = -g

    for i in range(1, len(t)):
        # Update y.
        vg += ay * dt
        y0 += (vg + vy) * dt
        # Update x.
        x0 += vx * dt

        # Stop updating when it hits ground at y=0.
        if y0 > 0:
            y_list.append(y0)
            x_list.append(x0)
        else:
            break

    # (max x, max t)
    return x_list, y_list


x_list1, y_list1 = projectile(np.pi / 3, 100, 30)

x_list2, y_list2 = projectile(np.pi / 4, 60, 25)  # plot for (i)

# print (x_list1, y_list1)
# print (x_list2, y_list2)

plt.plot(x_list1, y_list1)
plt.plot(x_list2, y_list2)  # since, we have to plot in the same figure
plt.xlabel("x_list (m)")
plt.ylabel("y_list (m)")
plt.legend(["Angle = pi/3, v0 = 100, time = 30", "Angle = pi/4, v0 = 60, time = 25"])
plt.show()
print("Range of Projectile: ", x_list2[-1])  # Range of Projectile is simply last value of x_list
