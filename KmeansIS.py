import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
image = cv2.imread("face.jpg")

# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image.reshape((-1, 3))
# convert to float
pixel_values = np.float32(pixel_values)

# define stopping criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# number of clusters (K)
for i in range (2,21):
  if i==2 or i==3 or i==5 or i==10 or i==15 or i==20:

    k = i
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # convert back to 8 bit values
    centers = np.uint8(centers)

    # flatten the labels array
    labels = labels.flatten()

    # convert all pixels to the color of the centroids
    newimage = centers[labels.flatten()]

    # reshape back to the original image dimension
    newimage = newimage.reshape(image.shape)
    # show the image
    print("Image for K=",i)
    plt.imshow(newimage)
    plt.show()
