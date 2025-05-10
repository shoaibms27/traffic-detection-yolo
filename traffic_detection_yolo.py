#pip install ultralytics opencv-python numpy tqdm

from ultralytics import YOLO
model = YOLO("yolov8n.pt")  # 'n' = nano, fastest and lightweight

import cv2
from google.colab.patches import cv2_imshow
import time
from ultralytics import YOLO
import numpy as np

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Input video path
video_path = "/content/img/27260-362770008_tiny.mp4"

# Output video path
output_path = "/content/output_video.mp4"

# Open the input video
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Process the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform YOLO detection
    results = model(frame)

    # Get the annotated frame
    annotated_frame = results[0].plot()

    # Write the annotated frame to the output video
    out.write(annotated_frame)

    # Display the annotated frame (
    # cv2_imshow(annotated_frame)
    # time.sleep(0.01) # Adjust the delay


# Release resources
cap.release()
out.release()
# cv2.destroyAllWindows()

print(f"Output video saved to: {output_path}")



