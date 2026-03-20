# Bu script'i çalıştırarak galeri görsellerini kopyalayabilirsiniz.
# Komut: python kopyala_gorseller.py

import os
import shutil

# Kaynak: Cursor assets klasörü
assets = os.path.expanduser(r"~\.cursor\projects\c-Users-Mine-Desktop-kra-Scooter-Rent-Kurye-hizmetleri\assets")
# Hedef: Bu script'in bulunduğu klasördeki images
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

os.makedirs(dest, exist_ok=True)

files = [
    "c__Users_Mine_AppData_Roaming_Cursor_User_workspaceStorage_51c9b79d40bca871cb9dc83fe32377aa_images_WhatsApp_Image_2026-03-20_at_20.57.23-b4aa88d6-95d3-4c3d-aedb-0730176980f0.png",
    "c__Users_Mine_AppData_Roaming_Cursor_User_workspaceStorage_51c9b79d40bca871cb9dc83fe32377aa_images_WhatsApp_Image_2026-03-20_at_20.5944-70b0de21-197f-4c61-97fd-10b341b99c5a.png",
    "c__Users_Mine_AppData_Roaming_Cursor_User_workspaceStorage_51c9b79d40bca871cb9dc83fe32377aa_images_WhatsApp_Image_2026-03-20_at_20.59.44-aff50347-4f69-490b-bc36-682f7a3cad1d.png",
    "c__Users_Mine_AppData_Roaming_Cursor_User_workspaceStorage_51c9b79d40bca871cb9dc83fe32377aa_images_WhatsApp_Image_2026-03-20_at_20.59.56-e3f2c2dc-8290-45f3-8306-6630b8298a69.png",
    "c__Users_Mine_AppData_Roaming_Cursor_User_workspaceStorage_51c9b79d40bca871cb9dc83fe32377aa_images_WhatsApp_Image_2026-03-20_at_20.59.57-de359c2b-e7fa-4184-8d24-42afeb33dade.png",
    "c__Users_Mine_AppData_Roaming_Cursor_User_workspaceStorage_51c9b79d40bca871cb9dc83fe32377aa_images_WhatsApp_Image_2026-03-20_at_20.57-2f3e9a8b-68ee-4b1e-a20b-60e72bc4b9ad.png",
]

for i, f in enumerate(files, 1):
    src = os.path.join(assets, f)
    dst = os.path.join(dest, f"gallery{i}.png")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"OK: gallery{i}.png")
    else:
        print(f"Bulunamadı: {f}")

print("\nTamamlandı. Sayfayı yenileyin.")
