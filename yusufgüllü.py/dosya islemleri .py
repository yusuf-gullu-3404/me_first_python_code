
with open("tarih islemleri.txt ","w",encoding="utf-8") as f:
    icerik = f.readlines()
    for i in icerik :
        print(i,end="")


#with open("tarih islemleri.txt ", "w", encoding="utf-8") as f:
 #   f.write("Bu bir deneme dosyasıdır.")  # Örnek içerik ekle
#print("Dosya oluşturuldu!")

# Önce dosyayı oluştur ve içine yaz
with open("prt ödevi .txt", "w", encoding="utf-8") as f:
    f.write("Bu dosya Python tarafından oluşturuldu.\nprt ödevi burada olacak.")

# Dosyayı kapattıktan sonra tekrar aç ve oku
with open("Tarih işlemleri.txt", "r", encoding="utf-8") as f:
    icerik = f.readlines()  # Satırları oku

# Okunan içeriği ekrana yazdır
for satir in icerik:
    print(satir, end="")
