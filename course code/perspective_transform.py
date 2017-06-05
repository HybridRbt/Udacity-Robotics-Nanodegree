import cv2

import matplotlib.pyplot as plt
import numpy as np

from helper_functions import perspect_transform, source, destination, image

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
