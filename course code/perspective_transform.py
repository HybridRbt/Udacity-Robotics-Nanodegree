import cv2
import matplotlib.image as mpimg

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
left_bottom = [15.629, 141.177]
left_top = [118.855, 96.0161]
right_top = [199.5, 96.6613]
right_bottom = [301.435, 141.177]
