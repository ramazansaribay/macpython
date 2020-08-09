class Araba:
    marka = ""
    renk = ""
    plaka = ""
    hiz = 0

    def hizArttir(self):
        self.hiz += 10
        return self.hiz


araba1 = Araba()
araba1.marka = "Citroen"
araba1.renk = "Siyah"
araba1.plaka = "35BEB59"

print("-------MY CAR--------")
print(f"Marka:{araba1.marka}\nRenk:{araba1.renk}\nPlaka:{araba1.plaka}")
araba1.hizArttir()
print("Hız:",araba1.hiz)