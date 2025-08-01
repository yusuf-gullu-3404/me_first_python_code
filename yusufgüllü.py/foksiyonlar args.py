# Python *argsNedir? Ne İşe Yarar?Python'da *args, bir fonksiyona belirsiz sayıda aralıkları
#  değiştirmek için kullanılır. Kaç tane birikimini bilmeyensan *args kullanabilirsin.

# Eğer bir fonksiyon sabit sayıda parametre almak yerine esnek olmalıysa , *argskullanabilirsin.



def topla(*args):
    toplam = sum(args)
    print("Toplam:", toplam)

topla(3, 5)         # Çıktı: Toplam: 8
topla(1, 2, 3, 4)   # Çıktı: Toplam: 10
topla
