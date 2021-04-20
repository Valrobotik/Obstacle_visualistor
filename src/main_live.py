
from DistSenor import DistSensor
from affichage import curvelinear_plot
from capteur import Carte_detecteur_obstacle

import matplotlib.pyplot as plt
import numpy as np

import time

def update_quiver(num, Q, X, Y):
    """updates the horizontal and vertical vector components by a
    fixed increment on each frame
    """

    U = np.cos(X + num*0.1)
    V = np.sin(Y + num*0.1)

    Q.set_UVC(U,V)

    return Q,
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
ax = curvelinear_plot(fig, 500)

# plot robot
ax.plot(get_robot_points()[0], get_robot_points()[1], 'b')

sensor_plots = []
sensor_obs_plots = []
sensor_dir_plots = []
for sensor in dist_sensors:
    sensor_pose = sensor.get_sensor_pose()
    tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ko')
    sensor_plots.append(tmp_plot)

    # tmp_plot, = ax.plot([sensor_pose[0], sensor_pose[0]+ 10*np.cos(sensor_pose[2])], [sensor_pose[1], sensor_pose[1] + sensor_pose[1] + 10*np.sin(sensor_pose[2])], 'k')
    tmp_plot, = ax.plot([],[], 'k')
    sensor_dir_plots.append(tmp_plot)


    sensor_obs = sensor.get_obstacle_pose()
    tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ro')
    sensor_obs_plots.append(tmp_plot)


####################################################
while True:
    dist_sensor.set_dist(carte.get_distance(0))


    ####################
    #affichage

    #plot sensors
    for sensor, sensor_plot, sensor_obs_plot, sensor_dir_plot in zip(dist_sensors, sensor_plots, sensor_obs_plots, sensor_dir_plots):
        # sensor
        sensor_pose = sensor.get_sensor_pose()
        # ax.plot(sensor_pose[0], sensor_pose[1], 'k.')
        sensor_plot.set_data(sensor_pose[0], sensor_pose[1])
        
        #tracé de la direction du capteur
        sensor_dir_plot.set_data([sensor_pose[0], sensor_pose[0]+ 50*np.sin(-sensor_pose[2])], [sensor_pose[1], sensor_pose[1] + 50*np.cos(-sensor_pose[2])])        

        # obstacle
        sensor_obstacle_pose = sensor.get_obstacle_pose()     
        # ax.plot(sinsor_obstacle_pose[0],sensor_obstacle_pose[1], 'ro')
        sensor_obs_plot.set_data(sensor_obstacle_pose[0], sensor_obstacle_pose[1])
        
        #tracé du rayon capteur-obstacle
        # sensor_dir_plot.set_data([sensor_pose[0], sensor_obstacle_pose[0]], [sensor_pose[1], sensor_obstacle_pose[1]])        
        # sensor_dir_plot.set_data([sensor_pose[0], sensor_obstacle_pose[0]], [sensor_pose[1], sensor_obstacle_pose[1]])        
    
    plt.pause(0.01)

plt.show()
