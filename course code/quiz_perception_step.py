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

# create a figure for plotting
fig = plt.figure(figsize=(5, 10))

# plot red channel
plt.subplot(311)
plt.imshow(red_channel)

# plot green channel
plt.subplot(312)
plt.imshow(green_channel)

# plot blue channel
plt.subplot(313)
plt.imshow(blue_channel)

# show figure
plt.show()