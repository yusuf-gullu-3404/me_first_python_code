liste = ["1", "3", "5", "20b", "abc", "10a", "60"]

for x in liste:
    try:
        sonuc = int(x)  # Sayıya dönüştürmeye çalış
        print(sonuc)    # Başarılı olursa ekrana yazdır
    except ValueError:  # Eğer dönüştürülemezse hatayı yakala
        continue        # Hata olursa döngüye devam et

while True:
    sayi = input("Sayı: ")
    if sayi == "q":
        break

    try:
        result = float(sayi)
        print("Girdiğiniz sayı:", result)
        break  # Burada doğru seviyede olmalı
    except ValueError:
        print("Geçersiz sayı, lütfen tekrar deneyin.")
        continue


turkce_karakterler = 'şçğüöİ'

parola = input('parola: ')

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkçe karakter içeremez.')


