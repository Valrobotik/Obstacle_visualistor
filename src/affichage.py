import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np



# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute areas and colors
N = 5
r = 2 * np.random.rand(N)
print(r)
theta = 2 * np.pi * np.random.rand(N)

area = 200 * r**2
colors = theta

# fig = plt.figure()
# axes_coords = [0, 0, 1, 1]


# ax_polar = fig.add_axes(axes_coords, projection='polar', label="ax polar")
# ax_polar.set_theta_zero_location('N')
# c = ax_polar.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

# im = plt.imread('./images/top.png')


image = img.imread('./images/top.png')
plt.imshow(image, interpolation='none', extent=(-15, 15, 10, -10))
plt.show()


plt.show()
