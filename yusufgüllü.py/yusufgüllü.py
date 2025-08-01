#int tam sayıları fload da ondalıklı sayıları gösterir
type(2+0.5)

# veri tipi dönüsümlerinde bir degisken belirleriz örnegin 
#a = 10
#ad = yusuf 
#gibi bunlarıda print(ad) yazarak calıstırabiliyoruz


# sayılı islemlerde float yada int olduguna dikkat et
# sayılı islemlerde number yada string olup olmadıgına dikkat et

#bir cümle yazarken basına \n koyarsan at satıra yazar örnegin 
konusma = "merhaba benim adım " +" \n " + "yusuf güllü" 
print(konusma)

#index yazdırma 
print(konusma[0])
print(konusma[1])
print(konusma[2])
print(konusma[3])

# len kelimesi ifademizin kac karakterden olustugunu yazar

#format kelimesi belirlenen sırada süslü parantezin icine degiskeni koyar
#örn:
 
name = "yusuf"
sorname = "güllü"

print("my name is a {n}  {s} ".format(n=name,s=sorname))

# süslü parantezlerin içine  1,0 gibi degerler yada hic deger girmeden 
# yada 1,0 yapıp farklı yöntemler ve sekillerde yazdırabili 
# aynı zamanda söylede yapabiliriz

result = 200/700
print(" the result is {}".format(result))

# egerki süslü parantezin içine  bir aralık verirsek ondan sonraki sayıyı yazdırmaz

presult = 200 / 700
print("The result is {r:.4f}".format(r=result))

# sıfırdan sonraki basamagı yazmaz


# uppur lower capitalize ve title bunlar dizedeki harfleri sırasıyla hepsi büyük , hepsi küçük,sadece
#  ilk harf büyük , hepsinin  ilk harfi büyük  olur 

mesaj = " ben optimus prime bu mesajım bütün otobotlara biz dünyadayız ve sizi bekliyoruz lan "

mesaj = mesaj.upper()
print(mesaj)


mesaj = mesaj.lower()
print(mesaj)

mesaj = mesaj.title()
print(mesaj)


# Örnek 1
metin = "python programlama"
print(metin.capitalize())
# Çıktı: "Python programlama"

# Örnek 2
metin = "123python PROGRAMLAMA"
print(metin.capitalize())
# Çıktı: "123python programlama"

# Örnek 3
metin = "PYTHON"
print(metin.capitalize())
# Çıktı: "Python"

#baslangıctaki ve  sondaki boşlugu siler 
mesaj = mesaj.strip()
print(mesaj)
 
# spilit " "  sekilde kelimeleri ayırır boslugun içinde belirtilen seyden de ayırabilir
#  kısaca diziyi parcalara ayırır
mesaj = mesaj.split()
print(mesaj) 

#  " " join ile kelimeyi tekrar birlestirebiliriz 
mesaj = " " .join(mesaj)
print(mesaj)

mesaj = "*" .join(mesaj)
print(mesaj)

# find cümlenin icinde aradıgımızı bulur ve indexini verir ilk harfinin 
mesaj = " ben optimus prime bu mesajım bütün otobotlara biz dünyadayız ve sizi bekliyoruz lan "
soru = mesaj.find("lan")
print(soru)
#startswith cümlenin bas harfinin dogru olup olmadıgını true ve false ile gösterir
#tam tersi olan endswith de son harfi gösterir
soyu = mesaj.startswith("")
soyu2 = mesaj.endswith("")
print(soyu)
print(soyu2)

# replace aradıgımız karakteri bulup istedigimiz ile degistirir
 
tr = mesaj.replace("optimus","yusuf")
print(tr)


#Python'da center() yöntemi, bir stringin belirli bir genişlikte ortalanmasını sağlar. Bu işlem sırasında,
#  stringin sağına ve soluna belirtilen karakterler (varsayılan olarak boşluk) eklenir.
yusuf = "Yusuf"
result = yusuf.center(50, "*")
print(result)

 # isalpha ve isdigit dize mizin alfebetik yada sayılarda olup olmadıgını true veya false ile gösterir
 
result = "yusuf".isalpha()
print(result)

# rjust ve ljust center gibi ama kelimemizi ya en sola yada en saga yazar 

yusuf = yusuf 
result = "yusuf".ljust(50,"*")
result2 = "yusuf".rjust(50 , "*")
print(result)
print(result2)


# pythonda listeler ve liste birleştirme 

kullanıcı1 = [ "yusuf ,güllü "]
kullanıcı2 = [ "14 , python"]

kullanıcılar = [kullanıcı1 + kullanıcı2]

print(kullanıcı1)
print(kullanıcı2)
print(kullanıcılar)

print(kullanıcılar[0][1])

# in ile bir degiskenin liste içinde olup olmadıgını ögreniriz 

# Python'da del anahtar kelimesi, bir nesneyi bellekten silmek veya bir değişkeni
#  liste öğesini ya da bir sözlük anahtarını kaldırmak için kullanılır.

liste = [1, 2, 3, 4, 5]
del liste[2]  # 2. indeksi (3) kaldırır
print(liste)  # Çıktı: [1, 2, 4, 5]

#pythonda bir listeyi ters cevirmek için sunları yapabilirsiniz
#reversed,reverse,::-1 ile listeyi ters cevirebilirsiniz örnekler

liste = [1, 2, 3, 4, 5]
ters_liste = liste[::-1]
print(ters_liste)  # Çıktı: [5, 4, 3, 2, 1]

liste = [1, 2, 3, 4, 5]
ters_liste = list(reversed(liste))
print(ters_liste)  # Çıktı: [5, 4, 3, 2, 1]

liste = [1, 2, 3, 4, 5]
liste.reverse()  # Orijinal listeyi ters çevirir
print(liste)  # Çıktı: [5, 4, 3, 2, 1]

# min ve max ile alfabetik ve sayıtik en büyük ve en küçük degerleri bulup yazdırabiliriz

sayılar = [1,3,65,67,43,888,9,31,13]
harfler = [ "a","m","l","x","w","z"]

ebs = max(sayılar)
eks = min(sayılar)
ebh = max(harfler)
ekh = min(harfler)

print(harfler)
print(sayılar)
print(ebs)
print(ebh)
print(eks)
print(ekh)

# listelerin foksiyonları 

