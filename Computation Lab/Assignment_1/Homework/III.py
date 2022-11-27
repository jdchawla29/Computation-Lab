# code for IIA.py using classes and methods

import numpy as np
import matplotlib.pyplot as plt


class Projectile:
    g = 9.8  # m/s^2

    # m = 1  # kg

    def __init__(self, v0, angle, time):
        self.dt = time / 1000
        self.t = [0]
        self.vx = [v0 * np.cos(angle)]
        self.vy = [v0 * np.sin(angle)]
        self.x_list = [0]
        self.y_list = [0]
        self.cd = 0.005

    def get_values(self):
        i = 0
        while self.y_list[i] >= 0:
            self.t.append(self.t[i] + self.dt)

            # Get acceleration
            v = np.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2)
            fd = self.cd * v ** 2
            ax = -(fd * self.vx[i] / v)
            ay = -self.g - (fd * self.vy[i] / v)

            # Update vx and vy
            self.vx.append(self.vx[i] + self.dt * ax)
            self.vy.append(self.vy[i] + self.dt * ay)

            # Update x and y
            self.x_list.append(self.x_list[i] + self.dt * self.vx[i])
            self.y_list.append(self.y_list[i] + self.dt * self.vy[i])

            i += 1
        return self.x_list, self.y_list, self.vx, self.vy, self.t

    def show_trajectory(self):
        x_list, y_list, vx, vy, t = self.get_values()
        plt.plot(x_list, y_list)
        plt.ylabel("y_list (m)")
        plt.xlabel("x_list (m)")
        plt.show()

    def get_range(self):
        print("The range of the projectile is ", self.x_list[-1])


def main():
    projectile = Projectile(30, np.pi / 3, 30)
    projectile.show_trajectory()
    projectile.get_range()


if __name__ == "__main__":
    main()
