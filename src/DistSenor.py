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

    def set_sensor_postion(self, x, y, t):
        """[summary]

        Args:
            x (float): position en x en mm du capteur
            y (float): position en y en mm du capteur
            t (float): angle en radian du capteur par rapport à l'axe x du robot (devant)
        """        
        self.position = {'x':x, 'y':y, 't':t}

    def set_dist(self, dist):
        """[summary]

        Args:
            dist (float): distance en mm de l'obstacle par rapport au capteur
        """
        self.distance = dist

    def get_obstacle_pose(self):
        """[summary]

        Returns:
            [float, float]: position [[x], [y]] in mm of the obstacle in the robot space (cartesian coordinate)
        """
        if self.distance == None:
            return [0], [0]

        y = self.distance*np.sin(-self.position['t'])
        x = self.distance*np.cos(-self.position['t'])

        # ajout du vecteur obstacle au vecteur capteur
        obstacle_x = self.position['x'] + x
        obstacle_y = self.position['y'] + y
        
        return [obstacle_x], [obstacle_y]
        


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.patches import Rectangle


    fig, ax = plt.subplots()
    ax.polar(theta, r)
    plt.show()

    def conversion2polaire(x, y):
        """Conversion des coordinnées cartésiennes vers les coordonnées polaires

        Args:
            x (float): position cartésienne en x en mm
            y (float): position cartésienne en y en mm

        Returns:
            [float, float]: norme r en mm et angle en radian
        """
        r = np.sqrt(np.power(x, 2) + np.power(y, 2))
        theta = np.arctan2(y, x)

        return r, theta

    def draw_sensor(ax, x, y, theta):
        """Dispose les capteurs sur le graphe. 

        Args:
            ax (matplotlib ax): axe matplotlib
            x (float): position cartésienne x en mm du capteur
            y (float): position cartérsienne y en mm du capteur
            theta (float): direction theta en radian du capteur
        """
        r, th = conversion2polaire(x, y)
        ax.plot(th, r, 'ro')
        a = np.deg2rad(theta+90)
        ax.quiver(th, r, np.cos(a), np.sin(a))

    def draw_robot_polar(ax):
        """Affichage du robot sur le graphe

        Args:
            ax (matplotlib ax): ax matplotlib
        """
        robot_x = [50, 50, -50, -50, -150, -150, -50, -50]
        robot_y = [-150, 150, 150, 20, 20, -20, -20, -150]

        robot_x += [robot_x[0]]
        robot_y += [robot_y[0]]

        r, th = conversion2polaire(robot_x, robot_y)
        ax.plot(th, r)


    # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # ax.set_theta_zero_location('N')
    # # ax.plot(0, 0, 'ro')
    # draw_robot_polar(ax)


    # draw_sensor(ax, 50, 100, 00)
    # # draw_obstacle_polar(ax, 550, 50, 100, 0)

    # ax.grid(True)
    # ax.set_rmax(1000)
    # ax.set_rmin(0)
    # plt.show()


    # sensor1 = Sensor(5, 10, 0)
    # sensor1.set_dist(Truc du serial)
    # obstacle_sensor1 = sensor1.get_obstacle_pos()

#TODO
# fonction affichage