#append listenin sonuna eleman eklemek için kullanılır 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.append("ekran kartı")
print(donanım)

# extend listeleri birleştirmek için kullanılır 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
yazılım = ["işletim sistemi","web tarayıcı"]
yazılım.extend(donanım)
print(yazılım)

# ınsert listenin belirtilen indekse eleman eklemesi 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.insert(2,"tarayıcı")
print(donanım)

#  remove  liste içinde değeri verilen elemanı siler 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.remove("klavye")
print(donanım)

# pop listede indeksi belirtileni siler 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.pop(3)
print(donanım)

# clear listenin tüm elemanlarını siler 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.clear()
print(donanım)

# ındex bir elemanın listede konumunu bulur 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
print(donanım.index("sabit disk"))


# count listede belirtilen elemandan kaç tane olduğunu söyler 
donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
say  = donanım.count("klavye")
print(say)

# sort liste içindeki elemanları sayı veya harf ne işe sıralar 
donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.sort()
print(donanım)


#reverse listeyi sondan basa dogru ters bir sekilde yazdırır 
donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
donanım.reverse()
print(donanım)


#copy listeyi yeni bir liste olarak kopyalar 
donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
yeni_donanım = donanım.copy()
print(yeni_donanım)


# del indeksi verilen elemanı siler 

donanım = ["yazıcı","klavye","işlemci","bellek","sabit disk"]
del donanım[2]
print(donanım)


# tuple , tuplenin özelliği eleman silip ekleyememek ancak genel bir tuple listesi ile birlestirebiliriz 

# Tuple ve Liste tanımlamaları
tuple_ornek = ("elma", "armut", "muz")  # Tuple (değiştirilemez)
liste_ornek = ["elma", "armut", "muz"]  # Liste (değiştirilebilir)

# 1. Elemanlara erişim (Her ikisinde de benzer)
print("Tuple'dan ilk eleman:", tuple_ornek[0])  # Çıktı: elma
print("Listeden ilk eleman:", liste_ornek[0])   # Çıktı: elma

# 2. Eleman değiştirme
# Tuple değiştirilemez, aşağıdaki kod hata verir:
# tuple_ornek[0] = "çilek"  # Hata: TypeError: 'tuple' object does not support item assignment

# Liste değiştirilebilir:
liste_ornek[0] = "çilek"
print("Liste güncellenmiş hali:", liste_ornek)  # Çıktı: ['çilek', 'armut', 'muz']

# 3. Performans karşılaştırması (Tuple daha hızlıdır)
import time

# Tuple ile
basla = time.time()
tuple_ornek = tuple(range(1000000))  # 1 milyon elemanlı bir tuple oluşturma
bitir = time.time()
print("Tuple oluşturma süresi:", bitir - basla)

# Liste ile
basla = time.time()
liste_ornek = list(range(1000000))  # 1 milyon elemanlı bir liste oluşturma
bitir = time.time()
print("Liste oluşturma süresi:", bitir - basla)

# 4. Bellek kullanımı (Tuple daha az yer kaplar)
import sys
tuple_bellek = sys.getsizeof(tuple_ornek)
liste_bellek = sys.getsizeof(liste_ornek)
print("Tuple bellek kullanımı:", tuple_bellek, "byte")
print("Liste bellek kullanımı:", liste_bellek, "byte")

# 5. İmmutability (Değiştirilemezlik avantajı)
# Tuple sabit olduğu için hashlenebilir ve dictionary anahtarı olarak kullanılabilir:
sozluk = {("x", "y"): "Koordinat"}
print("Tuple dictionary anahtarı:", sozluk[("x", "y")])  # Çıktı: Koordinat

# Liste hashlenemez ve dictionary anahtarı olamaz:
# sozluk = {[1, 2]: "Hata"}  # Hata: TypeError: unhashable type: 'list'

# 6. Eleman ekleme/silme (Sadece listelerde mümkün)
# Listeye eleman ekleme
liste_ornek.append("portakal")
print("Listeye yeni eleman eklendi:", liste_ornek)

# Tuple'a doğrudan eleman eklenemez, ancak yeni bir tuple oluşturulabilir:
tuple_yeni = tuple_ornek + ("portakal",)
print("Tuple'a yeni eleman eklemek için yeni tuple oluşturuldu:", tuple_yeni)


# Python'da dictionary (sözlük), veri tiplerinden biridir ve anahtar-değer çiftleri (key-value pairs) 
# şeklinde veri saklamak için kullanılır. Sözlükler,, tıpkı gerçek hayattaki sözlükler gibi 
# bir anahtara karşılık bir değer tutar.
# Öne Çıkan Özellikler:
#Anahtarlar benzersizdir ve değiştirilemez (immutable) veri tiplerinde olmalıdır (örneğin, string, sayı 
#veya tuple).
#Değerler ise herhangi bir veri tipi olabilir (string, sayı, liste, başka bir sözlük, vs.).
#Sözlükler süslü parantez {} ile tanımlanır.
#Anahtarlara doğrudan erişerek değerleri alabilir veya değiştirebilirsiniz.


# Öğrenci bilgilerini tutan bir sözlük
ogrenci = {
    "isim": "Mehmet",
    "yas": 20,
    "dersler": ["Matematik", "Fizik", "Kimya"],
    "notlar": {"Matematik": 90, "Fizik": 85, "Kimya": 88}
}

# Verilere erişim
print(f"Öğrenci Adı: {ogrenci['isim']}")
print(f"Yaşı: {ogrenci['yas']}")
print(f"Aldığı Dersler: {', '.join(ogrenci['dersler'])}")
print(f"Matematik Notu: {ogrenci['notlar']['Matematik']}")

# Yeni bir ders ekleme
ogrenci["dersler"].append("Biyoloji")
ogrenci["notlar"]["Biyoloji"] = 92

# Güncellenmiş sözlük
print("\nGüncellenmiş Öğrenci Bilgisi:")
print(ogrenci)

# Python'da f" ile başlayan bir string, f-string (formatlı string) olarak adlandırılır. f-string,
#  Python 3.6 ve sonraki sürümlerinde tanıtılmış bir özellik olup, string içinde değişken 
# veya ifadeleri doğrudan yerleştirmek için kullanılır.
#  Bu, okunabilirliği artırır ve daha kolay bir şekilde string formatlamayı sağlar.

