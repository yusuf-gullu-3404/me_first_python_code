import random

sayı = random.randint(1, 20)  # randint düzeltilmiş
can = int(input("Kaç hakkınız olsun beyefendi? "))  # Daha okunabilir bir giriş mesajı
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin yap: "))

    if sayı == tahmin:
        print(f"Tebrikler! {sayac}. defada bildiniz. Toplam puanınız: {int(100 - (100/can) * (sayac-1))}")
        break  # Doğru tahmin yapılınca döngüden çık

    elif sayı > tahmin:
        print("Yukarı ⬆")

    else:
        print("Aşağı ⬇")

if hak == 0:
    print(f"Hakkınız bitti! Sayıyı bulamadınız. Doğru sayı: {sayı}")
