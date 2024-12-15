from tuomari import Tuomari


class KPSPelaajaVsPelaaja:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.tokan_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self.tokan_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def tokan_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")


    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