isim = "Ahmet"
yas = 25
print(f"Merhaba, benim adım {isim} ve {yas} yaşındayım.")


# Python'da update(), genellikle dictionary (sözlük) veri yapısında kullanılan bir yöntemdir ve
#  bir sözlüğü başka bir sözlükle veya anahtar-değer çiftleriyle güncellemek için kullanılır.
#update() metodu, mevcut sözlüğe yeni anahtar-değer çiftleri ekler veya aynı anahtar varsa değerini günceller
# . Orijinal sözlük üzerinde değişiklik yapar (in-place) ve hiçbir şey döndürmez.


# Örnek sözlük
bilgiler = {"ad": "Ahmet", "yas": 25}

# Yeni bilgiler içeren başka bir sözlük
yeni_bilgiler = {"meslek": "Mühendis", "yas": 26}

# Update ile güncelleme
bilgiler.update(yeni_bilgiler)

print(bilgiler)

bilgiler = {"ad": "Ayşe", "yas": 30}

# Anahtar-değer çiftleriyle güncelleme
bilgiler.update(meslek="Doktor", adres="İstanbul")

print(bilgiler)

bos_sozluk = {}
bos_sozluk.update({"ad": "Ali", "yas": 20})
print(bos_sozluk)



# add eleman eklemek için kullanılır 

#Python'da discard() yöntemi, bir set (kümeye) ait bir elemanı silmek için kullanılır.
#  Eğer belirtilen eleman kümede bulunuyorsa, siler; fakat eleman kümede yoksa hata vermez 
# (bu, remove() yönteminden farkıdır).

kume = {1, 2, 3, 4, 5}
kume.discard(3)
print(kume)  # {1, 2, 4, 5}

#Python'da remove(), bir koleksiyondan (örneğin, liste veya set) belirtilen bir elemanı kaldırmak
#  için kullanılan bir metottur. Eğer kaldırılmak istenen eleman koleksiyonda yoksa, 
# ValueError veya KeyError hatası verir.

liste = [1, 2, 3, 4, 5]
liste.remove(3)  # 3 elemanını sil
print(liste)  # [1, 2, 4, 5]



# Python'da sets (kümeler), sırasız, değiştirilebilir ve benzersiz (tekrar etmeyen) elemanlardan oluşan bir
#  veri yapısıdır. Matematikteki kümelere benzer şekilde çalışır ve güçlü küme işlemleri 
# (kesişim, birleşim, fark gibi) yapmayı kolaylaştırır.
# ÖzelliklerSırasız: Elemanlar sırasızdır; indeksleme ve sıralama yapılamaz.Benzersiz Elemanlar: Aynı elema 
#  birden fazla kez yer alamaz.Değiştirilebilir: Eleman eklenip çıkarılabilir.Heterojen Elemanlar:
#  Farklı tür

# 1. Küme Parantezleriyle Set Tanımlama:
# Elemanları olan bir set
kume = {1, 2, 3, 4, 5}
print(kume)  # {1, 2, 3, 4, 5}
# set() Fonksiyonu ile Set Tanımlama:
# Boş bir set
bos_kume = set()
print(type(bos_kume))  # <class 'set'>

# Tekrarlayan elemanları otomatik olarak kaldırır
tekrarli_kume = {1, 2, 2, 3, 4, 4}
print(tekrarli_kume)  # {1, 2, 3, 4}

#Birleşim (Union):Birleştirilen iki küme arasında tüm elemanlar bulunur
#  (tekrar eden elemanlar bir kez yer alır).
kume1 = {1, 2, 3}
kume2 = {3, 4, 5}
print(kume1.union(kume2))  # {1, 2, 3, 4, 5}
print(kume1 | kume2)       # {1, 2, 3, 4, 5}

#2. Kesişim (Intersection):
#İki kümenin ortak elemanlarını döndürür.


print(kume1.intersection(kume2))  # {3}
print(kume1 & kume2)              # {3}

#Fark (Difference):
#birinci kümenin, ikinci kümede olmayan elemanlarını döndürür.

print(kume1.difference(kume2))  # {1, 2}
print(kume1 - kume2)            # {1, 2}

#Alt Küme ve Üst Küme (Subset, Superset):
#issubset(): Bir küme, diğerinin alt kümesi mi?
#issuperset(): Bir küme, diğerini kapsıyor mu?

kume3 = {1, 2}

print(kume3.issubset(kume1))  # True
print(kume1.issuperset(kume3))  # True

#Value (Değer)Bir değişken değer ile ilişkilendirildiğinde, o değişken aslında veriyle doğrudan bağlantılıdır
# . Başka bir deyişle, değişkenin içeriği değer olarak kopyalanır.

a = 5
b = a  # b'ye a'nın değeri kopyalanır
a = 10  # a'nın değeri değiştirilir
print(a)  # 10
print(b)  # 5 (b değişmedi, a'dan bağımsızdır)

#Reference (Referans) Bir değişken referans ile ilişkilendirildiğinde, o değişken aslında veri üzerinde
#  bir bağlantı taşır. Başka bir deyişle, bir değişkenin değeri üzerinde yapılan değişiklikler,
#  o veriye referans veren tüm değişkenleri etkiler.

a = [1, 2, 3]
b = a  # b, a'nın referansını alır
a.append(4)  # a'nın içeriği değiştirilir
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4] (b de değişti çünkü a ve b aynı nesneyi referans eder)

# 1. Aritmetik Operatörler
#Aritmetik operatörler, sayısal değerler üzerinde matematiksel işlemler yapmamızı sağlar.

# operatör	Açıklama	Örnek	Sonuç
#+	Toplama	3 + 2	5
#-	Çıkarma	3 - 2	1
#*	Çarpma	3 * 2	6
#/	Bölme	5 / 2	2.5
#//	Tam Bölme (floored division)	5 // 2	2
#%	Modül (kalan)	5 % 2	1
#**	Üs Alma (Exponentiation)	2 ** 3	8
#2. Karşılaştırma Operatörleri
#Karşılaştırma operatörleri, iki değeri karşılaştırır ve sonuç olarak True veya False döndürür.

