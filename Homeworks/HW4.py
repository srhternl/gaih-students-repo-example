class HangmanOyunu:
    aranan_kelime = ""
    dogru_harf = list()
    yanlis = 0

    def kelime_yaz(self, word_list):
        for character in self.dogru_harf:
            print(character, end=" ")

    def harf_al(self):
        self.aranan_kelime = input("Bulunacak kelimeyi yazın: ")
        self.dogru_harf = ['_' for i in range(len(self.aranan_kelime))]

    def harf_karsilastir(self, tahmin):
        sayac = 0
        for harf in self.aranan_kelime:
            if tahmin == harf:
                self.dogru_harf[sayac] = harf
            sayac += 1

    def oyun_basladi(self):
        durum = True
        while durum:
            print("Retries:", (len(self.aranan_kelime))-self.yanlis)
            harf_tahmin = input("Senin tahminin:")
            self.harf_karsilastir(harf_tahmin)
            self.kelime_yaz(self.dogru_harf)
            self.oyun_bitti()
            if len(self.aranan_kelime) - self.yanlis == 1:
                durum = False
            self.yanlis = self.yanlis + 1
            if harf_tahmin in self.aranan_kelime:
                durum = True
                self.yanlis -= 1
        else:
           print("\nHakkın Bitti!!!")
           quit()

    def oyun_bitti(self):
        if "_" not in self.dogru_harf:
            print("\nOyun Bitti, Görüşürüz")
            quit()

oyun = HangmanOyunu()
oyun.harf_al()
oyun.oyun_basladi()


