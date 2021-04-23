from utils.curvelinear_plot import curvelinear_plot, get_robot_points
from robot_package.data_robot_creator import data_robot_creator

import matplotlib.pyplot as plt
import numpy as np


def init_plot(ax, point_robot, dist_sensors):
    """Fonction pour initier l'affichage.

    Args:
        ax (matplotlib.axe): axe sur lequel on va tracer les éléments
        dist_sensors (liste DistSensor): liste avec tous les capteurs 

    Returns:
        liste matplotlib.line : liste de tous les éléments à tracer sur l'axe. Ils sont regroupé pour un seul capteur
    """
    # Affichage du robot
    ax.plot(point_robot[0], point_robot[1])

    # Affichage des capteurs
    data2plot = []
    
    for sensor in dist_sensors:
        data_plot1sensor = []
        #Affichage capteur
        sensor_pose = sensor.get_sensor_pose()
        tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ko')
        data_plot1sensor.append(tmp_plot)

        # Affichage direction
        tmp_plot, = ax.plot([], [], 'k')
        data_plot1sensor.append(tmp_plot)

        # Affichage obstacle
        sensor_obs = sensor.get_obstacle_pose()
        tmp_plot, = ax.plot(sensor_obs[0], sensor_obs[1], 'ro')
        
        # Save data in data2plot for this sensor
        data_plot1sensor.append(tmp_plot)

        data2plot.append(data_plot1sensor)

    return data2plot

# Variable à incrementer pour simuler les capteurs
index = 0
def update_data(dist_sensors):
    global index
    index += 1
    for sensor in dist_sensors:
        new_dist = 200+200*np.cos(0.1*index)  # generation des datas
        sensor.set_dist(new_dist, 0)    #update des data des capteurs


def update_plot(data2plot, dist_sensors):
    # Maintenant on décompile les objets à update sur le plot avec son sensor associé
    for data, sensor in zip(data2plot, dist_sensors):
        # sensor
        sensor_pose = sensor.get_sensor_pose()
        data[0].set_data(sensor_pose[0], sensor_pose[1])

        #tracé de la direction du capteur
        data[1].set_data([sensor_pose[0], sensor_pose[0] + 50*np.sin(-sensor_pose[2])], [
                                 sensor_pose[1], sensor_pose[1] + 50*np.cos(-sensor_pose[2])])

        # obstacle
        sensor_obstacle_pose = sensor.get_obstacle_pose()
        data[2].set_data(sensor_obstacle_pose[0], sensor_obstacle_pose[1])


if __name__ == "__main__":
    ####################
    #affichage
    fig, ax = curvelinear_plot(500)

    # initialisation des capteurs
    nom_fichier = './src/robot_config.yaml'
    point_robot, dist_sensors = data_robot_creator(nom_fichier)
    
    data2plot = init_plot(ax, point_robot, dist_sensors)

    # Attention le plot ne se ferme pas avec la croix de la fenètre
    while True:
        update_data(dist_sensors)
        update_plot(data2plot, dist_sensors)
        plt.pause(0.1)



