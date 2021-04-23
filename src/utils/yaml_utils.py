"""
Programme pour lire les données du json
"""

import yaml


def yaml_data_import(nom_fichier):
    with open(nom_fichier) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


if __name__ == "__main__":
    nom_fichier = './src/capteur_config.yaml'
    liste_capteur = yaml_data_import(nom_fichier)
    
    for capteur, data in liste_capteur:
        print(data['type'], " -- ", data['x'],
              " -- ", data['y'], " -- ", data['theta'])
    


