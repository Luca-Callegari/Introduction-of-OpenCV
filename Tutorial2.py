# What this file will contain?
'''
1) Structure of an Image
2) Modifying an Image like changing the pixel values
3) Copy and Paste an Image
4) 
'''

import cv2
import random

def display_image(image, titolo="Immagine"):
    """
    Mostra un'immagine in una finestra e la chiude premendo un tasto qualsiasi.
    
    Parametri:
    - image: L'immagine caricata (un array NumPy)
    - titolo: Il titolo della finestra (opzionale)
    """

    cv2.imshow(titolo, image)
    # How to close the image window? cv2.waitKey(0) will wait for a key press indefinitely. If you pass a number, it will wait for that many milliseconds.
    # In this case, we will wait indefinitely for a key press.
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# --------------------------------------------------







img = cv2.imread('immagini/UbuntuSfondo.png', 1)  # Load an image from file
 
# -------------------- STRUCTURE OF AN IMAGE ----------------------

print(type(img))  # Print the type of the image array -> numpy.ndarray

print(img.shape)  # Print the shape of the image array -> (height, width, channels)
# where channels = 3 for BGR images and channels = 4 for BGRA images
# and height and width are the dimensions of the image in pixels, each pixel is represented by a 3D array of values corresponding to the color channels.
# For example, an image with the shape (2,2,3) would have 2 rows and 2 columns of pixels, 
# with each pixel represented by a 3D array of values corresponding to the BGR color channels.
# [
#  [[  0   0   0] [255 255 0]]
#  [[  0   255   0] [255 0 255]]
# ]
# is an example of a 2x2 image with 3 color channels (BGR). The first pixel has the color black (0,0,0), 
# the second pixel has the color yellow (255,255,0), the third pixel has the color green (0,255,0), 
# and the fourth pixel has the color magenta (255,0,255).

# Note: when you rotate an image, you are just transpose the np.array, so the shape of the image will change accordingly. For example, if you rotate a 2x3 image, the shape will become 3x2.

print(img[0, 0])  # Print the pixel value at (0,0) 

# -------------------------------------------------------------------------------

#  ------------- MODIFYING THE IMAGE (CHANGE PIXEL VALUES) ------------------
for i in range(100):  # Loop through the rows of the image (first 100 rows)
    for j in range(100):  # Loop through the columns of the image (first 100 columns)
        img[i, j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]  # Set the pixel value at (i,j) to a random color (BGR)

# ----------------------------------------------------------------------------------------------------------

display_image(img, 'Modified Image') 

# --------------------- COPY AND PASTE AN IMAGE ----------------------
# Want to copy a part of the image and paste it somewhere else in the same image
tag = img[0:100, 0:100]  # Copy the first 100 rows and 100 columns of the image
img[100:200, 100:200] = tag  # Paste the copied part


display_image(img, 'Copy and Paste Image')  