
class Oyuncu ():
    def __init__(self,isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 0

    def hareket_et (self):
        print("hareket ediliyor....")

    def puan_kazan(self):
        print("puan kazanıldı....")
    def puan_kaybet(self):
        print("puan kayebdiliyor...")

class asker(Oyuncu):
    memleket = "Kayseri"
    def __init__(self,*args):
        super().__init__(*args)
        self.guc = 100

class isci(Oyuncu):
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 70

class yonetici(Oyuncu):
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 50
