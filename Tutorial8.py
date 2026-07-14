# What we want to do?

'''
Live Face and Eye Detection using Haar Cascade Classifiers in OpenCV.
'''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Start video capture from the default camera (index 0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Load the Haar cascade for face detection
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  # Load the Haar cascade for eye detection

if face_cascade.empty():
    raise IOError("Impossibile caricare il file xml del classificatore.")
if eye_cascade.empty():
    raise IOError("Impossibile caricare il file xml del classificatore.")

while True:
    ret, frame = cap.read()  # Read a frame from the video capture
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  # Detect faces in the grayscale image
    # Where scaleFactor is the amount by which the image is scaled at each iteration, and minNeighbors is the minimum number of neighbors a detection must have to be considered valid

    # Now we want to draw rectangles around the detected faces and eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around each detected face
        roi_gray = gray[y:y + h, x:x + w]  # Region of interest in grayscale for eyes, these are the coordinates of the detected face
        roi_color = frame[y:y + h, x:x + w]  # Region of interest in color for eyes

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)  # Detect eyes within the face region

        # Now we want to draw rectangles around the detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Draw a rectangle around each detected eye

    cv2.imshow('Face and Eye Detection', frame)  # Display the frame with detected faces and eyes

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit the loop when 'q' is pressed
        break