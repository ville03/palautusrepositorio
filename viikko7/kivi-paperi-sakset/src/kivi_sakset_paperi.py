from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KiviSaksetPaperi:
    def __init__(self, peli_moodi):
        self.peli_moodi = peli_moodi

    def pelaa(self):
        if self.peli_moodi == "a":
            peli = KPSPelaajaVsPelaaja()
        elif self.peli_moodi == "b":
            peli = KPSTekoaly()
        else:
            peli = KPSParempiTekoaly()
        peli.pelaa()
