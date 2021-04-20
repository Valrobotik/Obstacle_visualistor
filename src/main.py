from DistSenor import DistSensor
from affichage import curvelinear_plot, get_robot_points

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from itertools import count


# initialisation des capteurs
dist_senor = DistSensor(20, 50, np.deg2rad(-30))
dist_senor2 = DistSensor(-30, -50, np.deg2rad(-190))
dist_sensors = [dist_senor, dist_senor2]
# dist_sensors = [dist_senor]




####################
#affichage
fig, ax = curvelinear_plot(500)


sensor_plots = []
sensor_obs_plots = []
sensor_dir_plots = []

def init():
    robot = get_robot_points()
    ax.plot(robot[0], robot[1])
    for sensor in dist_sensors:
        sensor_pose = sensor.get_sensor_pose()
        tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ko')
        sensor_plots.append(tmp_plot)

        # tmp_plot, = ax.plot([sensor_pose[0], sensor_pose[0]+ 10*np.cos(sensor_pose[2])], [sensor_pose[1], sensor_pose[1] + sensor_pose[1] + 10*np.sin(sensor_pose[2])], 'k')
        tmp_plot, = ax.plot([], [], 'k')
        sensor_dir_plots.append(tmp_plot)

        sensor_obs = sensor.get_obstacle_pose()
        tmp_plot, = ax.plot([sensor_pose[0]], sensor_pose[1], 'ro')
        sensor_obs_plots.append(tmp_plot)

    return sensor_plots, sensor_dir_plots, sensor_obs_plots


index = count()

def data_gen():
    data = next(index)
    for sensor in dist_sensors:
        new_dist = 200+200*np.cos(0.1*data)
        sensor.set_dist(new_dist)
        yield data


def run(data):
    for sensor, sensor_plot, sensor_obs_plot, sensor_dir_plot in zip(dist_sensors, sensor_plots, sensor_obs_plots, sensor_dir_plots):
        # sensor
        sensor_pose = sensor.get_sensor_pose()
        # ax.plot(sensor_pose[0], sensor_pose[1], 'k.')
        sensor_plot.set_data(sensor_pose[0], sensor_pose[1])

        #tracé de la direction du capteur
        sensor_dir_plot.set_data([sensor_pose[0], sensor_pose[0] + 50*np.sin(-sensor_pose[2])], [
                                 sensor_pose[1], sensor_pose[1] + 50*np.cos(-sensor_pose[2])])

        # obstacle
        sensor_obstacle_pose = sensor.get_obstacle_pose()
        # ax.plot(sinsor_obstacle_pose[0],sensor_obstacle_pose[1], 'ro')
        sensor_obs_plot.set_data(
            sensor_obstacle_pose[0], sensor_obstacle_pose[1])



init()
ani = animation.FuncAnimation(fig, run, data_gen, interval=1)
plt.show()