# Operatör	Açıklama	Örnek	Sonuç
# ==	Eşit mi?	3 == 2	False
# !=	Eşit değil mi?	3 != 2	True
# >	Büyüktür	3 > 2	True
# <	Küçüktür	3 < 2	False
# >=	Büyük ya da eşit mi?	3 >= 2	True
# <=	Küçük ya da eşit mi?	3 <= 2	False
# 3. Mantıksal Operatörler
# Mantıksal operatörler, iki veya daha fazla koşulu karşılaştırarak bunların doğruluğunu değerlendirir.

# Operatör	Açıklama	Örnek	Sonuç
# and	Mantıksal VE	True and False	False
# or	Mantıksal VEYA	True or False	True
# not	Mantıksal DEĞİL	not True	False
# 4. Atama Operatörleri
# Atama operatörleri, bir değeri bir değişkene atamak için kullanılır.

# Operatör	Açıklama	Örnek	Sonuç
# =	Değeri atama	x = 5	x = 5
# +=	Toplamı atama	x += 3	x = x + 3
# -=	Farkı atama	x -= 3	x = x - 3
# *=	Çarpımı atama	x *= 3	x = x * 3
# /=	Bölmeyi atama	x /= 3	x = x / 3
# //=	Tam bölmeyi atama	x //= 3	x = x // 3
# %=	Modül atama	x %= 3	x = x % 3
# **=	Üssü atama	x **= 3	x = x ** 3
# 5. Üye Operatörleri
# Üye operatörleri, bir değer bir koleksiyon (liste, set, sözlük) içinde var mı diye kontrol etmek için kullanılır.

# operatör	Açıklama	Örnek	Sonuç
# in	Eleman koleksiyon içinde var mı?	3 in [1, 2, 3]	True
# not in	Eleman koleksiyon içinde yok mu?	4 not in [1, 2, 3]	True
# 6. Kimlik Operatörleri
# Kimlik operatörleri, iki nesnenin aynı bellek alanına sahip olup olmadığını kontrol eder.

# Operatör	Açıklama	Örnek	Sonuç
# is	Aynı nesne mi?	x is y	True / False
# is not	Aynı nesne değil mi?	x is not y	True / False
# 7. Bit Düzeyinde Operatörler
# Bit düzeyinde operatörler, sayıları ikili (binary) formatta işleyerek bitler üzerinde işlem yapmamıza olanak tanır.

# Operatör	Açıklama	Örnek	Sonuç
# &	Bit düzeyinde VE	5 & 3	1
# `	`	Bit düzeyinde VEYA	`5
# ^	Bit düzeyinde XOR	5 ^ 3	6
# ~	Bit düzeyinde NOT	~5	-6
# <<	Bit düzeyinde sola kaydırma	5 << 1	10
# >>	Bit düzeyinde sağa kaydırma	5 >> 1	2
# 8. Koşul (Ternary) Operatörü
# Python'da koşullu bir ifade yazmanın kısa bir yoludur. Üçlü operatör olarak da bilinir.



#if (Eğer)
# if ifadesi, belirli bir koşulun doğru olup olmadığını kontrol eder. Eğer koşul doğru (True) ise, if bloğundaki kod çalıştırılır.

#Örnek:

sayi = 10

if sayi > 5:
    print("Sayı 5'ten büyüktür.")
#📌 Çıktı:


#Sayı 5'ten büyüktür.
#Çünkü sayi > 5 koşulu doğrudur.

#elif (Aksi Eğer)
#elif, if koşulu yanlış (False) olduğunda, yeni bir koşul belirlemek için kullanılır.

#Örnek:

sayi = 5

if sayi > 10:
    print("Sayı 10'dan büyüktür.")
elif sayi == 5:
    print("Sayı 5'e eşittir.")
#📌 Çıktı:


#Sayı 5'e eşittir.
#Çünkü sayi > 10 yanlış olduğu için elif kontrol edilir ve sayi == 5 doğru olduğu için ilgili kod çalıştırılır.

#else (Aksi Durum)
#else, yukarıdaki hiçbir koşul sağlanmazsa çalıştırılan kod bloğudur.

#Örnek:

sayi = 3

if sayi > 10:
    print("Sayı 10'dan büyüktür.")
elif sayi == 5:
    print("Sayı 5'e eşittir.")
else:
    print("Sayı 10'dan küçük ve 5 değil.")
#📌 Çıktı:


#Tümünü Kullanarak Örnek:

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif bir sayı girdiniz.")
elif sayi < 0:
    print("Negatif bir sayı girdiniz.")
else:
    print("Sıfır girdiniz.")
#📌 Girdi ve Çıktı Örnekleri:

# Python'daki döngüler, belirli bir koşul altında bir kod bloğunu tekrar tekrar çalıştırmanıza olanak tanır.
#  İki ana türde döngü bulunur: for döngüsü ve while döngüsü. Ayrıca, bu döngülerin kullanımını 
# kolaylaştıran break, continue, ve else gibi ek yapılar da vardır. İşte Python’daki döngülerin 
# açıklamaları ve örnekleri:

#1. for Döngüsü
#for döngüsü, bir iterable (örneğin, liste, dizi, string) üzerinde döner ve her adımda öğeyi alır.

#Örnek:

# Liste üzerinde döngü
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
#Açıklama: Burada, numbers listesindeki her bir öğe tek tek num değişkenine atanır ve print(num) 
# her birini ekrana yazdırır.

#range() Fonksiyonu ile for Döngüsü:
#range() fonksiyonu, belirli bir aralıkta sayılar üretmek için kullanılır.
#  Bu genellikle bir sayacın kontrol edildiği durumlarda kullanılır.


# 0'dan 4'e kadar sayılarla döngü
for i in range(5):
    print(i)
#Açıklama: range(5) ifadesi 0'dan 4'e kadar olan sayıları üretir ve her biriyle döngü çalıştırılır.

#2. while Döngüsü
#while döngüsü, bir koşul doğru olduğu sürece çalışır. Koşul yanlış olduğunda döngü sonlanır.

#Örnek:

# 1'den 5'e kadar sayılarla döngü
count = 1
while count <= 5:
    print(count)
    count += 1  # count değişkenini artırıyoruz
#Açıklama: Burada, count değişkeni 5'e ulaşana kadar döngü devam eder. Her seferinde count 1 artırılır.

#3. break ve continue
#break:
#break komutu döngüyü erken sonlandırmak için kullanılır. Koşul sağlandığında döngü tamamen durur.


