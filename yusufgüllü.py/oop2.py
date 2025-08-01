from datetime import date

class Kisi:
    zam_oranı = 1.1
    kisi_sayisi = 0

    def __init__(self, isim, yaş):
        self.isim = isim
        self.yaş = yaş
        Kisi.kisi_sayisi += 1

    def bilgilerini_soyle(self):
        return f"Ad: {self.isim}, Yaş: {self.yaş}"

    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi

    @classmethod
    def string_ile_olustur(cls, str_):
        isim, yaş = str_.split("-")
        return cls(isim, int(yaş))

    @classmethod
    def dogum_yili_ile_olustur(cls, isim, dogum_yili):
        return cls(isim, date.today().year - dogum_yili)

    @staticmethod
    def dogumyili_bul(yas):
        return date.today().year - yas

# Örnek Kullanım
kisi1 = Kisi("Ali", 20)
kisi2 = Kisi("Veli", 30)

print(kisi1.bilgilerini_soyle())  
print(kisi2.bilgilerini_soyle())  
print(Kisi.kisi_sayisini_soyle())  

# String ile oluşturma
kisi3 = Kisi.string_ile_olustur("Ayşe-25")
print(kisi3.bilgilerini_soyle())  

# Doğum yılı ile oluşturma
kisi4 = Kisi.dogum_yili_ile_olustur("Mehmet", 1995)
print(kisi4.bilgilerini_soyle())  

# Doğum yılını bulma (staticmethod çağrısı)
print(Kisi.dogumyili_bul(kisi1.yaş))  # 2025 - 20 = 2005
print(Kisi.dogumyili_bul(kisi2.yaş))  # 2025 - 25 = 2000
print(Kisi.dogumyili_bul(kisi3.yaş)) 
print(Kisi.dogumyili_bul(kisi4.yaş)) 