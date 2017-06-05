import cv2
import numpy as np
import matplotlib.image as mpimg

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

# define transform function
def perspect_transform(img, src, dst):
    # get transform matrix
    M = cv2.getPerspectiveTransform(src, dst)

    # warp image, keep the same size
    shape = img.shape
    warped = cv2.warpPerspective(img, M, (shape[0], shape[1]))

    return warped

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

# define the function to convert coords
def rover_coords(binary_image):
    # get non-zero pixels
    # note: the tuple returned by nonzero() is indexed by row, which means ypos comes first
    ypos, xpos = binary_image.nonzero()

    # get length and height of image
    length = binary_image.shape[1]
    height = binary_image.shape[0]

    # 1. shift
    xpos1 = xpos - length / 2
    ypos1 = ypos - height

    # 2. mirror along y
    xpos2 = -xpos1
    ypos2 = ypos1

    # 3. rotate +90 degree
    xpos3 = -ypos2
    ypos3 = xpos2

    return xpos3.astype(np.float), ypos3.astype(np.float)