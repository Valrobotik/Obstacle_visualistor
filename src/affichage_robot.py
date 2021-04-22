from robot_package.DistSenor import DistSensor
from utils.curvelinear_plot import curvelinear_plot, get_robot_points
from utils.yaml_utils import yaml_data_import

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from itertools import count


# initialisation des capteurs
dist_sensors = []
nom_fichier = './src/capteur_config.yaml'
liste_capteur = yaml_data_import(nom_fichier)

# Ajout des capteurs en fonction du fichier capteur_config.yaml
for capteur, data in liste_capteur:
    dist_sensors.append(DistSensor(
        data['x'], data['y'], np.deg2rad(data['theta'])))





####################
#affichage
fig, ax = curvelinear_plot(500)


sensor_plots = []
sensor_obs_plots = []
sensor_dir_plots = []

def init_plot():
    robot = get_robot_points()
    ax.plot(robot[0], robot[1])
    for sensor in dist_sensors:
        sensor_pose = sensor.get_sensor_pose()
        tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ko')
        sensor_plots.append(tmp_plot)

        # tmp_plot, = ax.plot([sensor_pose[0], sensor_pose[0]+ 10*np.cos(sensor_pose[2])], [sensor_pose[1], sensor_pose[1] + sensor_pose[1] + 10*np.sin(sensor_pose[2])], 'k')
        tmp_plot, = ax.plot([], [], 'k')
        sensor_dir_plots.append(tmp_plot)

        sensor_obs = sensor.get_obstacle_pose()
        tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ro')
        sensor_obs_plots.append(tmp_plot)

    return sensor_plots, sensor_dir_plots, sensor_obs_plots


index = count()

def update_data():
    data = next(index)
    for sensor in dist_sensors:
        new_dist = 200+200*np.cos(0.1*data) # generation des datas
        sensor.set_dist(new_dist, 0)    #update des data des capteurs


def update_plot():
    for sensor, sensor_plot, sensor_obs_plot, sensor_dir_plot in zip(dist_sensors, sensor_plots, sensor_obs_plots, sensor_dir_plots):
        # sensor
        sensor_pose = sensor.get_sensor_pose()
        # ax.plot(sensor_pose[0], sensor_pose[1], 'k.')
        sensor_plot.set_data(sensor_pose[0], sensor_pose[1])

        #tracé de la direction du capteur
        sensor_dir_plot.set_data([sensor_pose[0], sensor_pose[0] + 50*np.sin(-sensor_pose[2])], [
                                 sensor_pose[1], sensor_pose[1] + 50*np.cos(-sensor_pose[2])])

        # obstacle
        sensor_obstacle_pose = sensor.get_obstacle_pose()
        # ax.plot(sinsor_obstacle_pose[0],sensor_obstacle_pose[1], 'ro')
        sensor_obs_plot.set_data(sensor_obstacle_pose[0], sensor_obstacle_pose[1])



init_plot()
# Attention le plot ne se ferme pas avec la croix de la fenètre
while True:
    update_data()
    update_plot()
    plt.pause(0.1)



