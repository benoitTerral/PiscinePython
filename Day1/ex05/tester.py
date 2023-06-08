from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.use("WebAgg")

os.chdir(os.path.dirname(__file__))
array = ft_load("landscape.jpg")
array_inverted = ft_invert(array)
array_red = ft_red(array)
array_green = ft_green(array)
array_blue = ft_blue(array)
array_grey = ft_grey(array)
print(ft_invert.__doc__)

fig = plt.figure(figsize=(10, 8))
ax1 = plt.subplot(3, 2, 1)
ax2 = plt.subplot(3, 2, 2)
ax3 = plt.subplot(3, 2, 3)
ax4 = plt.subplot(3, 2, 4)
ax5 = plt.subplot(3, 2, 5)
ax6 = plt.subplot(3, 2, 6)
ax1.imshow(array)
ax2.imshow(array_inverted)
ax3.imshow(array_red)
ax4.imshow(array_green)
ax5.imshow(array_blue)
ax6.imshow(array_grey, cmap=plt.cm.gray)
plt.show()
