def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = int(input("1. yazılı notu: "))
    not2 = int(input("2. yazılı notu: "))
    not3 = int(input("3. yazılı notu: "))

    with open("sınav_notları.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + " : " + str(not1) + "," + str(not2) + "," + str(not3) + "\n")

def notları_oku():
    with open("sınav_notları.txt", "r", encoding="utf-8") as file:
        for satır in file:
            print(satır.strip())  # `strip()` kullanarak gereksiz boş satırları temizledik

def notları_kaydet():
    print("Notları kaydet fonksiyonu henüz yazılmadı.")

while True:
    islem = input("\n1- Not gir\n2- Notları oku\n3- Notları kaydet\n4- Çıkış\nSeçiminiz: ")

    if islem == "1":
        not_gir()
    elif islem == "2":
        notları_oku()
    elif islem == "3":
        notları_kaydet()
    elif islem == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen 1-4 arasında bir değer girin.")
