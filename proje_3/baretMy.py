from ultralytics import YOLO
import cv2

model = YOLO('C:/Users/Yalın/Desktop/vsc/python/my_train_best.pt')

cap = cv2.VideoCapture(0)

CONFIDENCE_THRESHOLD = 0.5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        conf = float(box.conf[0])  
        if conf < CONFIDENCE_THRESHOLD:
            continue  

        cls = int(box.cls[0])
        label = model.names[cls].lower()

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if label == 'hardhat' or label == 'baretli': 
            color = (0, 255, 0) 
            text = f'Baretli {conf:.2f}'
        else:
            color = (0, 0, 255)
            text = f'Baretsiz {conf:.2f}'


        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        cv2.putText(frame, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow('Baret Tespiti', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
