# Hostinger'a Tam Yükleme - Sıfırdan Kurulum

Tüm dosyalarınızı (public_html dahil) sildiyseniz, aşağıdaki adımlarla siteyi yeniden kurun.

---

## Adım 1: Web Kök Klasörünü Bulun veya Oluşturun

### public_html klasörü yoksa:

1. File Manager'da sol tarafta **"Yeni klasör"** (New folder) butonuna tıklayın
2. Klasör adı olarak **`public_html`** yazın (tire ile, küçük harf)
3. **Oluştur** / **Create** deyin
4. **public_html** klasörüne çift tıklayarak içine girin

### Başka bir yapı görüyorsanız:

- **"domains"** → **"ikrascooterrental.com"** görüyorsanız: O domain klasörü web kökünüz olabilir. İçine girin, dosyaları oraya yükleyin.
- **File Manager açıldığında doğrudan bir klasör listesi görüyorsanız:** Üstteki yol çubuğuna (breadcrumb) bakın. Örn. `🏠 > ikrascooterrental.com` ise zaten doğru yerdesiniz; `index.html` burada olmalı.
- **Hangi klasörün kök olduğundan emin değilseniz:** hPanel → **Websites** → **Manage** → **FTP Accounts**. "Root folder path" yazan yerde tam yol görünür (örn. `.../public_html` veya `.../domains/ikrascooterrental.com/public_html`).

> **Özet:** `index.html` dosyasının bulunduğu klasör = web kökü. O klasöre dosyaları yükleyin.

---

## Adım 2: ZIP Dosyasını Hazırlayın

Proje klasöründe **`ikrascooterrental.zip`** dosyası hazır. Bu dosya şunları içerir:
- index.html (ana sayfa)
- gizlilik-politikasi.html
- config.js
- translations.js
- .htaccess (sunucu ayarları – önemli)
- images/ klasörü

**Not:** ZIP’i yeniden oluşturacaksanız `.htaccess` dosyasını da ekleyin. Mevcut ZIP'te yoksa, ZIP açıldıktan sonra proje klasöründeki `.htaccess` dosyasını ayrıca Upload ile yükleyin.

---

## Adım 3: Hostinger File Manager'a Girin

1. **hPanel** açın: https://hpanel.hostinger.com
2. **Websites** → **Manage** (ikrascooterrental.com)
3. **File Manager** tıklayın
4. Web kök klasörüne girin (public_html veya domains/ikrascooterrental.com – Adım 1’e bakın)

---

## Adım 4: ZIP Dosyasını Yükleyin

1. **Upload** (Yükle) butonuna tıklayın
2. **ikrascooterrental.zip** dosyasını seçin (proje klasörünüzde)
3. Yükleme tamamlanana kadar bekleyin

---

## Adım 5: ZIP Dosyasını Açın

1. **ikrascooterrental.zip** dosyasına sağ tıklayın
2. **Extract** veya **Extract All** seçin
3. Açılacak klasörü **şu an bulunduğunuz kök klasör** olarak seçin (public_html veya domains/ikrascooterrental.com – "Buraya çıkar" da olur)
4. Çıkarma işlemi tamamlanınca ZIP içinde bir klasör oluşabilir

---

## Adım 6: Dosyaları Doğru Konuma Taşıyın

ZIP açıldıktan sonra:

- Eğer dosyalar **public_html** içinde doğrudan görünüyorsa (index.html, config.js vb.) → **İşlem tamam**
- Eğer **public_html** içinde yeni bir klasör oluştuysa (örn. "ikrascooterrental.com" veya "İkra Scooter...") → O klasörün **içindeki tüm dosyaları** public_html köküne taşıyın, sonra boş klasörü silin

**Doğru yapı şöyle olmalı:**
```
public_html/
├── .htaccess           ← Sunucu ayarları
├── index.html          ← Ana sayfa (buradan açılmalı)
├── gizlilik-politikasi.html
├── config.js
├── translations.js
└── images/
    └── GALERI_README.txt
```

---

## Adım 7: Görselleri Ekleyin (İsteğe Bağlı)

Galeri için 6 fotoğraf ekleyin:
1. **images** klasörüne girin
2. **gallery1.png**, **gallery2.png** ... **gallery6.png** olarak 6 görsel yükleyin

