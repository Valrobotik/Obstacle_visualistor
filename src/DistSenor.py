import numpy as np

class DistSensor(object):
    """
    capteur de distance
    """
    def __init__(self, x=0.0, y=0.0, t=0.0) -> None:
        """[summary]

        Args:
            x (float): position en x en mm du capteur
            y (float): position en y en mm du capteur
            t (float): angle en radian du capteur par rapport à l'axe x du robot (devant)
        """
        self.position = {'x':x, 'y':y, 't':t}
        self.distance = None # distance mesurée par le capteur

    def set_sensor_pose(self, x, y, t):
        """[summary]

        Args:
            x (float): position en x en mm du capteur
            y (float): position en y en mm du capteur
            t (float): angle en radian du capteur par rapport à l'axe x du robot (devant)
        """        
        self.position = {'x':x, 'y':y, 't':t}

    def get_sensor_pose(self):
        """[summary]

        Returns:
            [tuple]: (x, y, t) pose of the sensor in the robot coordinates
        """        
        return self.position['x'], self.position['y'], self.position['t']

    def set_dist(self, dist):
        """[summary]

        Args:
            dist (float): distance en mm de l'obstacle par rapport au capteur
        """
        self.distance = dist
        return dist

    def get_obstacle_pose(self):
        """[summary]
        #TODO à faire en matrice
        Returns:
            [float, float]: position [[x], [y]] in mm of the obstacle in the robot space (cartesian coordinate)
        """
        if self.distance == None:
            return [0], [0]

        y = self.distance*np.cos(-self.position['t'])
        x = self.distance*np.sin(-self.position['t'])

        # ajout du vecteur obstacle au vecteur capteur
        obstacle_x = self.position['x'] + x
        obstacle_y = self.position['y'] + y
        
        return [obstacle_x], [obstacle_y]