# Sayıları 5'e kadar yazdır, ancak 3'te dur
for i in range(5):
    if i == 3:
        break
    print(i)
#açıklama: i 3 olduğunda döngü break ile sonlanır.

#continue:
#continue komutu döngünün o anki iterasyonunu atlar ve bir sonraki iterasyona geçer.


# Sayıları 5'e kadar yazdır, ancak 3'ü atla
for i in range(5):
    if i == 3:
        continue
    print(i)
#Açıklama: i 3 olduğunda continue devreye girer ve bu iterasyon atlanır, dolayısıyla 3 yazdırılmaz.

#4. else ile Döngüler
#Döngülerle birlikte else kullanmak mümkündür. Döngü tamamlandığında (koşul sağlanmadığında) else bloğu çalıştırılır. Ancak, döngü bir break komutu ile erken sonlandırılmışsa, else bloğu çalışmaz.


# 0'dan 4'e kadar sayılarla döngü, 3'te bitirmeden devam et
for i in range(5):
    print(i)
else:
    print("Döngü tamamlandı!")
#Açıklama: Döngü, range(5) içindeki her sayıyı yazdırdıktan sonra, else bloğu devreye girer ve "Döngü tamamlandı!" mesajını yazdırır.

#Özet
#for döngüsü: İterable üzerinde döner ve her öğeyi işler.
#while döngüsü: Bir koşul doğru olduğu sürece çalışır.
#break: Döngüyü erken sonlandırır.
#continue: O anki iterasyonu atlar ve bir sonraki iterasyona geçer.
#else: Döngü tamamlandığında çalışır, ancak break ile sonlanmışsa çalışmaz.
#Her bir döngü tipi farklı durumlar için uygundur, bu yüzden hangi durumda hangi döngünün kullanılacağı önemlidir.


#foksiyonlar 

#📌 1. Temel Gömülü Fonksiyonlar (Yerleşik Fonksiyonlar)
#Python, tanıtılmış birçok fonksiyon sunar. Bunlar, işlemler , tür dönüşümleri , 
# giriş/çıkış işlemleri ve veri yapıları ile çalışmak için kullanılır.

#🔹 Matematiksel Fonksiyonlar
#Oran	Açıklama	Örnek
#abs(x)	#Sayının mutlak değeri döner.	#abs(-10) → 10
#round(x, n)	#Sayıyı n basamağa yuvarlar.	#round(3.14159, 2) → 3.14
#pow(x, y)	#x'in y'inci kuvvetinin hesapları.	#pow(2, 3) → 8
#sum(iterable)	#Listedeki elemanlar toplar.	#sum([1, 2, 3]) → 6
#min(iterable)	#Listedeki en küçük döngüler.	#min([4, 7, 1, 9]) → 1
#max(iterable)	#Listedeki en büyük döngüler.	#max([4, 7, 1, 9]) → 9
#📌 Örnek:

numbers = [4, -3, 7, -1, 9]
print(abs(-5))  # 5
print(round(3.756, 2))  # 3.76
print(pow(3, 4))  # 81
print(sum(numbers))  # 16
print(min(numbers))  # -3
print(max(numbers))  # 9
# Tür Dönüşüm Fonksiyonları
#Oran	Açıklama	Örnek
#int(x)	Sayıyı tam sayıya çevirir.	#int(3.9) → 3
#float(x)	Sayıyı ondalıklı sayıya çevirir.	#float(10) → 10.0
#str(x)	Veriyi string (metin) türüne çevirir.	#str(42) → "42"
#bool(x)		

#Python'da defFonksiyonu (Fonksiyon Tanımlama)Python'da defanahtarlanabilir,
#  özel bir işlem yapmak için bir fonksiyon (işlev) hesaplamak amacıyla kullanılır. Fonksiyonlar, 
# kodun tekrarını engellemek , programı daha modüler hale getirmek ve daha okunabilir
#  bir yapı oluşturmak için kullanılır.
def topla(a, b):  # a ve b parametre olarak alınıyor
    return a + b  # Toplam değeri döndürülüyor

sonuc = topla(5, 10)  # Fonksiyon çağrılıyor
print(sonuc)  # 15



def topla(a, b):
    return a + b

sonuc = topla(5, 7)
print("Toplam:", sonuc)



#sum() fonksiyonu, Python'da bir dizi veya iterable (liste, demet, set vb.) içindeki sayıları toplamak için 
# kullanılan yerleşik (built-in) bir fonksiyondur.


# Liste içindeki sayıları toplama
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Çıktı: 15

# Başlangıç değeri ekleme
print(sum(numbers, 10))  # Çıktı: 25 (15 + 10)

# Tuple (demet) ile kullanımı
values = (10, 20, 30)
print(sum(values))  # Çıktı: 60

# Set ile kullanımı
num_set = {4, 5, 6}
print(sum(num_set))  # Çıktı: 15


#Dikkat Edilmesi Gerekenler:sum() fonksiyonu sadece sayılarla çalışır. Eğer içinde string gibi
#  farklı veri tipleri varsa hata alırsınız.sum() fonksiyonu çok büyük listelerde performans açısından 
# math.fsum() fonksiyonuna göre daha yavaş olabilir. math.fsum() özellikle kayan nokta (float) işlemleri 
# için daha hassas sonuç verir.




# sort() Fonksiyonu Nedir?Python'da sort() fonksiyonu, listelerdeki elemanları sıralamak için kullanılan
#  bir metottur. Varsayılan olarak küçükten büyüğe sıralama yapar, ancak ters sıralama da mümkündür.


list.sort(key=None, reverse=False)



#key (isteğe bağlı): Sıralama için özel bir fonksiyon belirtebilirsiniz.reverse (isteğe bağlı):
#  True olursa büyükten küçüğe sıralar. Varsayılan olarak False yani küçükten büyüğedir.




numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)  # Çıktı: [1, 2, 5, 7, 9]




words = ["elma", "armut", "üzüm", "çilek"]
words.sort()
print(words)  # Çıktı: ['armut', 'çilek', 'elma', 'üzüm']



words = ["elma", "armut", "üzüm", "çilek"]
words.sort()
print(words)  # Çıktı: ['armut', 'çilek', 'elma', 'üzüm']



words.sort(key=len)
print(words)  # Çıktı: ['elma', 'üzüm', 'armut', 'çilek']





