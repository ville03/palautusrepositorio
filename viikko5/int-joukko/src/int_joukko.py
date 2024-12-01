class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        return False

    def lisaa(self, n):

        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = n
            self.alkioiden_lukumaara += 1
            return True
        

        if self.kuuluu(n):
            return False
        self.lukujono[self.alkioiden_lukumaara] = n
        self.alkioiden_lukumaara += 1
        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lukumaara == len(self.lukujono):
            taulukko_old = self.lukujono
            self.lukujono = self._luo_lista(self.alkioiden_lukumaara + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lukujono)
        return True

        

    def poista(self, n):
        if n not in self.lukujono:
            return False
        self.lukujono.remove(n)
        self.lukujono.append(0)
        self.alkioiden_lukumaara -= 1
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = []

        for i in range(0, self.alkioiden_lukumaara):
            taulu.append(self.lukujono[i])

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            if i in b_taulu:
                y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):
        b_taulu = b.to_int_list()

        for i in range(0, len(b_taulu)):
            a.poista(b_taulu[i])

        return a

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
    
        tuotos = "{"
        for i in range(0, self.alkioiden_lukumaara - 1):
            tuotos = tuotos + str(self.lukujono[i])
            tuotos = tuotos + ", "
        tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
        tuotos = tuotos + "}"
        return tuotos
