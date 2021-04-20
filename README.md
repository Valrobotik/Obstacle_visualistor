<p align="center">
<img width="30%" src="images\logo_valrob.png" alt="Logo Valrob">
</p>

# Obstacle Visualisator

Obstacle visualisator permet placer les capteurs sur le robot et de voir en temps réels les obstacles sur la carte.
<p align="center">
<img width="100%" src="images\Affichage_capteur.gif" alt="Simulation de la detection d'obstacle du robot">
</p>

Ici il est simuler deux capteurs avec le robot au centre.

- [Obstacle Visualisator](#obstacle-visualisator)
  * [Contexte](#contexte)
  * [Utilisation](#utilisation)
  * [Auteurs](#auteurs)



## Contexte

L'association Valrobotik de l'INSA HDF développe un robot pour participer à la coupe de France de Robotique.

On recherche alors à placer et à utiliser facilement les capteurs du robot. 

On positionne les axes du robot et du capteur suivant le schéma ci-dessous :
<p align="center">
<img width="100%" src="images\Repère_robot_capteur.png" alt="Positionnement des axes du robot">
</p>


## Utilisation

Nous utilisons le fichier `capteur_config.yaml`. On inscrit dedans la position et l'angle des capteurs (l'angle est définit ci dessus) :

```code
ultrason1:
  type: ultrason
  x: 20 # position suivant x en mm
  y: 50 # position suivant y en mm
  theta: -30 #angle en degrès

ultrason2:
  type: ultrason
  x: -30 # position suivant x en mm
  y: -50 # position suivant y en mm
  theta: -190 #angle en degrès
```

Le nom `ultrason1` n'est pas important, il permet seulement de distinguer les capteurs.

<p align="center">
❗ Deux capteurs ne doivent pas avoir le même nom ❗
</p>

Il existe ensuite deux programmes :
- Un programme de simulation pur, les obstacles mesurés par le capteur sont généré par une sinusoïde. Pour lancer ce programme, executer `main.py`
- Un programme qui utilise les capteurs réels du robot. Pour cela, il faut connecter la carte à votre ordinateur, configurer le baudrate et le port_serial dans le programme `main_live.py`. 
   ```code
   # initialisation communication avec carte d'obstacles
   carte = Carte_detecteur_obstacle("COM7", 9600)
   ```

## Auteurs
S6ril & Starfunx








