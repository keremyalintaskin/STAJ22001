# Baret Tespiti Uygulaması (YOLOv8)

Bu proje, YOLOv8 modeli ve OpenCV kullanarak gerçek zamanlı kamera görüntüsü üzerinden baret (hardhat) tespiti yapar. Baretli kişiler yeşil, baretsiz kişiler kırmızı çerçeve ile gösterilir.

## Özellikler

- YOLOv8 modelini kullanarak nesne tespiti yapar  
- Baretli ve baretsiz kişileri ayırt eder  
- Tespit edilen nesneleri farklı renklerle çizer  
- Güven eşiği (confidence threshold) ayarlanabilir  

## Gereksinimler

- Python 3.x  
- OpenCV  
- Ultralytics YOLOv8  

Gerekli kütüphaneleri yüklemek için:

```bash
pip install ultralytics opencv-python
```

## Kullanım

1. Eğitimli model dosyanızı (`my_train_best.pt`) doğru konuma ekleyin  
2. Kod dosyasını kaydedin, örneğin `baret_tespiti.py`  
3. Terminalden çalıştırın:

```bash
python baret_tespiti.py
```

4. Kamera açılacak ve tespit edilen nesneler ekranda gösterilecektir  

## Kodun İşleyişi

- YOLO modeli yüklenir  
- Kamera görüntüsü alınır ve her karede nesne tespiti yapılır  
- Baretli kişiler yeşil, baretsiz kişiler kırmızı kutularla işaretlenir  
- Güven oranı ve etiketler ekranda gösterilir  

## Tuşlar

- **Q** tuşuna basarak uygulamayı kapatabilirsiniz
