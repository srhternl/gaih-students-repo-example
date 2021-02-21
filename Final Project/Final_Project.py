class Tarifler:
    def __init__(self, tarif_isim):
        self.tarif_isim = tarif_isim

    def yemege_basla(self):
        print("\nTarif İsmi:", self.tarif_isim)

    def ocak_acma(self):
        print("Ocağı Açalım.")

    def tuz_ekle(self):
        print("Tuz Ekleyelim.")

    def ocak_koy(self):
        print("Tencereyi Ocağa Koyalım.")

    def kavurma(self):
        print("Tencereye koyulan malzemeleri kavuralım.")

    def tenecere_ekle(self):
        print("Malzemeleri tencere koyalım.")

    def baharat_ekle(self):
        print("İstediğimiz baharatları tencere koyalım.")

    def su_ekle(self):
        print("Su ekleyelim.")

    def tencere_kapa(self):
        print("Tenceremizin ağzını kapatıp 45 dakika kısık ateşte bekletelim.")

    def bitir(self):
        print("Afiyet Olsun.")

class Nohut_Tarif(Tarifler):
    def __init(self, tarif_isim):
        super().__init__(tarif_isim)

    def nohut_hazirla(self):
        print("Nohutları yıkayıp su dolu bir kabın içinde 5 saat bekletelim.")

    def nohut_suzgec(self):
        print("Nohutları sudan geçirip süzgeçe alalım.")

    def malzemeleri_hazırla(self):
        print("Zeytinyağını ve küçük küp doğranmış kuru soğanı, biberleri hazırlayalım.")

    def nohut_koy(self):
        print("Süzülmüş nohutları tencereye koyup kavurmaya devam edelim.")

    def basla(self):
        self.yemege_basla()
        self.nohut_hazirla()
        self.nohut_suzgec()
        self.malzemeleri_hazırla()
        self.tenecere_ekle()
        self.ocak_acma()
        self.ocak_koy()
        self.kavurma()
        self.nohut_koy()
        self.tuz_ekle()
        self.baharat_ekle()
        self.su_ekle()
        self.tencere_kapa()
        self.bitir()

class Kuru_Fasulye_Tarif(Tarifler):
    def __init(self, tarif_isim):
        super().__init__(tarif_isim)
    def fasulye_hazirla(self):
        print("Fasulyeleri yıkayıp su dolu bir kabın içinde 5 saat bekletelim.")

    def malzemeleri_hazırla(self):
        print("4 yemek kaşığı sıvı yağ ve 2 yemek kaşığı tereyağını hazırlayalım.")

    def tenecere_ekle(self):
        print("Malzemeleri tencere koyalım.")

    def fasulye_koy(self):
        print("Suda beklletilen fasulyeleri tencereye koyup kavurmaya devam edelim.")

    def salca_ekle(self):
        print("Tencereye 1 yemek kaşığı salça ekleyelim.")

    def karistirma(self):
        print("Tencereye koyulan malzemeleri 1-2 dakika karıştıralım.")

    def basla(self):
        self.yemege_basla()
        self.fasulye_hazirla()
        self.malzemeleri_hazırla()
        self.tenecere_ekle()
        self.ocak_acma()
        self.ocak_koy()
        self.kavurma()
        self.salca_ekle()
        self.fasulye_koy()
        self.karistirma()
        self.su_ekle()
        self.tuz_ekle()
        self.baharat_ekle()
        self.tencere_kapa()
        self.bitir()

class Ezogelin_Corbasi_Tarif(Tarifler):
    def __init(self, tarif_isim):
        super().__init__(tarif_isim)

    def kaynatma(self):
        print("Teneceredeki suyu kaynatalım.")

    def mercimek_ekle(self):
        print("Tencereye 2 çay kasığı mercimek ekleyelim.")

    def malzeme_ekle(self):
        print("3 yemek kaşığı pirinci, 2 yemek kaşığı bulguru ekleyelim.")

    def pisirme(self):
        print("Yaklaşık 35 dakika kadar ve kırmızı mercimekler yumuşayana kadar pişirelim")

    def basla(self):
        self.yemege_basla()
        self.tenecere_ekle()
        self.su_ekle()
        self.ocak_acma()
        self.ocak_koy()
        self.kaynatma()
        self.mercimek_ekle()
        self.malzeme_ekle()
        self.tuz_ekle()
        self.pisirme()
        self.bitir()


choice = '0'
while choice != '4':
    print("\nMain Choice: Choose 1 of 3 choices")
    print("Nohut Tarifi")
    print("Kuru Fasulye Tarifi")
    print("Ezogelin Çorbası Tarifi")
    print("Programdan Çıkış")

    choice = input("Seçiminizi Yapınız: ")

    if choice == "1":
        nohut_tarif = Nohut_Tarif("Nohut \n")
        nohut_tarif.basla()
    elif choice == "2":
        kuru_fasulye_tarif = Kuru_Fasulye_Tarif("Kuru Fasulye \n")
        kuru_fasulye_tarif.basla()
    elif choice == "3":
        ezogelin_corbasi_tarif = Ezogelin_Corbasi_Tarif("Ezogelin Çorbası \n ")
        ezogelin_corbasi_tarif.basla()
    elif choice == "4":
        quit()
    else:
        print("Yanlış seçim yaptınız.\n")