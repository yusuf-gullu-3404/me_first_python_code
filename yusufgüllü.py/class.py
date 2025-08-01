class Bankahesabı:
    def __init__(self,hesapsahibi):
        self.hesapsahibi = hesapsahibi
        self.bakiye = 0.0


    def get_bakiye(self):
        return self.bakiye

    
    
    def parayatir(self,miktar):
        self.bakiye += miktar
        return self.bakiye
    

    def paracek(self,miktar):
        self.bakiye -= miktar
        return self.bakiye
    
hesap = Bankahesabı("yusuf güllü")
sonuc = hesap.parayatir(1000)
print(hesap.get_bakiye())
hesap.paracek(500)
print(hesap.get_bakiye())
hesap.paracek(200)
print(hesap.get_bakiye())

