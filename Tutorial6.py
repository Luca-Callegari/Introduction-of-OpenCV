# What this file will contain?
''' 
Corner detection
'''

import numpy as np
import cv2


img = cv2.imread('immagini/scacchiera.png')  # Load an image from file
img = cv2.resize(img, (0,0) , fx=1.5, fy=1.5)  # Resize the image

# Everytime we have to deal with corner detecion, we have to convert the image to grayscale, because the corner detection algorithm works on a single channel image.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)  # Detect corners in the image
# where the first parameter is the image, the second parameter is the maximum number of corners to return, 
# the third parameter is the quality level, and the fourth parameter is the minimum distance between corners.

# Notice that the corners variable is a numpy array of floats
print(corners)  # Print the corners detected in the image
# But we want to convert the corners to integers, because we want to draw circles on the corners, and the circle function takes integers as parameters.
corners = np.int32(corners)  # Convert the corners to integers

# Now we have to decompose the corners array, because it is a 3D array, and we want to iterate over the corners and draw circles on them.
for corner in corners:
    x, y = corner.ravel()  # Decompose the corner array to get the x and y coordinates of the corner, ravel() flattens the array to 1D, so we can unpack the x and y coordinates.
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)  # Draw a circle on the corner

# Now we want to draw lines between the corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))  # Generate a random color for the line
        cv2.line(img, corner1, corner2, color, 1)  # Draw a line between the corners


cv2.imshow('Grayscale Image', img)  # Display the grayscale image in a window
cv2.waitKey(0)  # Wait for a key press indefinitely
cv2.destroyAllWindows()  # Close all OpenCV windows