words.sort(key=lambda x: x[-1])
print(words)  # Çıktı: ['armut', 'çilek', 'elma', 'üzüm']



#sorted() ile sort() Arasındaki Fark sort() listenin kendisini değiştirir ve None döner.
# sorted() yeni bir liste döndürür, orijinal liste değişmez.


numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)  # Yeni bir liste oluşturur
print(sorted_numbers)  # Çıktı: [1, 2, 5, 7, 9]
print(numbers)  # Orijinal liste değişmez: [5, 2, 9, 1, 7]


#Sonuçsort() sadece listelerde kullanılır, sorted() ise her türlü iterable (tuple, dictionary, string vb.)
#  ile çalışabilir.Orijinal listeyi değiştirmek istiyorsan sort(),
#  yeni bir sıralı liste oluşturmak istiyorsan sorted() kullan.





#Python'da replace() metodu, bir string (metin) içindeki belirli bir karakter veya alt diziyi 
# (substring) başka bir şeyle değiştirmek için kullanılır.

# "\r" kendisinden sonra gelen metnin satırın başına 
# yazılmasını sağlar.

#python string metotları

# **`capitalize()`** – İlk karakteri büyük harfe çevirir.  
# **`casefold()`** – Metni küçük harfe çevirir.  
# **`center()`** – Ortalanmış bir string döndürür.  
# **`count()`** – Belirtilen değerin string içinde kaç kez geçtiğini döndürür.  
# **`encode()`** – Metnin kodlanmış bir versiyonunu döndürür.  
# **`endswith()`** – Eğer string belirtilen değerle bitiyorsa `True` döndürür.  
# **`expandtabs()`** – Sekme (tab) boyutunu belirler.  
# **`find()`** – Belirtilen değeri string içinde arar ve bulunduğu konumu döndürür.  
# **`format()`** – String içinde belirtilen değerleri biçimlendirir.  
# **`format_map()`** – String içinde belirtilen değerleri biçimlendirir.  
# **`index()`** – Belirtilen değeri string içinde arar ve bulunduğu konumu döndürür.  
# **`isalnum()`** – String’in tüm karakterleri alfanümerikse `True` döndürür.  
# **`isalpha()`** – String’in tüm karakterleri harfse `True` döndürür.  
# **`isascii()`** – String’in tüm karakterleri ASCII karakterleriyse `True` döndürür.  
# **`isdecimal()`** – String’in tüm karakterleri ondalıksa `True` döndürür.  
# **`isdigit()`** – String’in tüm karakterleri rakamsa `True` döndürür.  
# **`isidentifier()`** – String, bir Python tanımlayıcısı ise `True` döndürür.  
# **`islower()`** – String’in tüm harfleri küçük harfse `True` döndürür.  
# **`isnumeric()`** – String’in tüm karakterleri numerikse `True` döndürür.  
# **`isprintable()`** – String’in tüm karakterleri yazdırılabilir karakterlerse `True` döndürür.  
# **`isspace()`** – String yalnızca boşluk karakterlerinden oluşuyorsa `True` döndürür.  
# **`istitle()`** – String başlık biçimindeyse (her kelimenin ilk harfi büyükse) `True` döndürür.  
# **`isupper()`** – String’in tüm harfleri büyük harfse `True` döndürür.  
# **`join()`** – Bir iterable’ın elemanlarını belirtilen ayraçla birleştirir.  
# **`ljust()`** – String’in sola yaslanmış bir versiyonunu döndürür.  
# **`lower()`** – String’i küçük harfe çevirir.  
# **`lstrip()`** – String’in sol tarafındaki boşlukları kaldırır.  
# **`maketrans()`** – Çeviri işlemleri için bir dönüşüm tablosu döndürür.  
# **`partition()`** – String’i belirtilen değer etrafında üç parçaya böler.  
# **`replace()`** – String içinde belirtilen değeri başka bir değerle değiştirir.  
# **`rfind()`** – String içinde belirtilen değerin son geçtiği konumu döndürür.  
# **`rindex()`** – String içinde belirtilen değerin son geçtiği konumu döndürür.  
# **`rjust()`** – String’in sağa yaslanmış bir versiyonunu döndürür.  
# **`rpartition()`** – String’i belirtilen değer etrafında üç parçaya böler (sağdan başlar).  
# **`rsplit()`** – String’i belirtilen ayraçla böler ve bir liste döndürür.  
# **`rstrip()`** – String’in sağ tarafındaki boşlukları kaldırır.  
# **`split()`** – String’i belirtilen ayraç ile böler ve bir liste döndürür.  
# **`splitlines()`** – String’i satır sonlarına göre böler ve bir liste döndürür.  
# **`startswith()`** – Eğer string belirtilen değerle başlıyorsa `True` döndürür.  
# **`strip()`** – String’in başındaki ve sonundaki boşlukları kaldırır.  
# **`swapcase()`** – Büyük harfleri küçük, küçük harfleri büyük yapar.  
# **`title()`** – Her kelimenin ilk harfini büyük yapar.  
# **`translate()`** – Çeviri tablosuna göre string içinde değişiklik yapar.  
# **`upper()`** – String’i büyük harfe çevirir.  
# **`zfill()`** – String’in başına belirtilen sayıda `0` ekler.  



#Python'da extend() metodu, bir listeye başka bir iterable (liste, demet, set vb.) eklemek için kullanılır.


liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste1.extend(liste2)

print(liste1)  # Çıktı: [1, 2, 3, 4, 5, 6]



#Python'da insert() metodu, bir listeye belirli bir indekse öğe eklemek için kullanılır.



#Python'da bir tuple'ı listeye çevirmek için list() fonksiyonunu kullanabilirsin.

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)

print(my_list)  
# Çıktı: [1, 2, 3, 4, 5]



# anagram örneklerine geldik soru olarak bolca cıkan anagram sorusunun yöntemleri 

def anagram_mi(kelime1, kelime2):
    return sorted(kelime1) == sorted(kelime2)

# Örnek kullanım
print(anagram_mi("listen", "silent"))  # True
print(anagram_mi("hello", "world"))    # False



from collections import Counter

def anagram_mi(kelime1, kelime2):
    return Counter(kelime1) == Counter(kelime2)

