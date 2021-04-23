if __name__ == "__main__":
    # Pour executer le code en local et avoir les bon import
    import sys
    import os
    sys.path.append(os.getcwd() + "\\src")

from utils.yaml_utils import yaml_data_import


def get_table_point(nom_fichier):

    point_table = yaml_data_import(nom_fichier)
    points = point_table.get('point_table')

    listeX = []
    listeY = []
    for point in points:
            listeX.append(points.get(point).get('x'))
            listeY.append(points.get(point).get('y'))

    return [listeX, listeY]


if __name__ == "__main__":
    nom_fichier = './src/table_config.yaml'
    table = get_table_point(nom_fichier)

    print(table)
