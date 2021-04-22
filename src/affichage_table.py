

import matplotlib.pyplot as plt
import numpy as np

from robot_package.Robot import Robot

carte = [[0, 0, 3000, 3000, 0],
         [0, 2000, 2000, 0, 0]]



def init_plot(ax):
    ax.plot(carte[0], carte[1])

    point_robot = robot.get_robot_point()
    plot_robot, = ax.plot(point_robot[0], point_robot[1])

    ax.grid()
    ax.axis('equal')
    return plot_robot


def update_data(robot):
    global x
    robot.update_position(1500 + 200*np.sin(x), 1000 +
                          200*np.cos(x), np.arctan2(np.sin(-x), np.cos(-x)))
    x +=0.1


def update_plot(robot, plot_robot):
    point_robot = robot.get_robot_point()
    plot_robot.set_data(point_robot[0], point_robot[1])


robot = Robot(1500, 1000, np.pi/3)

fig, ax = plt.subplots(1, 1)
plot_robot = init_plot(ax)

x = 0
while True:
    update_data(robot)
    update_plot(robot, plot_robot)
    
    plt.pause(0.001)



