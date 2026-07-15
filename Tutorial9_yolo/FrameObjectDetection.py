
'''
This script demonstrates how to perform object detection on an image using the YOLOv8 model from the Ultralytics library.

The primary difference between this and the Haar Cascade Classifier (used in Tutorial 8) is the underlying 
technology: a Haar Cascade is a traditional machine learning algorithm that requires specific .xml files to detect 
predefined objects. In contrast, YOLOv8 is a pre-trained deep neural network that has already learned the optimal 
parameters to detect over 80 different object categories out of the box.

'''

from ultralytics import YOLO
import cv2

# Configure target class and image path

target_class = "person"  # Specify the target class you want to detect
image_path = "immagini/persona.jpg"  # Replace with the path to your image
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

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image.")
    exit()

# Perform object detection on the image
results = model(image, classes=[class_id], conf=confidence_threshold, verbose=False)
# where the inputs are the image, the class ID of the target class, the confidence threshold, and verbose set to False to suppress detailed output;
# and the output is stored in the results variable which conteins the detection results.

print(results)  # Print the detection results for debugging purposes


# Draw bounding boxes and labels on the image for detected objects

found = 0  # Initialize a counter for found objects

for r in results: # Iterate through each detection result
    for box in r.boxes: # Iterate through each bounding box in the result

        # For instance, if r.boxes contains 3 elements, the inner loop will run 3 times, once for each target class 
        # detected in the image. Each box represents a detected object, and the loop allows you to access the coordinates 
        # and confidence score of each detected object.

        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get the coordinates of the bounding box

        # box.xyxy is a matrix that contains the coordinates of the bounding box in the format [[x1, y1, x2, y2]].
        # Therefore, box.xyxy[0] retrieves the first (and only) row of the matrix, which contains the coordinates of the bounding box.
        # Then map(int, ...) converts the coordinates to integers, and the result is unpacked into the variables x1, y1, x2, and y2.

        confidence = float(box.conf[0])  # Get the confidence score of the detection

        # box.conf is a matrix that contains the confidence scores of the detected objects in the format [[confidence_score]]. 
        # Therefore, box.conf[0] retrieves the first (and only) row of the matrix, which contains the confidence score of the detected object.

        found += 1  # Increment the count of found objects

        # Draw the bounding box on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw a green rectangle with thickness of 2
        label = f"{target_class}: {confidence:.2f}"  # Create a label
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Put the label above the bounding box

if found == 0:
    print(f"No '{target_class}' detected in the image.")

# Display the image with detected objects
cv2.imshow("Detected Objects", image)  # Show the image in a window
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
