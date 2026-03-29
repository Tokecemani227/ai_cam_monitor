from ultralytics import YOLO
import cv2
import csv
from datetime import datetime

# Pakai yolov8 nano
model = YOLO('yolov8n.pt')

# Setup
url = "http://192.168.101.11:8080/video" 
cap = cv2.VideoCapture(url)

log_file = "detections_log.csv"

def write_log(obj_name, confidence):
    with open(log_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, obj_name, f"{confidence:.2f}"])

with open(log_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Object', 'Confidence'])


window_name = "AI Object Detection - (Press Q to Exit)"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

#print("Memulai deteksi... Tekan 'q' untuk berhenti.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

   
    results = model(frame, stream=True, verbose=False)


    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls]

            if conf> 0.5:
                write_log(name, conf)
                print(f"Logged: {name} ({conf:.2f})")
        
        annotated_frame = r.plot()

    cv2.imshow(window_name, annotated_frame)

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()