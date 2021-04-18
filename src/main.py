from DistSenor import DistSensor
from affichage import curvelinear_test2

import matplotlib.pyplot as plt
import numpy as np


def get_robot_points():
    robot_x = [50, 50, -50, -50, -150, -150, -50, -50]
    robot_y = [-150, 150, 150, 20, 20, -20, -20, -150]
    robot_x += [robot_x[0]]
    robot_y += [robot_y[0]]
    return robot_x, robot_y


# initialisation des capteurs
dist_senor = DistSensor(0.0, 0.0, 0.0)
dist_senor2 = DistSensor(0.0, 0.0, np.deg2rad(90))


# set des valeurs de distances
dist_senor.set_dist(50)
dist_senor2.set_dist(50)


#affichage
fig = plt.figure()
ax = curvelinear_test2(fig, 100)
# ax.plot(get_robot_points()[0], get_robot_points()[1], 'b')

print(dist_senor.get_obstacle_pose())
ax.plot(dist_senor.get_obstacle_pose()[0],dist_senor.get_obstacle_pose()[1], 'ro')
ax.plot(dist_senor2.get_obstacle_pose(), 'bo')


plt.show()
