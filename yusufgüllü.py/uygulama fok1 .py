def soru1(kelime,sayı):
    print(kelime*sayı)

soru1("yusuf",5)





def alan(kısakenar , uzunkenar ):
    return kısakenar * uzunkenar
    
sonucA = alan(5,15)
print(sonucA)





def cevre(kısakenar , uzunkenar ):
    return kısakenar * 2 + 2 *  uzunkenar
    
sonucc = cevre(5,15)
print(sonucc)





def yazıtura ():
    import random
    sayı = random.random()


    if sayı > 0.5 :
        return "tura "
    else :
        return "yazı"
    
deger = yazıtura()
print(deger)
    