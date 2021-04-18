
from DistSenor import DistSensor
from affichage import curvelinear_test2
from capteur import Carte_detecteur_obstacle

import matplotlib.pyplot as plt
import numpy as np

import time


def get_robot_points():
    robot_x = [-150, 150, 150, 20, 20, -20, -20, -150]
    robot_y = [50, 50, -50, -50, -150, -150, -50, -50]
    robot_x += [robot_x[0]]
    robot_y += [robot_y[0]]
    return [robot_x, robot_y]

#####################################
#initialisation

# initialisation des capteurs (virtuels)
dist_sensor = DistSensor(20, 50, np.deg2rad(-30))
dist_sensor2 = DistSensor(-30, -50, np.deg2rad(-180))
# dist_sensors = [dist_sensor, dist_sensor2]
dist_sensors = [dist_sensor]

# initialisation communication avec carte d'obstacles
carte = Carte_detecteur_obstacle("COM7", 9600)

#init afffichage
fig = plt.figure()
ax = curvelinear_test2(fig, 500)


####################################################
while True:
    dist_sensor.set_dist(carte.get_distance(0))

    time.sleep(0.2)


    ####################
    #affichage
    ax.cla()

    # plot robot
    ax.plot(get_robot_points()[0], get_robot_points()[1], 'b')

    #plot sensors
    for sensor in dist_sensors:
        # sensor
        sensor_pose = sensor.get_sensor_pose()
        ax.plot(sensor_pose[0], sensor_pose[1], 'k.')
            # ax.plot(th, r, 'ro')
            # a = np.deg2rad(theta+90)
        ax.quiver(sensor_pose[0], sensor_pose[1], np.sin(-sensor_pose[2]), np.cos(-sensor_pose[2]))

        # obstacle
        sensor_obstacle_pose = sensor.get_obstacle_pose()     
        ax.plot(sensor_obstacle_pose[0],sensor_obstacle_pose[1], 'ro')
    
    plt.pause(0.1)

plt.show()
