# import libs
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

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

# define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    # create an empty array the same size in x and y as the image but only has one channel
    color_select = np.zeros_like(img[:, :, 0])

    # create the filter for each color
    red_thresh = img[:, :, 0] > rgb_thresh[0]
    green_thresh = img[:, :, 1] > rgb_thresh[1]
    blue_thresh = img[:, :, 2] > rgb_thresh[2]

    # combine the filter
    thresh = red_thresh & green_thresh & blue_thresh

    # set the pixels
    color_select[thresh] = 1

    return color_select

# show figure
plt.show()