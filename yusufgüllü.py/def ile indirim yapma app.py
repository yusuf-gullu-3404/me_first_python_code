def indirimyap(fiyat,yüzde) :
    indirim = fiyat * (yüzde/100)
    indirimli_fiyat = fiyat - indirim 
    print("indirimli fiyatı :", indirimli_fiyat,"tl")

indirimyap(280,5)