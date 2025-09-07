import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

def get_color_name_hsv(R, G, B):
    color = np.uint8([[[B, G, R]]])
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = hsv

    if s < 50 and v > 200:
        return "Beyaz"
    elif v < 50:
        return "Siyah"
    elif h < 10 or h > 160:
        return "Kırmızı"
    elif 10 <= h < 25:
        return "Turuncu"
    elif 25 <= h < 35:
        return "Sarı"
    elif 35 <= h < 85:
        return "Yeşil"
    elif 85 <= h < 130:
        return "Mavi"
    elif 130 <= h < 160:
        return "Mor"
    else:
        return "Tanımsız"

class RenkAlgilayici:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Canlı Renk Algılayıcı (HSV)")
        
        self.video_label = tk.Label(self.pencere)
        self.video_label.pack()

        self.renk_etiket = tk.Label(self.pencere, text="Tıklanan yerin rengi burada görünecek", font=("Arial", 14))
        self.renk_etiket.pack(pady=10)

        self.cap = cv2.VideoCapture(0)
        self.video_label.bind("<Button-1>", self.tikla)
        self.guncelle()

    def tikla(self, event):
        if hasattr(self, "frame_rgb"):
            x = event.x
            y = event.y
            try:
                renk = self.frame_rgb[y, x]
                R, G, B = renk
                renk_adi = get_color_name_hsv(R, G, B)
                self.renk_etiket.config(
                    text=f"Renk: {renk_adi} | RGB: ({R}, {G}, {B})"
                )
            except:
                pass

    def guncelle(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.frame_rgb = frame.copy()

            im = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=im)
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)

        self.pencere.after(10, self.guncelle)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

pencere = tk.Tk()
uygulama = RenkAlgilayici(pencere)
pencere.mainloop()