# Örnek kullanım
print(anagram_mi("listen", "silent"))  # True
print(anagram_mi("hello", "world"))    # False




def harf_sayisi(kelime):
    harfler = {}
    for harf in kelime:
        harfler[harf] = harfler.get(harf, 0) + 1
    return harfler

def anagram_mi(kelime1, kelime2):
    return harf_sayisi(kelime1) == harf_sayisi(kelime2)

# Örnek kullanım
print(anagram_mi("listen", "silent"))  # True
print(anagram_mi("python", "java"))    # False




anagram_mi = lambda k1, k2: sorted(k1) == sorted(k2)

print(anagram_mi("earth", "heart"))  # True
print(anagram_mi("hello", "python")) # False





kelime1 = "listen"
kelime2 = "silent"

anagram = sorted(kelime1) == sorted(kelime2)

print(anagram)  # Çıktı: True




kelime1 = "listen"
kelime2 = "silent"

harfler1 = {}
harfler2 = {}

for harf in kelime1:
    harfler1[harf] = harfler1.get(harf, 0) + 1

for harf in kelime2:
    harfler2[harf] = harfler2.get(harf, 0) + 1

anagram = harfler1 == harfler2

print(anagram)  # Çıktı: True





# ASAL SAYI BULMA 


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




# Python *argsNedir? Ne İşe Yarar?Python'da *args, bir fonksiyona belirsiz sayıda aralıkları
#  değiştirmek için kullanılır. Kaç tane birikimini bilmeyensan *args kullanabilirsin.

# Eğer bir fonksiyon sabit sayıda parametre almak yerine esnek olmalıysa , *argskullanabilirsin.



def topla(*args):
    toplam = sum(args)
    print("Toplam:", toplam)

topla(3, 5)         # Çıktı: Toplam: 8
topla(1, 2, 3, 4)   # Çıktı: Toplam: 10
topla





#  Özet: passKullanım Alanları
#✅ Fonksiyonları boş bırakmak için
#✅ if-elsebloklarını şimdilik boş bırakmak için
#✅ Boş döngüler veya sınıflar tükenmek için
#📌 Kısacası passbir "boş kod" ifadesidir! Hata vermemesi için kodu yerinde tutar ama hiçbir işlem yapmaz.


#Python'da .center() metodu, bir stringi belirli bir genişliğe ortalayarak hizalamak için kullanılır.
#  Metod, belirtilen toplam genişliği sağlamak için stringin sağına ve soluna boşluk veya belirttiğin 
# başka bir karakter ekler.


#string.center(width, fillchar)
#width: Ortalanacak toplam genişlik (zorunlu).
#fillchar: Boşlukları dolduracak karakter (varsayılan olarak boşluk " " kullanılır, isteğe bağlıdır).
#Örnekler:
#Boşluk ile Ortalamak:

text = "Python"
print(text.center(20))  # '       Python       '
#Özel Karakter ile Ortalamak:


text = "Python"
print(text.center(20, "-"))  # '-------Python-------'
#Eğer belirtilen genişlik (width), string uzunluğundan küçük veya eşitse,
#  string değiştirilmeden döndürülür.


#Tüm Hata Türleri Listesi


#Hata Türü	Açıklama
#SyntaxError	Yanlış sözdizimi kullanıldığında oluşur.
#NameError	Tanımlanmamış bir değişken çağrıldığında oluşur.
#TypeError	Yanlış türde bir veri kullanıldığında oluşur.
#IndexError	Geçersiz bir liste indeksi kullanıldığında oluşur.
#KeyError	Sözlükte bulunmayan bir anahtar çağrıldığında oluşur.
#ValueError	Fonksiyonun aldığı değer uygun olmadığında oluşur.
#AttributeError	Bir nesnenin var olmayan bir metoduna erişildiğinde oluşur.
#ZeroDivisionError	Bir sayı sıfıra bölündüğünde oluşur.
#ModuleNotFoundError	import edilen bir modül bulunamadığında oluşur.
#ImportError	Modül içinden içeri aktarılan öğe bulunamadığında oluşur.
#FileNotFoundError	Açılmak istenen dosya bulunamadığında oluşur.
#PermissionError	Bir dosyaya erişim izni olmadığında oluşur.
#IsADirectoryError	Bir dosya yerine dizin açılmaya çalışıldığında oluşur.
#MemoryError	Bellek yetersiz kaldığında oluşur.
#RecursionError	Özyineleme (recursive) çok derinleştiğinde oluşur.
#RuntimeError	Belirli bir açıklaması olmayan genel bir hata türüdür.
#NotImplementedError	Bir metodun henüz uygulanmadığını belirtmek için kullanılır.



