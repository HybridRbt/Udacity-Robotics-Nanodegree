import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from helper_functions \
    import perspect_transform, color_thresh, source, destination, image, rover_coords

# perform warping and color threshold
warped_image = perspect_transform(image, source, destination)
color_sel_image = color_thresh(warped_image, rgb_thresh=(160, 160, 160))

# show the filtered image first
plt.imshow(color_sel_image, cmap='gray')
plt.show()

# get x, y pos and convert
xpos, ypos = rover_coords(color_sel_image)

# show figure
fig = plt.figure(figsize=(20, 10))
plt.plot(xpos, ypos, '.')
plt.ylim(-160, 160)
plt.xlim(0, 300)
plt.title('Rover-Centric Map', fontsize=20)
plt.show()


