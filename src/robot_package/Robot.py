from matplotlib.pyplot import copper
import numpy as np
#Robot point dans yalm

class Robot():
    def __init__(self, x, y, t) -> None:
        self.position = np.array([x, y, t])
        self.shape = []

    def update_position(self, x, y, t):
        self.position = np.array([x, y, t])

    def get_transformation_matrix(self):
        x = self.position[0]
        y = self.position[1]
        t = self.position[2]

        M_robot_table_rotation = np.array([[np.sin(t), np.cos(t), 0],
                                           [-np.cos(t), np.sin(t), 0],
                                           [0, 0, 1]])

        M_robot_table_translation = np.array([[1, 0, x],
                                              [0, 1, y],
                                              [0, 0, 1]])

        M_robot_table = np.dot(M_robot_table_translation,
                               M_robot_table_rotation)

        return M_robot_table

    def get_robot_point(self):
        robot = self.get_robot_shape()
        robot = np.append(robot, [[1]*len(robot[0])], axis=0)

        M_robot_table = self.get_transformation_matrix()
        robot = np.dot(M_robot_table, robot)

        return np.array([robot[0], robot[1]])
    
    def define_robot_shape(self, points_of_shape):
        self.shape = points_of_shape

    def get_robot_shape(self):
        return self.shape

    def transform_robot_point_2_robot_table(self, coordonnee_point):
        if coordonnee_point == [[], []]:
            return np.array([[], []])
        
        coordonnee_point = np.append(coordonnee_point, [[1]])
        M_robot_table = self.get_transformation_matrix()

        return np.dot(M_robot_table, coordonnee_point)
