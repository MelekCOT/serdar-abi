# GitHub'a Yükleme Adımları

Proje hazır! GitHub'a yüklemek için aşağıdaki adımları izleyin.

## 1. GitHub'da Yeni Depo Oluşturun

1. [github.com](https://github.com) adresine gidin ve giriş yapın
2. Sağ üstteki **"+"** → **"New repository"** tıklayın
3. **Repository name:** `ikra-scooter-rent` (veya istediğiniz isim)
4. **Description:** "İkra Scooter Rent & Kurye web sitesi"
5. **Public** seçin
6. **"Create repository"** tıklayın (README eklemeyin, boş oluşturun)

## 2. Projeyi GitHub'a Gönderin

Cursor'da **Terminal** açın (Ctrl + `) ve proje klasöründe şu komutları çalıştırın:

```bash
git remote add origin https://github.com/KULLANICI_ADINIZ/REPO_ADI.git
git branch -M main
git push -u origin main
```

**Örnek:** GitHub kullanıcı adınız `ahmet` ve repo adı `ikra-scooter-rent` ise:
```bash
git remote add origin https://github.com/ahmet/ikra-scooter-rent.git
git branch -M main
git push -u origin main
```

## 3. GitHub Pages ile Yayınlama (İsteğe Bağlı)

Sitenizi ücretsiz yayınlamak için:

1. GitHub repo sayfanızda **Settings** → **Pages**
2. **Source:** "Deploy from a branch" seçin
3. **Branch:** main, / (root) seçin
4. **Save** tıklayın
5. Birkaç dakika sonra siteniz `https://KULLANICI_ADINIZ.github.io/REPO_ADI/` adresinde yayında olacak

---

**Not:** İlk `git push` sırasında GitHub kullanıcı adı ve şifre/token istenebilir. Şifre yerine **Personal Access Token** kullanmanız gerekebilir.
