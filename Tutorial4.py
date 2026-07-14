# What this file will contain?

''' Drawing lines, rectangles, circles, text and other shapes on an image using OpenCV'''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Open the default webcam

while True:
    
    ret, frame = cap.read()  # Read a frame from the webcam, where frame is a numpy array 
    # representing the image and ret is a boolean indicating if the frame was read successfully.

    if not ret:
        print("Error: Could not read frame.")
        break

    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    # Draw a line on the frame and return the modified frame. The line will be drawn from the top-left corner to the bottom-right corner of the frame, with a blue color and a thickness of 5 pixels.
    image = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5) 

    # Draw a line on the previous modified frame and return the modified frame. The line will be drawn from the top-right corner to the bottom-left corner of the frame, with a green color and a thickness of 5 pixels.
    image = cv2.line(image, (width, 0), (0, height), (0, 255, 0), 5) 

    # Draw a rectangle on the previous modified frame and return the modified frame. The rectangle will be drawn from the top-left corner to the bottom-right corner of the frame, with a gray color and a thickness of 5 pixels.
    image = cv2.rectangle(image, (100, 100), (200, 200), (128, 128, 128), 5)

    # Draw a circle on the previous modified frame and return the modified frame. The circle will be drawn at the center of the frame, with a radius of 50 pixels, a red color and a thickness of 5 pixels.
    image = cv2.circle(image, (width//2, height//2), 50, (0, 0, 255), -1)  # -1 means that the circle will be filled with the color

    # Draw text on the previous modified frame and return the modified frame. The text will be drawn at the bottom-left corner of the frame, with a font size of 1, a white color and a thickness of 2 pixels.
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'Luco', (10, height - 10), font, 4, (255, 255, 255), 5, cv2.LINE_AA)  # cv2.LINE_AA is an anti-aliased line type

    # Display the modified frame in a window
    cv2.imshow('Webcam Stream with Drawing', image)

    # Wait for 1 ms and check if the user pressed the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break