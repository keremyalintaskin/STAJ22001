# Okey / Not Okey Tanıma Sistemi

Bu proje, bilgisayar kamerası ile gerçek zamanlı görüntü alarak fotoğrafları **Okey** ve **Not Okey** olarak sınıflandıran bir sistem sunar.  
Kullanıcı, canlı görüntü üzerinde belirli alanları seçip fotoğraf kaydedebilir ve kendi verisiyle modeli güncelleyebilir.  
Ayrıca sistem, yüz tespiti ve template matching özellikleri de içerir.

## Özellikler

- Gerçek zamanlı kamera görüntüsü  
- Okey ve Not Okey fotoğraf çekme ve kaydetme  
- Kullanıcı verileriyle modeli yeniden eğitme (retrain)  
- Yüz tespiti (Haar Cascade)  
- Template Matching ile belirli nesneleri tespit etme  
- GUI arayüzü ile kolay kullanım  

## Gereksinimler

- Python 3.x  
- OpenCV  
- TensorFlow / Keras  
- scikit-learn  
- Pillow  
- NumPy  

Gerekli kütüphaneleri yüklemek için:
```bash
pip install opencv-python tensorflow scikit-learn pillow numpy
```

## Kullanım

1. Kod dosyasını kaydedin, örneğin `okey_system.py`.  
2. Template dosyasının ve eğitimli model dosyasının doğru konumda olduğundan emin olun.  
3. Terminalden çalıştırın:
```bash
python okey_system.py
```
4. Kamera açılacak ve arayüz üzerinden:
   - Okey veya Not Okey fotoğrafı çekebilirsiniz  
   - Yeni verilerle modeli güncelleyebilirsiniz  
   - Yüz tespitlerini ve template matching sonuçlarını görebilirsiniz  

## Arayüz Özellikleri

- **Okey Fotoğrafı Çek:** Seçilen alanı Okey olarak kaydeder  
- **Not Okey Fotoğrafı Çek:** Seçilen alanı Not Okey olarak kaydeder  
- **Modeli Güncelle:** Tüm verilerle modeli yeniden eğitir ve kaydeder  
- **Canlı Kamera Görüntüsü:** Ekranda anlık olarak tahmin sonucu ve tespitler görünür  

## Klasör Yapısı

- `C:/ok_fotos` → Okey fotoğrafları  
- `C:/nok_fotos` → Not Okey fotoğrafları  
- `okey_model.h5` → Kayıtlı model dosyası  
- `template_ok.png` → Template matching için görsel  

## Kodun İşleyişi

1. Kamera görüntüsü alınır ve Tkinter arayüzünde gösterilir  
2. Yüz tespiti ve template matching yapılır  
3. Kullanıcı fotoğraf çektiğinde görüntü kaydedilir  
4. Yeterli veri olduğunda model yeniden eğitilebilir  
5. Yeni model otomatik olarak kaydedilir ve kullanılmaya devam eder  

## Tuşlar

- Kamera penceresini kapatmak için uygulama penceresini kapatın  
- Fotoğraf seçimi için çıkan pencerede ROI seçtikten sonra Enter’a basın  
