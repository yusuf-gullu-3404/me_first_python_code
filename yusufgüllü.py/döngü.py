sayılar = [ 1,2,3,4,5,6,7,8,9,0,]


for sayı in sayılar: 
    print(sayı)


sayılar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for sayı in sayılar:
    ters_sayı = int(str(sayı)[::-1])  # Sayıyı string yap, ters çevir, tekrar integer'a çevir
    print(ters_sayı)


for i in range(1,11):
    print(i)
for i in range(1,11,):
    print(i)