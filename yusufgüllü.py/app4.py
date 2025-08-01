markalar = ( "bmw","mercedes","opel","mazda")
print(markalar)
sayı = len(markalar)
print(sayı)
result1 = markalar[0]
result2 = markalar[3]
print(result1)
print(result2)
markalar = ["bmw", "mercedes", "opel", "mazda"]
markalar[3] = "toyota"  # 3. indeksi değiştiriyoruz
print(markalar)
result = "mercedes" in markalar
print(result)
result = markalar[-2]
print(result)
result = markalar[0:3]
print(result)
markalar = ["bmw", "mercedes", "opel", "mazda"]
markalar[3] = "renault"
markalar[2] = "toyota"
print(markalar)
result = markalar + ["audi" , "nissan"]
print(result)
