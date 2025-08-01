# Kullanıcı hesap bilgileri
hesaplar = {
    "4657273923": {  # Yusuf'un hesabı
        "ad": "Yusuf Güllü",
        "pin": "1234",
        "bakiye": 3000,
        "ekbakiye": 2000
    },
    "481140973923": {  # Melike'nin hesabı
        "ad": "Melike Güllü",
        "pin": "5678",
        "bakiye": 2000,
        "ekbakiye": 3000
    }
}

# Kullanıcı girişi fonksiyonu
def giris_yap():
    hesap_no = input("Hesap Numaranızı Girin: ")
    if hesap_no in hesaplar:
        sifre = input("PIN Kodunuzu Girin: ")
        if sifre == hesaplar[hesap_no]["pin"]:
            print(f"Giriş Başarılı! Hoş geldiniz, {hesaplar[hesap_no]['ad']}.\n")
            return hesap_no  # Kullanıcı başarılı giriş yaptıysa hesap numarasını döndür
        else:
            print("Hatalı PIN! Tekrar deneyin.\n")
    else:
        print("Böyle bir hesap bulunamadı!\n")
    return None

# Bakiye sorgulama fonksiyonu
def bakiye_sorgula(hesap_no):
    hesap = hesaplar[hesap_no]
    print(f"\nAna Bakiye: {hesap['bakiye']} TL")
    print(f"Ek Bakiye: {hesap['ekbakiye']} TL")
    print(f"Toplam Kullanılabilir Bakiye: {hesap['bakiye'] + hesap['ekbakiye']} TL\n")

# Para yatırma fonksiyonu
def para_yatir(hesap_no):
    miktar = int(input("Yatırmak istediğiniz tutarı girin: "))
    if miktar > 0:
        hesaplar[hesap_no]["bakiye"] += miktar
        print(f"{miktar} TL başarıyla yatırıldı.")
        bakiye_sorgula(hesap_no)
    else:
        print("Geçersiz miktar!\n")

# Para çekme fonksiyonu (Ek bakiye kullanımı dahil)
def para_cek(hesap_no):
    miktar = int(input("Çekmek istediğiniz tutarı girin: "))
    hesap = hesaplar[hesap_no]
    
    toplam_bakiye = hesap["bakiye"] + hesap["ekbakiye"]  # Toplam kullanılabilir bakiye
    
    if 0 < miktar <= toplam_bakiye:
        if miktar <= hesap["bakiye"]:
            hesap["bakiye"] -= miktar  # Ana bakiyeden düş
        else:
            fark = miktar - hesap["bakiye"]
            hesap["bakiye"] = 0
            hesap["ekbakiye"] -= fark  # Ek bakiyeden kalan kısmı düş
        
        print(f"{miktar} TL başarıyla çekildi.")
        bakiye_sorgula(hesap_no)
    else:
        print("Yetersiz bakiye veya geçersiz tutar!\n")

# Ana menü fonksiyonu
def bankamatik():
    print("** Bankamatik Uygulamasına Hoş Geldiniz **\n")
    hesap_no = giris_yap()
    
    if hesap_no:
        while True:
            print("1 - Bakiye Sorgulama")
            print("2 - Para Yatırma")
            print("3 - Para Çekme")
            print("4 - Çıkış\n")
            secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")

            if secim == "1":
                bakiye_sorgula(hesap_no)
            elif secim == "2":
                para_yatir(hesap_no)
            elif secim == "3":
                para_cek(hesap_no)
            elif secim == "4":
                print("Çıkış yapılıyor. İyi günler!\n")
                break
            else:
                print("Geçersiz seçim! Tekrar deneyin.\n")

# Programı başlat
bankamatik()
