# Traffic Detection using YOLOv8

🚗 Real-time object detection from traffic videos using the YOLOv8 Nano model.

## 🔧 Technologies Used
- Python
- OpenCV
- Ultralytics YOLOv8
- Google Colab (for initial testing)

## 📹 How it Works
1. Load a YOLOv8 Nano model (`yolov8n.pt`)
2. Read a video frame-by-frame using OpenCV
3. Perform detection on each frame
4. Annotate and save the output video

## 📝 Output
The final video is saved with all detections annotated.

## 📂 Example
Make sure to replace the video path:
```python
video_path = "your_input_video.mp4"
