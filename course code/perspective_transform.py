import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

from helper_functions import perspect_transform

# read the grid image
image = mpimg.imread('example_grid1.jpg')

# define source point
src_left_bottom = [15.629, 141.177]
src_left_top = [118.855, 96.0161]
src_right_top = [199.5, 96.6613]
src_right_bottom = [301.435, 141.177]

source = np.float32([src_left_bottom, src_left_top,
                    src_right_top, src_right_bottom])

# define destination point
image_center_x = image.shape[0] / 2
image_near_bottom_y = image.shape[1] - 10

des_left_bottom = [image_center_x - 5, image_near_bottom_y]
des_left_top = [des_left_bottom[0], des_left_bottom[1] - 10]
des_right_top = [des_left_top[0] + 10, des_left_top[1]]
des_right_bottom = [des_right_top[0], des_right_top[1] + 10]

destination = np.float32([des_left_bottom, des_left_top,
                         des_right_top, des_right_bottom])
# get warped image
warped_image = perspect_transform(image, source, destination)

# draw source and destination points on images
# draw source in blue
cv2.polylines(image, np.int32([source]), True, (0, 0, 255), 3)
# draw destination in green
cv2.polylines(warped_image, np.int32([destination]), True, (0, 255, 0), 3)

# display figure
f, (ax1, ax2) = plt.subplots(1, 2, figsize = (24, 6), sharey= True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize = 40)

ax2.imshow(warped_image, cmap = 'gray')
ax2.set_title('Warped Image', fontsize = 40)
plt.subplots_adjust(left = 0.03, right = 0.58, top = 0.9, bottom = 0.05)
plt.show()
