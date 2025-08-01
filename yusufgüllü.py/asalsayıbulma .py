#Hangi Yöntemi Kullanmanız Gerekir?Yöntem	Hız	Zorluk	Ne Zaman Kullanılmalı?
# 1. Basit Bölüm	🐢 Yavaş	✅ Kolay	Küçük sayılar için
# 2. Yarısına Kadar Kontrol	⚡ Orta	✅ Kolay	Orta büyüklükte sayılar için
# 3. Kareköke Kadar Kotrol🚀 Hızlı	⚡ Orta	Büyük sayılar için en iyi yöntemle
# 4. 1-1000 Arası Asallar	🚀 Hızlı	⚡ Orta	Birden fazla asal sayısını bulmak için
# 5. Eratosthenes Eleği	🚀🚀 Çok Hızlı	🛠️ Orta/Zor	Çok büyük sayılar (örn. 10^6ve Üzeri) için




sayi = int(input("Bir sayı girin: "))

if sayi > 1:
    for i in range(2, sayi):
        if sayi % i == 0:
            print(f"{sayi} asal değildir.")
            break
    else:
        print(f"{sayi} asaldır.")
else:
    print(f"{sayi} asal değildir.")



sayi = int(input("Bir sayı girin: "))

if sayi > 1:
    for i in range(2, (sayi // 2) + 1):
        if sayi % i == 0:
            print(f"{sayi} asal değildir.")
            break
    else:
        print(f"{sayi} asaldır.")
else:
    print(f"{sayi} asal değildir.")




import math

for sayi in range(2, 1001):  # 1 ile 1000 arasındaki sayılar
    asal = True
    for i in range(2, int(math.sqrt(sayi)) + 1):  
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi, end=" ")





import math

sayi = int(input("Bir sayı girin: "))

if sayi > 1:
    for i in range(2, int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:
            print(f"{sayi} asal değildir.")
            break
    else:
        print(f"{sayi} asaldır.")
else:
    print(f"{sayi} asal değildir.")





def eratosthenes(n):
    asal = [True] * (n + 1)  
    asal[0], asal[1] = False, False  # 0 ve 1 asal değil

    for i in range(2, int(n**0.5) + 1):
        if asal[i]:  
            for j in range(i * i, n + 1, i):  
                asal[j] = False  

    return [i for i, is_asal in enumerate(asal) if is_asal]

print(eratosthenes(1000))  # 1-1000 arası asal sayıları bul



def asalsayıbul(sayı1, sayı2):
    for sayı in range(sayı1, sayı2 + 1):  # Belirtilen aralıktaki tüm sayılar için
        if sayı > 1:  # 1 asal sayı değildir, o yüzden kontrol ediyoruz
            for i in range(2, int(sayı ** 0.5) + 1):  # 2'den kareköküne kadar kontrol
                if sayı % i == 0:
                    break  # Eğer bölünüyorsa asal değildir, döngüden çık
            else:  
                print(sayı, end=" ")  # Eğer hiç bölünmezse asal sayıdır

# Fonksiyonu çalıştır
asalsayıbul(3, 37)





























































