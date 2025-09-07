import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split

okey_folder = "C:/ok_fotos"
notokey_folder = "C:/nok_fotos"
os.makedirs(okey_folder, exist_ok=True)
os.makedirs(notokey_folder, exist_ok=True)

model_path = r"C:\Users\Yalın\Desktop\vsc\python\okey_model.h5"

def load_trained_model():
    try:
        return load_model(model_path)
    except Exception as e:
        messagebox.showwarning("Model Yükleme", f"Model yüklenemedi: {e}")
        return None

model = load_trained_model()

IMG_SIZE = (128, 128)

template_path = r"C:\kullanilabilirler\template_ok.png"
template = cv2.imread(template_path, cv2.IMREAD_COLOR)
if template is None:
    messagebox.showwarning("Template Yükleme", f"{template_path} bulunamadı! Template matching devre dışı.")
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) if template is not None else None
w, h = template_gray.shape[::-1] if template_gray is not None else (0, 0)

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r"C:\kullanilabilirler\haarcascade_frontalface_default.xml")

def predict_image(frame):
    resized = cv2.resize(frame, IMG_SIZE)
    normalized = resized / 255.0
    input_data = np.expand_dims(normalized, axis=0)
    prediction = model.predict(input_data)[0][0]
    return prediction

def get_next_index(folder_name):
    files = [f for f in os.listdir(folder_name) if f.lower().endswith(".jpg") and f.startswith("image")]
    numbers = []
    for f in files:
        try:
            num = int(f.replace("image", "").replace(".jpg", ""))
            numbers.append(num)
        except:
            pass
    return max(numbers, default=0) + 1

def update_frame():
    ret, frame = cap.read()
    if ret:
        if model:
            try:
                pred = predict_image(frame)
                if pred > 0.5:
                    label = "Okey"
                    color = (0, 255, 0)
                else:
                    label = "Not Okey"
                    color = (0, 0, 255)
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.8
                thickness = 2
                text_size, _ = cv2.getTextSize(label, font, font_scale, thickness)
                text_x = frame.shape[1] - text_size[0] - 10
                text_y = 30
                cv2.putText(frame, label, (text_x, text_y), font, font_scale, color, thickness)
            except Exception:
                cv2.putText(frame, "Tahmin Hatası", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
        else:
            cv2.putText(frame, "Model Yüklenmedi", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        gray_for_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_for_face, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w_f, h_f) in faces:
            cv2.rectangle(frame, (x, y), (x+w_f, y+h_f), (255, 0, 0), 2)
            cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

        if template_gray is not None:
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
                cv2.putText(frame, "OK", (pt[0], pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)

    root.after(30, update_frame)

def select_and_capture(folder_name):
    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Hata", "Kamera görüntü alınamadı!")
        return

    roi = cv2.selectROI("Bölge Seç", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Bölge Seç")

    x, y, w, h = roi
    if w == 0 or h == 0:
        messagebox.showwarning("İptal", "Hiçbir alan seçilmedi.")
        return

    cropped = frame[y:y+h, x:x+w]
    index = get_next_index(folder_name)
    filename = os.path.join(folder_name, f"image{index}.jpg")
    cv2.imwrite(filename, cropped)
    messagebox.showinfo("Başarılı", f"Kırpılmış görüntü kaydedildi:\n{filename}")

def okey_button_clicked():
    select_and_capture(okey_folder)

def notokey_button_clicked():
    select_and_capture(notokey_folder)

def retrain_model():
    global model
    data = []

    def load_images(folder, label):
        imgs = []
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            img = cv2.imread(path)
            if img is not None:
                img = cv2.resize(img, IMG_SIZE)
                imgs.append((img, label))
        return imgs

    data += load_images(okey_folder, 1)
    data += load_images(notokey_folder, 0)

    if len(data) < 10:
        messagebox.showwarning("Yetersiz Veri", "Modeli eğitmek için daha fazla veri gerekiyor!")
        return

    np.random.shuffle(data)
    X = np.array([item[0] for item in data]) / 255.0
    y = np.array([item[1] for item in data])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    messagebox.showinfo("Eğitim", "Model eğitiliyor, lütfen bekleyin...")

    new_model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    new_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    new_model.fit(X_train, y_train, epochs=10, batch_size=16, validation_data=(X_test, y_test), verbose=0)

    new_model.save(model_path)
    model = new_model

    messagebox.showinfo("Başarılı", "Model başarıyla güncellendi!")

root = tk.Tk()
root.title("Okey / Not Okey Tanıma Sistemi")
root.geometry("950x550")
root.resizable(False, False)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

camera_label = tk.Label(main_frame)
camera_label.pack(side=tk.LEFT, padx=10, pady=10)

button_frame = tk.Frame(main_frame)
button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=30, pady=10)

info_label = tk.Label(button_frame, text="Fotoğraflar", font=("Arial", 14))
info_label.pack(pady=10)

btn_okey = tk.Button(button_frame, text="Okey Fotoğrafı Çek", bg="green", fg="white", font=("Arial", 12), width=25, height=2, command=okey_button_clicked)
btn_okey.pack(pady=10)

btn_notokey = tk.Button(button_frame, text="Not Okey Fotoğrafı Çek", bg="red", fg="white", font=("Arial", 12), width=25, height=2, command=notokey_button_clicked)
btn_notokey.pack(pady=10)

btn_retrain = tk.Button(button_frame, text="Modeli Güncelle", bg="blue", fg="white", font=("Arial", 12), width=25, height=2, command=retrain_model)
btn_retrain.pack(pady=20)

update_frame()
root.mainloop()

cap.release()
cv2.destroyAllWindows()