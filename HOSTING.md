# Hosting Kurulumu - İkra Scooter Rent & Kurye

Sitenizi ücretsiz olarak yayınlamak için aşağıdaki seçeneklerden birini kullanabilirsiniz.

---

## 1. GitHub Pages (Önerilen - Ücretsiz)

Projeniz zaten [github.com/MelekCOT/serdar-abi](https://github.com/MelekCOT/serdar-abi) adresinde. Sadece GitHub Pages'i etkinleştirmeniz yeterli.

### Adımlar:

1. **[github.com/MelekCOT/serdar-abi](https://github.com/MelekCOT/serdar-abi)** sayfasına gidin
2. **Settings** sekmesine tıklayın
3. Sol menüden **Pages** seçin
4. **Build and deployment** bölümünde:
   - **Source:** "Deploy from a branch" seçin
   - **Branch:** `main` seçin
   - **Folder:** `/ (root)` seçin
5. **Save** butonuna tıklayın
6. 1-2 dakika bekleyin

### Siteniz yayında:
**https://melekcot.github.io/serdar-abi/**

---

## 2. Netlify (Alternatif - Ücretsiz)

1. [netlify.com](https://www.netlify.com) adresine gidin ve ücretsiz hesap oluşturun
2. **Add new site** → **Import an existing project**
3. **GitHub** ile bağlayın ve `serdar-abi` reposunu seçin
4. **Deploy** tıklayın
5. Siteniz `https://rastgele-isim.netlify.app` adresinde yayınlanır
6. **Domain settings** ile özel domain ekleyebilirsiniz

---

## 3. Vercel (Alternatif - Ücretsiz)

1. [vercel.com](https://vercel.com) adresine gidin ve ücretsiz hesap oluşturun
2. **Add New** → **Project**
3. **Import** ile GitHub reposunu seçin (`serdar-abi`)
4. **Deploy** tıklayın
5. Siteniz `https://serdar-abi.vercel.app` benzeri bir adreste yayınlanır

---

## Önemli Notlar

- **Görseller:** `images` klasöründeki gallery1.png - gallery6.png dosyalarını GitHub'a eklemeniz gerekir (şu an .gitignore'da). Yayınlamak için `.gitignore`'dan çıkarıp commit edebilir veya görselleri doğrudan repo'ya yükleyebilirsiniz.
- **Güncellemeler:** GitHub'a her `git push` yaptığınızda site otomatik güncellenir (GitHub Pages, Netlify, Vercel hepsi bunu destekler).
