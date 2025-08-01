def yazdır(kelime , adet):
    print(kelime * adet)


yazdır("yusuf güllü\n" , 10)




def listeyecevir(*params):
    liste = []

    for param in params:
        liste.append(param)

    return liste 

result = listeyecevir(1,2,3,4,5,6,7,8,8,9,76,54,34567,8765,432,3,46,765,432,3,2)
print(result)



def asalsayılarıbul(sayı1 , sayı2):
    for sayı in range(sayı1 , sayı2+1):
     if sayı > 1 :
        for i in range(2,sayı) :
           if sayı % i == 0 :
              break
           
        else:
           print(sayı)




sayı1 = int(input("1.sayı gir "))
sayı2 = int(input("2.sayı gir "))


asalsayılarıbul(sayı1,sayı2) 















