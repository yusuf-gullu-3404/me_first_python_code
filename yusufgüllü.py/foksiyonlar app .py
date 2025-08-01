def saat() :
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if (saat() < 12):
      return "günaydın"
    else: 
       return "tünaydın"
    
print(selamla())








sayılar = [10, 20, 30, 40, 50]

def toplam(liste):
    sonuc = 0
    for i in liste:
        sonuc += i  # Doğru kullanım
    return sonuc

sonuc = toplam(sayılar)
print(sonuc)
