import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist.angle_helper as angle_helper
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import HostAxes, GridHelperCurveLinear, Axes


def curvelinear_test2(fig, rayon_max = 1000):
    """Polar projection, but in a rectangular box."""
    # see demo_curvelinear_grid.py for details
    tr_rotate = Affine2D().translate(90, 0)
    tr_scale = Affine2D().scale(np.pi/180., 1.)
    tr = tr_rotate + tr_scale + PolarAxes.PolarTransform()
    
    extreme_finder = angle_helper.ExtremeFinderCycle(20,
                                                     20,
                                                     lon_cycle=360,
                                                     lat_cycle=None,
                                                     lon_minmax=None,
                                                     lat_minmax=(-np.inf,
                                                                 np.inf),
                                                     )

    grid_locator1 = angle_helper.LocatorDMS(8)
    # tick_formatter1 = angle_helper.FormatterDMS()

    grid_helper = GridHelperCurveLinear(tr,
                                        extreme_finder=extreme_finder,
                                        grid_locator1=grid_locator1,
                                        # tick_formatter1=tick_formatter1
                                        )

    ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)


    # Now creates floating axis
    # ax1.scatter(5, 5)

    # floating axis whose first coordinate (theta) is fixed at 60
    ax1.axis["ax"] = axis = ax1.new_floating_axis(0, 0)
    axis.set_axis_direction("top")
    axis.major_ticklabels.set_axis_direction("left")
    ax1.axis["ax1"] = axis = ax1.new_floating_axis(0, -90)
    axis.set_axis_direction("left")
    axis.major_ticklabels.set_axis_direction("top")
    # axis.label.set_text(r"$\theta = 60^{\circ}$")
    # axis.label.set_visible(True)

    # floating axis whose second coordinate (r) is fixed at 6
    ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 20)
    axis.label.set_pad(10)
    
    # axis.label.set_text(r"$r = 1$")

    ax1.set_aspect(1.)
    ax1.set_xlim(-rayon_max, rayon_max)
    ax1.set_ylim(-rayon_max, rayon_max)

    ax1.grid(True)
    return ax1




if __name__ == "__main__":
    def draw_robot_polar(ax):
        """Affichage du robot sur le graphe

            Args:
                ax (matplotlib ax): ax matplotlib
            """
        robot_x = [-150, 150, 150, 20, 20, -20, -20, -150]
        robot_y = [50, 50, -50, -50, -150, -150, -50, -50]
        robot_x += [robot_x[0]]
        robot_y += [robot_y[0]]

        ax.plot(robot_x, robot_y)

    fig = plt.figure()
    ax1 = curvelinear_test2(fig)
    draw_robot_polar(ax1)


    plt.show()
