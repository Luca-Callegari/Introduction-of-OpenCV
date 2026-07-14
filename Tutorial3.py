# What this file will contain?
'''
1) Load a webcam 
2) Duplicate the webcam stream
3) Paste rotated the webcam stream in a window

'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # Open the default webcam
# If you have multiple webcams, you can change the index to 1, 2, etc. to access the other webcams.

# If you want to use a video file instead of a webcam, you can use the following code:
# cap = cv2.VideoCapture('video.mp4')  # Open a video file

while True:

    ret, frame = cap.read()  # Read a frame from the webcam, where frame is a numpy array 
    # representing the image and ret is a boolean indicating if the frame was read successfully.

    if not ret:
        print("Error: Could not read frame.")
        break

    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    # Now i want to have four of me on the screen, and rotate the web cam 
    image = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)  # Create a black image of the same size of the webcam frame
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)  # Resize the webcam frame to half its size

    image[0:height//2, 0:width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Paste the smaller frame in the top-left corner
    image[0:height//2, width//2:width] = smaller_frame # Paste the smaller frame in the top-right corner
    image[height//2:height, 0:width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Paste the smaller frame in the bottom-left corner
    image[height//2:height, width//2:width] = smaller_frame # Paste the smaller frame in the bottom-right corner

    # Display the original frame in a window
    cv2.imshow('Webcam Stream', image)

    # Wait for 1 ms and check if the user pressed the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows


