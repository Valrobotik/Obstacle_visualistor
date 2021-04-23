"""
Programme pour lire les données du json
"""

import yaml


def yaml_data_import(nom_fichier):
    with open(nom_fichier) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


if __name__ == "__main__":
    # nom_fichier = './src/robot_config.yaml'
    # liste = yaml_data_import(nom_fichier)
    # print(liste)
    
    nom_fichier = './src/table_config.yaml'
    point_table = yaml_data_import(nom_fichier)
    points = point_table.get('point_table')
    
    listeX = []
    listeY = []
    for point in points:
        listeX.append(points.get(point).get('x'))
        listeY.append(points.get(point).get('y'))
    
    print(listeX)
    
