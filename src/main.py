from DistSenor import DistSensor
from affichage import curvelinear_plot, get_robot_points

import matplotlib.pyplot as plt
import numpy as np



# initialisation des capteurs
dist_senor = DistSensor(20, 50, np.deg2rad(-30))
dist_senor2 = DistSensor(-30, -50, np.deg2rad(-180))
dist_sensors = [dist_senor, dist_senor2]
# dist_sensors = [dist_senor]

# set des valeurs de distances
dist_senor.set_dist(50)
dist_senor2.set_dist(50)


####################
#affichage
fig, ax = curvelinear_plot(500)

# plot robot
ax.plot(get_robot_points()[0], get_robot_points()[1], 'b')

#plot sensors
for sensor in dist_sensors:
    # sensor
    sensor_pose = sensor.get_sensor_pose()
    ax.plot(sensor_pose[0], sensor_pose[1], 'k.')
        # ax.plot(th, r, 'ro')
        # a = np.deg2rad(theta+90)
    ax.quiver(sensor_pose[0], sensor_pose[1], np.sin(-sensor_pose[2]), np.cos(-sensor_pose[2]))

    # obstacle
    sensor_obstacle_pose = sensor.get_obstacle_pose()     
    ax.plot(sensor_obstacle_pose[0],sensor_obstacle_pose[1], 'ro')





# ax.plot(robot_x, robot_y)

plt.show()
