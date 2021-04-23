if __name__ == "__main__":
    # Pour executer le code en local et avoir les bon import
    import sys, os
    sys.path.append(os.getcwd() + "\\src")

from utils.yaml_utils import yaml_data_import
from robot_package.DistSenor import DistSensor
import numpy as np

def data_robot_creator(nom_fichier):
    dict_data = yaml_data_import(nom_fichier)


    dist_sensors = capteur_creator(dict_data.get('capteurs'))
    point_robot = robot_point_creator(dict_data.get('point_robot'))

    return point_robot, dist_sensors



def capteur_creator(dict_capteur):
    # initialisation de la liste de capteurs
    dist_sensors = []
    
    # Ajout des capteurs en fonction du fichier capteur_config.yaml
    for capteur in dict_capteur:
        data = dict_capteur.get(capteur)
        dist_sensors.append(DistSensor(
            data['x'], data['y'], np.deg2rad(data['theta'])))
    
    return dist_sensors


def robot_point_creator(dict_point):
    # initialisation de la liste de capteurs
    robot_pointX = []
    robot_pointY = []

    # Ajout des capteurs en fonction du fichier capteur_config.yaml
    for point in dict_point:
        data = dict_point.get(point)
        robot_pointX.append(data['x'])
        robot_pointY.append(data['y'])
    
    # Ajout de la ligne pour fermer le robot
    robot_pointX.append(robot_pointX[0])
    robot_pointY.append(robot_pointY[0])

    return [robot_pointX, robot_pointY]



if __name__ == "__main__":     
    nom_fichier = './src/robot_config.yaml'
    point_robot, dist_sensor = data_robot_creator(nom_fichier)

    print(point_robot)

