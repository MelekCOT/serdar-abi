# Hostinger'a Yükleme - ikrascooterrental.com

## Hazırlanan ZIP Dosyası

Proje klasöründe **`ikrascooterrental.zip`** dosyası oluşturuldu. Bu dosya sitenizin tüm dosyalarını içerir.

---

## Yöntem 1: Migration/Backup Upload (Verdiğiniz Link)

1. **[Hostinger Migration Sayfası](https://hpanel.hostinger.com/migrations-onboarding/ikrascooterrental.com/169qXxVERJqQv4Sur/upload-backups)** adresine gidin
2. **ikrascooterrental.zip** dosyasını sürükleyip bırakın veya "Dosya Seç" ile yükleyin
3. Yükleme tamamlanana kadar bekleyin
4. Hostinger'ın talimatlarına göre devam edin

---

## Yöntem 2: File Manager ile Manuel Yükleme

1. **hPanel** → **Websites** → **File Manager** açın
2. **public_html** klasörüne girin
3. **Upload** butonuna tıklayın
4. **ikrascooterrental.zip** dosyasını yükleyin
5. Yükleme tamamlandıktan sonra ZIP dosyasına sağ tıklayın → **Extract**
6. ZIP içindeki dosyaları (index.html, config.js vb.) **public_html** köküne taşıyın
7. Boş kalan klasörleri ve ZIP dosyasını silin

---

## Yöntem 3: FTP ile Yükleme

1. **hPanel** → **FTP Accounts** bölümünden FTP bilgilerinizi alın
2. FileZilla veya benzeri FTP programı ile bağlanın
3. **public_html** klasörüne gidin
4. Şu dosyaları yükleyin:
   - index.html
   - gizlilik-politikasi.html
   - config.js
   - translations.js
   - images/ klasörü (içindeki dosyalarla birlikte)

---

## Dosya Yapısı (public_html)

Yükleme sonrası doğru yapı:

```
public_html/
├── index.html
├── gizlilik-politikasi.html
├── config.js
├── translations.js
└── images/
    ├── GALERI_README.txt
    └── gallery1.png ... gallery6.png (ekleyin)
```

---

## Önemli Notlar

- **Görseller:** `images` klasörüne gallery1.png - gallery6.png dosyalarını eklemeyi unutmayın
- **Ana sayfa:** index.html dosyası `public_html` kökünde olmalı
- **Domain:** ikrascooterrental.com zaten Hostinger'da tanımlı görünüyor

---

## Siteniz Yayında

Yükleme tamamlandıktan sonra siteniz şu adreste erişilebilir olacak:

**https://ikrascooterrental.com**
