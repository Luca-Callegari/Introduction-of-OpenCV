# What does this code do?
'''
This code performs template matching on an image using various methods available in OpenCV.
So, it loads an image and a template, and then it applies different template matching methods to find the location of the template in the image.
These algorithms works if and only if the template is cut based on the image, otherwise it will not work: this is the limitation of this technique. 
'''

import numpy as np
import cv2

img = cv2.resize(cv2.imread('immagini/soccer_practice.jpg', 0), (0, 0), fx=0.9, fy=0.9)  # Load an image from file in grayscale
template = cv2.resize(cv2.imread('immagini/shoe.png', 0), (0, 0), fx=0.8, fy=0.8)  # Load a template image from file in grayscale

# Pay attention: the images are resized because the original images are too big. You can change the resizing factors (fx, fy) to fit your needs.

if img is None:
    raise FileNotFoundError("Non sono riuscito a caricare 'soccer_practice.jpg'.")
if template is None:
    raise FileNotFoundError("Non sono riuscito a caricare 'shoe.png'.")

h, w = template.shape  # Get the height and width of the template image

# There are lots of methods available in OpenCV for template matching, such as:
# cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for method in methods:
    img2 = img.copy()  # Reset the image to the original copy for each method

    result = cv2.matchTemplate(img2, template, eval(method))  # Perform template matching, returning a result matrix with dimensions (W-w+1, H-h+1) where W and H are the width and height of the input image, 
    # and w and h are the width and height of the template image.
    # These function does a convolution between the template and the image, and returns a matrix of similarity scores. 
    # We can imagine this as sliding the template over the image and computing a similarity score at each position.

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # Find the minimum and maximum values and their locations in the result matrix

    if method in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
        location = min_loc  # For these methods, the best match is the minimum value
    else:
        location = max_loc  # For other methods, the best match is the maximum value

    cv2.rectangle(img2, location, (location[0] + w, location[1] + h), 255, 5)  # Draw a rectangle around the matched region in the image
    
    cv2.imshow(method, img2)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

