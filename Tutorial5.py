# What this code does:
'''
1) Convert a BGR image to a HSV image
2) Create a mask that only includes a specific color in that range
3) Apply the mask to the original image to get the result
4) Display the HSV image and the result image in a window

-> EXTRACT A COLOR FROM AN IMAGE OR A VIDEO STREAM
-> COLOR DETECTION

'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # Open the default webcam

while True:
    ret, frame = cap.read()  # Read a frame from the webcam, where frame is a numpy array

    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    # ----- Convert the BGR image to a HSV image ------
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the BGR image to a HSV image
    lower_blue = np.array([90, 50, 50])  # Define the lower bound of the blue color in HSV
    upper_blue = np.array([130, 255, 255])  # Define the upper bound of the blue color in HSV

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # Create a mask that only includes the blue color in that range, 
    # it tells which pixels are in the range and which are not, the pixels that are in the range will be white (255) and the pixels that are not in the range will be black (0)

    result = cv2.bitwise_and(frame, frame, mask=mask)  # Apply the mask to the original frame to get the result
    # In general, the bitwise_and operation is used to combine two images based on a mask. In this case, we are using the mask to keep only the blue pixels in the original frame and set all other pixels to black.

    #------------------------

    cv2.imshow('HSV Stream', hsv)  # Display the HSV frame in a window
    cv2.imshow('Result Stream', result)  # Display the result frame in a window
    cv2.imshow('Mask', mask)  # Display the mask in a window

    # Notice that the mask is a binary image, where the white pixels represent the blue color in the original frame and the black pixels represent 
    # all other colors. Infact when i dispay the mask image i can see that the white pixels are in the shape of the blue object in the original frame.

    # The result frame is the original frame with only the blue pixels visible and all other pixels set to black.

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows

# Notice: if i wanna detect a different color, i have to change the lower and upper bounds of the color in HSV. 
# For example, if i wanna detect red color, i have to change the lower and upper bounds to: 
# lower_red = np.array([0, 50, 50])
# upper_red = np.array([10, 255, 255])
