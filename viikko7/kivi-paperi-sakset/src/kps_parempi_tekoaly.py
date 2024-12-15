from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPSPelaajaVsPelaaja):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def pelaa(self):
        return super().pelaa()
    
    def tokan_siirto(self, ekan_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ekan_siirto)
        print(f"Tietokone valitsi: {siirto}")
        return siirto
    
    def _onko_ok_siirto(self, siirto):
        return super()._onko_ok_siirto(siirto)
    