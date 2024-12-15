from kivi_sakset_paperi import KiviSaksetPaperi

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus == "a" or vastaus == "b" or vastaus == "c":
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            peli = KiviSaksetPaperi(vastaus)
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
