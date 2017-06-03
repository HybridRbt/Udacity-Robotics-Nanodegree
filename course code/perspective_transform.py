import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# read the grid image
image = mpimg.imread('example_grid1.jpg')


# define transform function
def perspect_transform(img, src, dst):
    # get transform matrix
    M = cv2.getPerspectiveTransform(src, dst)

    # warp image, keep the same size
    shape = image.shape
    warped = cv2.warpPerspective(img, M, (shape[0], shape[1]))

    return warped


# define source point
src_left_bottom = [15.629, 141.177]
src_left_top = [118.855, 96.0161]
src_right_top = [199.5, 96.6613]
src_right_bottom = [301.435, 141.177]

source = np.float32(src_left_bottom, src_left_top,
                    src_right_top, src_right_bottom)

# define destination point
image_center_x = image.shape[0] / 2
image_near_bottom_y = image.shape[1] - 10

des_left_bottom = [image_center_x - 5, image_near_bottom_y]
des_left_top = [des_left_bottom[0], des_left_bottom[1] - 10]
des_right_top = [des_left_top[0] + 10, des_left_top[1]]
des_right_bottom = [des_right_top[0], des_right_top + 10]

destination = np.float32(des_left_bottom, des_left_top,
                         des_right_top, des_right_bottom)
# get warped image
warped_image = perspect_transform(image, source, destination)
