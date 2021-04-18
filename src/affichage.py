import numpy as np
import matplotlib.pyplot as plt


def draw_axis(max_range=1000):
    # initializing the figure
    fig = plt.figure()
    # setting the axis limits in [left, bottom, width, height]
    xy_limit = (-max_range, max_range)
    rect = [0.1, 0.1, 0.8, 0.8]

    # the carthesian axis:
    ax_carthesian = fig.add_axes(rect)
    ax_carthesian.set_xlim(xy_limit)
    ax_carthesian.set_ylim(xy_limit)
    # the polar axis:
    ax_polar = fig.add_axes(rect, polar=True, frameon=False)
    ax_polar.set_theta_zero_location('N')
    ax_polar.set_rmax(xy_limit[1])
    ax_polar.grid(True)

    # plotting the line on the carthesian axis
    # ax_carthesian.plot(line, 'b')

    # the polar plot
    # ax_polar.plot(theta, r, color='r', linewidth=3)
    return ax_carthesian, ax_polar


def draw_robot(ax):
    robot_x = [50, 50, -50, -50, -150, -150, -50, -50]
    robot_y = [-150, 150, 150, 20, 20, -20, -20, -150]

    robot_x += [robot_x[0]]
    robot_y += [robot_y[0]]

    ax.plot(robot_y, robot_x)



if __name__ == "__main__":
    ax_carthesian, ax_polar = draw_axis()
    draw_robot(ax_carthesian)




    plt.show()
