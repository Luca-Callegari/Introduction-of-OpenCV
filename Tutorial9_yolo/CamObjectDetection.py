'''
This script demonstrates how to perform object detection on a video stream (webcam or video file)
using the YOLOv8 model from the Ultralytics library.

The primary difference between this and the Haar Cascade Classifier (used in Tutorial 8) is the underlying 
technology: a Haar Cascade is a traditional machine learning algorithm that requires specific .xml files to detect 
predefined objects. In contrast, YOLOv8 is a pre-trained deep neural network that has already learned the optimal 
parameters to detect over 80 different object categories out of the box.

The difference between this script and the static image version is that here we read frames continuously
from a video source (webcam or .mp4 file) in a loop, and run detection on each individual frame, instead
of running detection just once on a single image.
'''

from ultralytics import YOLO
import cv2

# Configure target class and video source

target_class = "person"  # Specify the target class you want to detect
video_source = 0  # 0 = default webcam. Replace with a file path (e.g. "immagini/video.mp4") to use a video file instead
confidence_threshold = 0.5  # Set the confidence threshold for detection

# Load the YOLO model
model = YOLO("yolov8n.pt")  # Load the YOLOv8n model (you can choose a different model if needed)

#print(model.names)  # Print the class names to verify the target class

# Find the class index for the target class
class_id = None
for idx, class_name in model.names.items():
    if class_name == target_class:
        class_id = idx
        break

print(f"Class ID for '{target_class}': {class_id}")

# Open the video source (webcam or file)
cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()



while True:

    ret, frame = cap.read()  # Read a single frame from the video source
    # ret is a boolean indicating whether the frame was read successfully;
    # frame is the actual image data of that frame (same format as an image read with cv2.imread).

    if not ret:
        print("End of stream (video finished or webcam disconnected).")
        break

    # Perform object detection on the current frame
    results = model(frame, classes=[class_id], conf=confidence_threshold, verbose=False)
    # where the inputs are the frame, the class ID of the target class, the confidence threshold, and verbose set to False to suppress detailed output;
    # and the output is stored in the results variable which conteins the detection results.

    # Draw bounding boxes and labels on the frame for detected objects

    found = 0  # Initialize a counter for found objects (reset every frame)

    for r in results: # Iterate through each detection result
        for box in r.boxes: # Iterate through each bounding box in the result

            # For instance, if r.boxes contains 3 elements, the inner loop will run 3 times, once for each target class 
            # detected in the frame. Each box represents a detected object, and the loop allows you to access the coordinates 
            # and confidence score of each detected object.

            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get the coordinates of the bounding box

            # box.xyxy is a matrix that contains the coordinates of the bounding box in the format [[x1, y1, x2, y2]].
            # Therefore, box.xyxy[0] retrieves the first (and only) row of the matrix, which contains the coordinates of the bounding box.
            # Then map(int, ...) converts the coordinates to integers, and the result is unpacked into the variables x1, y1, x2, and y2.

            confidence = float(box.conf[0])  # Get the confidence score of the detection

            # box.conf is a matrix that contains the confidence scores of the detected objects in the format [[confidence_score]]. 
            # Therefore, box.conf[0] retrieves the first (and only) row of the matrix, which contains the confidence score of the detected object.

            found += 1  # Increment the count of found objects

            # Draw the bounding box on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw a green rectangle with thickness of 2
            label = f"{target_class}: {confidence:.2f}"  # Create a label
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Put the label above the bounding box

    # Display the frame with detected objects
    cv2.imshow("Detected Objects", frame)  # Show the frame in a window

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video source and close all windows
cap.release()
cv2.destroyAllWindows()