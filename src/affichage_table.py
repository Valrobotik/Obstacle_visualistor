

import matplotlib.pyplot as plt
import numpy as np

from robot_package.Robot import Robot

carte = [[0, 0, 3000, 3000, 0],
         [0, 2000, 2000, 0, 0]]



    

def update_data():
    pass


def update_plot():
    pass


robot = Robot(1500, 1000, np.pi/3)

fig, ax = plt.subplots(1, 1)
ax.plot(carte[0], carte[1])

point_robot = robot.get_robot_point()
plot_robot, = ax.plot(point_robot[0], point_robot[1])


ax.grid()
ax.axis('equal')

x = 0
while True:
    robot.update_position(1500 + 200*np.sin(x), 1000 + 200*np.cos(x), np.arctan2(np.sin(-x), np.cos(-x)))
    point_robot = robot.get_robot_point()
    plot_robot.set_data(point_robot[0], point_robot[1])
    x +=0.1
    plt.pause(0.001)


plt.show()

