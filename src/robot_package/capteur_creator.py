from utils.yaml_utils import yaml_data_import
from robot_package.DistSenor import DistSensor
import numpy as np

def capteur_creator(nom_fichier):

    # initialisation des capteurs
    dist_sensors = []
    # nom_fichier = './src/capteur_config.yaml'
    liste_capteur = yaml_data_import(nom_fichier)

    # Ajout des capteurs en fonction du fichier capteur_config.yaml
    for capteur, data in liste_capteur:
        dist_sensors.append(DistSensor(
            data['x'], data['y'], np.deg2rad(data['theta'])))
    
    return dist_sensors
