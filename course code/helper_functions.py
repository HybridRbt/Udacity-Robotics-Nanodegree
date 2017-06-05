import cv2
import numpy as np

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