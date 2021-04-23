from robot_package.data_robot_creator import data_robot_creator
from utils.get_table_point import get_table_point

import matplotlib.pyplot as plt
import numpy as np

from robot_package.Robot import Robot



def init_plot(ax, table, robot, dist_sensors):
    data2plot = []

    # Affichage objet fixe
    ax.plot(table[0], table[1])
    ax.grid()
    ax.axis('equal')
    

    # Affichage objet mouveant
    point_robot = robot.get_robot_point()
    plot_robot, = ax.plot(point_robot[0], point_robot[1])
    data2plot.append(plot_robot)

    data_plotsensor = []
    for sensor in dist_sensors:
        # Affichage obstacle
        sensor_obs = sensor.get_obstacle_pose()
        sensor_obs = robot.transform_robot_point_2_robot_table(sensor_obs)
        tmp_plot, = ax.plot(sensor_obs[0], sensor_obs[1], 'ro')

        data_plotsensor.append(tmp_plot)
    
    data2plot.append(data_plotsensor)

    return data2plot


def update_data(robot, dist_sensors):
    global x
    robot.update_position(1500 + 200*np.cos(x), 1000,0)# np.arctan2(np.sin(-x), np.cos(-x)))
    
    for sensor in dist_sensors:
        new_dist = 200+200*np.cos(x)  # generation des datas
        sensor.set_dist(new_dist, 0)  # update des data des capteurs
    x +=0.1


def update_plot(data2plot, robot, dist_sensors):
    point_robot = robot.get_robot_point()
    data2plot[0].set_data(point_robot[0], point_robot[1])

    for data, sensor in zip(data2plot[1], dist_sensors):
        sensor_obstacle_pose = sensor.get_obstacle_pose()
        sensor_obstacle_pose = robot.transform_robot_point_2_robot_table(sensor_obstacle_pose)

        data.set_data(sensor_obstacle_pose[0], sensor_obstacle_pose[1])


####################################################################
# MAIN PROGRAM

# Creation des points de la table
fichier_table = './src/table_config.yaml'
point_table = get_table_point(fichier_table)

# Creation des points capteurs et point robot
fichier_robot = './src/robot_config.yaml'
point_robot, dist_sensors = data_robot_creator(fichier_robot)

# creation de l'objet robot
robot = Robot(1500, 1000, np.pi/3)
robot.define_robot_shape(np.array(point_robot))

### Affichage
fig, ax = plt.subplots(1, 1)
data2plot = init_plot(ax, point_table, robot, dist_sensors)

x = 0
while True:
    update_data(robot, dist_sensors)
    update_plot(data2plot, robot, dist_sensors)
    
    plt.pause(0.001)