---

## Adım 8: ZIP Dosyasını Silin

Yükleme tamamlandıktan sonra **ikrascooterrental.zip** dosyasını public_html'den silin (yer kaplamasın).

---

## Kontrol

Tarayıcıda **https://ikrascooterrental.com** adresini açın. Site görünüyorsa kurulum tamamlanmıştır.

---

## Sorun Giderme

### Telefonda Farklı Fotoğraflar Görünüyor

**Olası neden 1 – Yanlış klasör:** `public_html` içinde `ikrascooterrental.com` adlı bir klasör varsa, domain bazen bu klasörden açılıyor olabilir. Güncellediğiniz dosyalar kökte kalır, site ise alt klasördeki eskileri kullanır.

**Çözüm:**
1. **ikrascooterrental.com** klasörüne tıklayın
2. İçindeki `index.html` ve `images` klasörünün tarihine bakın
3. **hPanel** → **Websites** → **Manage** → **Domains** bölümünden domain’in **document root** ayarını kontrol edin
4. Eğer kök `public_html/ikrascooterrental.com` ise: Güncel `index.html`, `config.js`, `translations.js`, `gizlilik-politikasi.html`, `images` klasörünü bu klasöre taşıyın
5. Veya document root’u doğrudan `public_html` yapın

**Olası neden 2 – Önbellek:** Tarayıcı veya Hostinger eski görselleri cache’ten gösteriyor olabilir.

**Çözüm:**
1. Telefonda siteyi **gizli sekme** ile açın
2. Veya tarayıcı ayarlarından “Önbelleği temizle” yapın
3. `index.html` içindeki görsel adreslerinde `?v=2` var; yeni fotoğraf yükledikten sonra bunu `?v=3` yapıp tekrar yüklemeniz cache’i yeniler

---

### 404 Hatası – Sayfa Açılmıyor

**En sık neden:** Dosyalar `public_html` kökünde değil, alt klasörde (örn. `public_html/ikrascooterrental.com/`).

**Çözüm adımları:**

1. **File Manager** → `public_html` klasörüne girin
2. İçeride **ikrascooterrental.com** veya **İkra Scooter** gibi bir alt klasör var mı bakın
3. Varsa o klasöre girin → **index.html, config.js, translations.js, .htaccess** dosyalarını seçin
4. **Move** (Taşı) → Hedef: `public_html` kökü (üst klasöre çıkıp oraya yapıştırın)
5. Boş kalan **ikrascooterrental.com** klasörünü silin
6. **Sonuç:** `index.html` doğrudan `public_html` içinde olmalı

**Doğru yapı:**
```
public_html/
├── .htaccess
├── index.html
├── gizlilik-politikasi.html
├── config.js
├── translations.js
└── images/
    ├── gallery1.png
    ├── gallery2.png
    ...
```

---

### Görseller "images\gallery1.png" Olarak Görünüyor – Klasör Yok

**Sorun:** Dosya adları `images\gallery1.png` şeklinde (backslash ile). Gerçek `images` klasörü yok, sunucu görselleri bulamıyor.

**Çözüm adımları:**

1. **public_html** içinde **Yeni klasör** → ad: `images` → Oluştur
2. `images\gallery1.png`, `images\gallery2.png` vb. dosyaların her birine tıklayın → **Rename** (Yeniden Adlandır) → sadece `gallery1.png`, `gallery2.png` ... `gallery6.png` yazın
3. Yeniden adlandırılmış dosyaları seçin → **Move** → `images` klasörüne taşıyın
4. `images\GALERI_README.txt` varsa → Rename ile `GALERI_README.txt` yapın → `images` klasörüne taşıyın

**Alternatif (daha kolay):** Proje klasörünüzdeki `images` klasörünü (içinde gallery1–6.png ile) doğrudan ZIP’leyip Hostinger’a yükleyin. `public_html` içinde Extract edin. Eski `images\galleryX.png` dosyalarını silebilirsiniz.

---

### Diğer Hatalar

- **403 Forbidden:** Dosya izinlerini kontrol edin (dosyalar: 644, klasörler: 755)
- **Sayfa boş:** config.js ve translations.js yüklü mü kontrol edin
- **Görseller yok:** images klasörü var mı, gallery1-6.png eklediniz mi kontrol edin
