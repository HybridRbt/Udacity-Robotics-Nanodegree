# import libs
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

from helper_functions import color_thresh

# define file names
filename = "sample.jpg"
image = mpimg.imread(filename)  # read file

print(image.dtype, image.shape, np.min(image), np.max(image))

# get red channel
red_channel = np.copy(image)
red_channel[:, :, [1, 2]] = 0

# get green channel
green_channel = np.copy(image)
green_channel[:, :, [0, 2]] = 0

# get blue channel
blue_channel = np.copy(image)
blue_channel[:, :, [0, 1]] = 0

red_th = 160
green_th = 160
blue_th = 160

rgb_th = (red_th, green_th, blue_th)

# get the filtered image
color_th = color_thresh(image, rgb_th)

# get a 2 X 4 grid
G = gridspec.GridSpec(2, 4)
fig = plt.figure(figsize=(21, 7))

# get the grid for original image
ax1 = plt.subplot(G[:, :2])
# show original image
ax1.imshow(image)
ax1.set_title('Original Image', fontsize = 40)

# get the grid for red channel
ax2 = plt.subplot(G[0, 2])
ax2.imshow(red_channel)
ax2.set_title('Red Channel', fontsize = 20)

# get the grid for green channel
ax3 = plt.subplot(G[0, 3])
ax3.imshow(green_channel)
ax3.set_title('Green Channel', fontsize = 20)

# get the grid for blue channel
ax4 = plt.subplot(G[1, 2])
ax4.imshow(blue_channel)
ax4.set_title('Blue Channel', fontsize = 20)

# get the grid for filtered b & w image
ax5 = plt.subplot(G[1, 3])
ax5.imshow(color_th, cmap = 'gray')
ax5.set_title('Filtered Image', fontsize = 20)

# fine tune the figure
plt.subplots_adjust(left = 0.03, right = 0.98, top = 0.98, bottom = 0.03)
plt.subplots_adjust(hspace = 0, wspace = 0.13)

# show figure
plt.show()