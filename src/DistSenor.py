import numpy as np

class DistSensor(object):
    """
    capteur de distance
    """
    def __init__(self, x=0.0, y=0.0, theta=0.0) -> None:
        """[summary]

        Args:
            x (float): position en x en mm du capteur
            y (float): position en y en mm du capteur
            t (float): angle en radian du capteur par rapport à l'axe x du robot (devant)
        """
        self.position = np.array([x, y, theta])
        self.obstacle_pose = [None, None] # Position de l'obstacle dans le repère du capteur

    def set_sensor_pose(self, x, y, theta):
        """[summary]

        Args:
            x (float): position en x en mm du capteur
            y (float): position en y en mm du capteur
            t (float): angle en radian du capteur par rapport à l'axe x du robot (devant)
        """       
        self.position = np.array([x, y, theta])

    def get_sensor_pose(self):
        """[summary]

        Returns:
            [tuple]: (x, y, t) pose of the sensor in the robot coordinates
        """        
        return self.position

    def set_dist(self, distance_x, distance_y):
        """[summary]

        Args:
            dist (float): distance en mm de l'obstacle par rapport au capteur
        """
        self.obstacle_pose = np.array([distance_x, distance_y])
        return self.obstacle_pose

    def get_obstacle_pose(self):
        """[summary]
        Returns:
            [np.array]: position in mm of the obstacle in the robot space (cartesian coordinate)
        """
        if any(elem is None for elem in self.obstacle_pose):
            return [[], []]*2


        # Projection dans le repère du robot mais positionné sur le capteur
        # x (obstacle->capteur)/robot = - distance * sin(theta)
        # y (obstacle->capteur)/robot = distance * cos(theta)
        theta = self.position[2]
        repere_robot_capteur = np.array([[-np.sin(theta),  np.cos(theta)],
                                         [-np.cos(theta), -np.sin(theta)]])

        # Déplacement de ce rèpere au centre du robot
        # x (capteur ->centre)/robot
        # y (capteur ->centre)/robot
        repere_robot_centre = np.array([self.position[0], self.position[1]])
        
        # Projection dans le repère du robot au point du capteur puis translation vers le centre du robot
        return np.dot(self.obstacle_pose, repere_robot_capteur) + repere_robot_centre
