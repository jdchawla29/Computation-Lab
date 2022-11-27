import numpy as np
import matplotlib.pyplot as plt


def projectile(angle, v0, time):
    dt = time / 1000  # s
    g = 9.8  # m/s^2
    # m = 1  # kg
    cd = 0.005

    # Initial
    t = [0]  # list for time
    vx = [v0 * np.cos(angle)]
    vy = [v0 * np.sin(angle)]
    x_list = [0]
    y_list = [0]

    i = 0
    while y_list[i] >= 0:
        t.append(t[i] + dt)

        # Get acceleration
        v = np.sqrt(vx[i] ** 2 + vy[i] ** 2)
        fd = cd * v ** 2
        ax = -(fd * vx[i] / v)
        ay = -g - (fd * vy[i] / v)

        # Update vx and vy
        vx.append(vx[i] + dt * ax)
        vy.append(vy[i] + dt * ay)

        # Update x and y
        x_list.append(x_list[i] + dt * vx[i])
        y_list.append(y_list[i] + dt * vy[i])

        i += 1
    return x_list, y_list, vx, vy, t


def main():
    x_list, y_list, vx, vy, t = projectile(np.pi / 3, 30, 30)
    plt.plot(x_list, y_list)
    plt.ylabel("y_list (m)")
    plt.xlabel("x_list (m)")
    plt.show()
    print("Range of Projectile is ", x_list[-1])


if __name__ == "__main__":
    main()