# Parantez eksikliği
print("Merhaba Dünya"  
# SyntaxError: '(' was never closed



print(x)  # NameError: name 'x' is not defined



print("5" + 5)  # TypeError: can only concatenate str (not "int") to str


liste = [1, 2, 3]
print(liste[5])  # IndexError: list index out of range


sozluk = {"ad": "Ali"}
print(sozluk["yas"])  # KeyError: 'yas'



print(int("abc"))  # ValueError: invalid literal for int() with base 10: 'abc'



sayi = 10
sayi.append(5)  # AttributeError: 'int' object has no attribute 'append'




import yanlis_modul  # ModuleNotFoundError: No module named 'yanlis_modul'

from math import yanlis_fonksiyon  # ImportError: cannot import name 'yanlis_fonksiyon'


with open("olmayan_dosya.txt", "r") as f:
    icerik = f.read()  # FileNotFoundError: No such file or directory


import os
os.remove("C:/Windows/system32")  # PermissionError: [WinError 5] Access is denied

with open("C:/Users", "r") as f:
    icerik = f.read()  # IsADirectoryError

buyuk_liste = [1] * (10**10)  # MemoryError



def sonsuz():
    return sonsuz()

sonsuz()  # RecursionError: maximum recursion depth exceeded



import math
print(math.sqrt(-1))  # ValueError: math domain error




def yas_kontrol(yas):
    if yas < 18:
        raise ValueError("Yaş 18'den küçük olamaz!")

yas_kontrol(15)  # ValueError: Yaş 18'den küçük olamaz!



#hatalar 

#try	Hata oluşturabilecek kod buraya yazılır.
#except	try bloğunda hata olursa burası çalışır.
#except as hata	Hata mesajını bir değişkene atayarak detaylı inceleme yapar.
#finally	Hata olsa da olmasa da çalışır. Genellikle temizleme işlemleri için kullanılır.
#raise	Özel hata fırlatmak için kullanılır.
#raise Exception	Genel bir hata fırlatır.
#as	except ile birlikte kullanılarak hata mesajını bir değişkene atamaya yarar.





try:
    sayı = int("abc")  # Hata: "abc" tam sayıya çevrilemez
except ValueError:
    print("Bir hata oluştu: Değer hatası")






try:
    sayı = int("abc")
except ValueError as hata:
    print("Bir hata oluştu:", hata)





try:
    dosya = open("dosya.txt", "r")
    içerik = dosya.read()
except FileNotFoundError:
    print("Dosya bulunamadı!")
finally:
    print("Bu blok her zaman çalışır.")





def pozitif_sayı_kontrol(sayı):
    if sayı < 0:
        raise ValueError("Sayı negatif olamaz!")
    return sayı

try:
    print(pozitif_sayı_kontrol(-5))
except ValueError as hata:
    print("Hata:", hata)





def yaş_kontrol(yaş):
    if yaş < 18:
        raise Exception("Yaş 18'den küçük olamaz!")
    return "Giriş başarılı"

try:
    print(yaş_kontrol(16))
except Exception as hata:
    print("Hata:", hata)



#Python'da .format() metodu, metin içinde değişkenleri yerleştirmek için kullanılan güçlü bir yöntemdir.

isim = "Ali"
yas = 25
mesaj = "Merhaba, benim adım {} ve ben {} yaşındayım.".format(isim, yas)
print(mesaj)



mesaj = "Benim adım {0}, yaşım {1} ve {0} ismini seviyorum.".format("Ali", 25)
print(mesaj)


mesaj = "Adım {ad}, yaşım {yas}".format(ad="Ayşe", yas=30)
print(mesaj)


isim = "Mehmet"
yas = 40
mesaj = f"Merhaba, benim adım {isim} ve ben {yas} yaşındayım."
print(mesaj)


sayi = 1000000
print("Para: {:,}".format(sayi))  # 1,000,000 şeklinde yazar


#Python'da random.uniform(a, b),rastgele ondalıklı (float) bir sayı üretimi için



import random

sayi = random.uniform(1.5, 5.5)  # 1.5 ile 5.5 arasında rastgele bir float sayı üretir
print(sayi)


#Kolay Sorular:
#1. En Büyük Sayıyı Bul

def en_buyuk(a, b, c):
    return max(a, b, c)

print(en_buyuk(10, 25, 7))  # Çıktı: 25
#2. Tek mi Çift mi?

def tek_mi_cift_mi(sayi):
    return "Çift" if sayi % 2 == 0 else "Tek"

print(tek_mi_cift_mi(8))  # Çıktı: Çift
print(tek_mi_cift_mi(7))  # Çıktı: Tek
#3. Faktöriyel Hesaplama

def faktoriyel(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))  # Çıktı: 120
#4. Palindrom Kontrolü

def palindrom_mu(kelime):
    return kelime == kelime[::-1]

print(palindrom_mu("kayak"))  # Çıktı: True
print(palindrom_mu("python")) # Çıktı: False
#5. Listeyi Ters Çevir

def ters_cevir(liste):
    return liste[::-1]

print(ters_cevir([1, 2, 3, 4, 5]))  # Çıktı: [5, 4, 3, 2, 1]
Orta Seviye Sorular:
6. Fibonacci Dizisi

def fibonacci(n):
    dizi = [0, 1]
    for _ in range(n - 2):
        dizi.append(dizi[-1] + dizi[-2])
    return dizi[:n]

print(fibonacci(6))  # Çıktı: [0, 1, 1, 2, 3, 5]
7. Asal Sayı Kontrolü

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

print(asal_mi(7))  # Çıktı: True
print(asal_mi(10)) # Çıktı: False
#8. Kelime Frekansı

def kelime_frekansi(cumle):
    kelimeler = cumle.split()
    frekans = {}
    for kelime in kelimeler:
        frekans[kelime] = frekans.get(kelime, 0) + 1
    return frekans

print(kelime_frekansi("elma armut elma muz elma"))  
# Çıktı: {'elma': 3, 'armut': 1, 'muz': 1}
#9. Mükemmel Sayı Kontrolü

def mukemmel_sayi(sayi):
    toplam = sum(i for i in range(1, sayi) if sayi % i == 0)
    return toplam == sayi

print(mukemmel_sayi(28))  # Çıktı: True
print(mukemmel_sayi(12))  # Çıktı: False
#10. En Uzun Kelimeyi Bul

def en_uzun_kelime(cumle):
    kelimeler = cumle.split()
    return max(kelimeler, key=len)

print(en_uzun_kelime("Python programlama dili harika"))  # Çıktı: "programlama"
Zor Sorular:
#11. Sayının Basamaklarının Toplamı

def basamak_toplami(sayi):
    return sum(int(rakam) for rakam in str(sayi))

print(basamak_toplami(456))  # Çıktı: 15
#12. Özyinelemeli Üs Alma

def us_al(a, b):
    if b == 0:
        return 1
    return a * us_al(a, b - 1)

print(us_al(2, 3))  # Çıktı: 8
#13. En Çok Tekrar Eden Harfi Bul

from collections import Counter

def en_cok_tekrar_eden_harf(metin):
    frekans = Counter(metin.replace(" ", ""))
    return max(frekans, key=frekans.get)

print(en_cok_tekrar_eden_harf("merhaba dünya"))  # Çıktı: 'a'
#14. Dizi İçindeki En Yakın Sayılar

def en_yakin_sayilar(liste):
    liste.sort()
    en_yakin = min(zip(liste, liste[1:]), key=lambda x: abs(x[0] - x[1]))
    return en_yakin

print(en_yakin_sayilar([10, 23, 45, 41, 18]))  # Çıktı: (41, 45)
#15. zip() Fonksiyonunu Taklit Et

def benim_zip(liste1, liste2):
    return [(liste1[i], liste2[i]) for i in range(min(len(liste1), len(liste2)))]

print(benim_zip([1, 2, 3], ['a', 'b', 'c']))  
# Çıktı: [(1, 'a'), (2, 'b'), (3, 'c')]
