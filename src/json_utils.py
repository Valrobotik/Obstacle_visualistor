"""
Programme pour lire les données du json
"""

import json


def donnee_capteurs(fichier_donnee):
    with open(fichier_donnee) as file:
            data = json.load(file)

    return data
    



if __name__ == "__main__":
    data = donnee_capteurs('./src/positions.json')

    for capteur in data['capteurs']:
        print(capteur['nom'], "position", capteur['position']['X'], capteur['position']['Y'])

