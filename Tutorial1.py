# Cosa conterrà questo file?
'''
1) Loading an Image
2) Displaying an Image
3) Resizing an Image
4) Rotating an Image
5) Saving an Image

'''

import cv2

# ------------------- Functions -------------------

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




# Load an image
# Principal mode of reading
'''
1) -1 -> cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It is the default flag.
2) 0 -> cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode
3) 1 -> cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel
'''
image = cv2.imread('immagini/UbuntuSfondo.png', 0)  # Load in grayscale mode

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")

# Resize the image by number of pixels (width, height)
# resized_image = cv2.resize(image, (400, 400))  # Resize to 400x400

# Resize the image by a scale factor (fx, fy)
resized_image = cv2.resize(image, None, fx=0.5, fy=0.5)  # Resize to half the size

# Rotate the image by 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Save the image
# cv2.imwrite('resized_image.png', resized_image)
# cv2.imwrite('rotated_image.png', rotated_image)

# Display the image
display_image(image, "Original Image")

# Display the resized image
display_image(resized_image, "Resized Image")

# Display the rotated image
display_image(rotated_image, "Rotated Image")

