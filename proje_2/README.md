# Canlı Renk Algılayıcı (HSV)

Bu proje, bilgisayarın kamerasını kullanarak canlı video akışı üzerinde tıklanan noktanın rengini tespit eder. Renk tespiti HSV renk uzayında yapılır ve renk adı ile birlikte RGB değerleri ekranda gösterilir.

## Özellikler

- Canlı kamera görüntüsü üzerinde herhangi bir noktaya tıklayarak renk tespiti yapabilirsiniz.  
- HSV değerine göre renk adı belirlenir (Kırmızı, Turuncu, Sarı, Yeşil, Mavi, Mor, Siyah, Beyaz).  
- Tıklanan noktanın RGB değerleri de ekranda gösterilir.  

## Gereksinimler

- Python 3.x  
- OpenCV  
- Pillow  
- NumPy  

Kurulum için:  
```pip install opencv-python pillow numpy```

## Kullanım

1. Kod dosyasını kaydedin, örneğin `renk_algilayici.py`.  
2. Terminalden çalıştırın:

```python renk_algilayici.py```

3. Kamera açılacak, görüntü üzerinde bir noktaya tıkladığınızda renk adı ve RGB değeri üstte görüntülenecektir.  

## Kodun İşleyişi

- Kamera görüntüsü alınır ve tkinter penceresi içinde gösterilir.  
- Tıklama ile koordinatlar alınır ve o pikselin RGB değeri çıkarılır.  
- RGB değeri HSV uzayına dönüştürülerek renk adı belirlenir.  
- Renk adı ve RGB değeri arayüzde gösterilir.  

## Tuşlar

- Pencereyi kapatarak uygulamayı sonlandırabilirsiniz.
