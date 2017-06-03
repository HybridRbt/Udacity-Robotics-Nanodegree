# import libs
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# define file names
filename = "sample.jpg"
image = mpimg.imread(filename)  # read file
plt.imshow(image) #show image
plt.show()