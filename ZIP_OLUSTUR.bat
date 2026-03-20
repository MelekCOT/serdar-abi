@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ikrascooterrental.zip olusturuluyor...
echo.

powershell -NoProfile -Command ^
  "Compress-Archive -Path 'index.html','gizlilik-politikasi.html','config.js','translations.js','.htaccess','images' -DestinationPath 'ikrascooterrental.zip' -Force"

if exist ikrascooterrental.zip (
    echo.
    echo Basarili! ikrascooterrental.zip olusturuldu.
    echo Bu dosyayi Hostinger File Manager'a yukleyebilirsiniz.
) else (
    echo Hata: ZIP olusturulamadi.
)

pause
