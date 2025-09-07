# Yüz Tespiti Uygulaması

Bu proje, OpenCV kütüphanesini kullanarak gerçek zamanlı yüz tespiti yapan basit bir Python uygulamasıdır. Bilgisayarın kamerasını kullanarak yüzleri algılar ve ekran üzerinde yeşil dikdörtgenler ile gösterir.

## Gereksinimler

- Python 3.x  
- OpenCV kütüphanesi  

Kurulum için:  

```pip install opencv-python```


## Kullanım

1. `haarcascade_frontalface_default.xml` dosyasının yolunu kodda doğru şekilde güncelleyin.  
2. Python dosyasını çalıştırın:
```python face_detection.py```
3. Kamera açılacak ve gerçek zamanlı olarak yüzleri algılayacaktır.  

## Tuşlar

- **ESC (Escape)** tuşuna basarak uygulamayı kapatabilirsiniz.

## Kodun İşleyişi

- Kamera görüntüsü alınır.  
- Görüntü gri tonlamaya dönüştürülür.  
- Haar Cascade sınıflandırıcısı kullanılarak yüzler tespit edilir.  
- Tespit edilen yüzlerin etrafına yeşil dikdörtgen çizilir.  
- Üst köşede tespit edilen yüz sayısı gösterilir.  
