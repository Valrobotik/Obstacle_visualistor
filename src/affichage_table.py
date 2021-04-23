from robot_package.data_robot_creator import data_robot_creator
from utils.get_table_point import get_table_point

import matplotlib.pyplot as plt
import numpy as np

from robot_package.Robot import Robot



def init_plot(ax, table, robot, dist_sensors):
    """Fonction pour initialiser l'affichage des objets sur le plot.
    Elle renvoie une liste de matplotlib.line qui sera update pour l'animation
    Args:
        ax (matplotlib.ax): axe sur lequel on veut afficher
        table (np.array): Coordonnnées représentant la table
        robot (np.array): Cordonnées représentant le robot
        dist_sensors (list Distsensor): Liste contenant tous les capteurs

    Returns:
        matplotlib.line : liste contenant les lignes qu'il faudra mettre à jour pour l'animation
    """
    data2plot = []

    # Affichage objet fixe, et définition du plot
    ax.plot(table[0], table[1])
    ax.grid()
    ax.axis('equal')
    

    ### Affichage objet mouveant
    # Du robot
    point_robot = robot.get_robot_point()
    plot_robot, = ax.plot(point_robot[0], point_robot[1])
    data2plot.append(plot_robot)

    # Des différents capteurs
    data_plotsensor = [] 
    # Choix de mettre les capteurs dans une sous liste pour y accéder plus facilement lors de la mise à jour de l'affichage
    for sensor in dist_sensors:
        # Seulement affichage obstacle pour ce plot. (voir affichage robot pour un autre exemple)
        sensor_obs = sensor.get_obstacle_pose()
        sensor_obs = robot.transform_robot2table(sensor_obs)
        tmp_plot, = ax.plot(sensor_obs[0], sensor_obs[1], 'ro')

        data_plotsensor.append(tmp_plot)
    
    data2plot.append(data_plotsensor)

    return data2plot


def update_data(robot, dist_sensors):
    """Fonction pour mettre à jour les objets à afficher

    Args:
        robot (Robot): [description]
        dist_sensors ([type]): [description]
    """
    global x
    robot.update_position(1500 + 200*np.cos(x), 1000, 0) #+ 200*np.sin(x), np.arctan2(np.cos(-x), np.sin(-x)))
    
    for sensor in dist_sensors:
        new_dist = 200+200*np.cos(x)  # generation des datas
        sensor.set_dist(new_dist, 0)  # update des data des capteurs
    x +=0.1


def update_plot(data2plot, robot, dist_sensors):
    """Fonction pour update les datas du plot, et faire l'animation

    Args:
        data2plot (liste de matplotlib.lines): liste contenant les lines à annimer
        robot (Robot): Rboot à mettre à jour
        dist_sensors (Liste Distsensor): Capteurs à mettre à jour.
    """
    point_robot = robot.get_robot_point()
    data2plot[0].set_data(point_robot[0], point_robot[1])

    for data, sensor in zip(data2plot[1], dist_sensors):
        sensor_obstacle_pose = sensor.get_obstacle_pose()
        sensor_obstacle_pose = robot.transform_robot2table(sensor_obstacle_pose)

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

############################
# Affichage
##############################
fig, ax = plt.subplots(1, 1)
data2plot = init_plot(ax, point_table, robot, dist_sensors)

x = 0 # data x pour simuler les capteurs et le déplacement du robot.
while True:
    update_data(robot, dist_sensors)
    update_plot(data2plot, robot, dist_sensors)
    
    plt.pause(1/30)



