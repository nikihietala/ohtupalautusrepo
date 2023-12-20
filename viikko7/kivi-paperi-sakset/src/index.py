from kps import KiviPaperiSakset

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan")

        vastaus = input()

        if vastaus == "a":
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            pelityyppi = "pvp"
        elif vastaus == "b":
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            pelityyppi = "helppo"
        elif vastaus == "c":
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            pelityyppi = "vaikea"
        else:
            break

        peli = KiviPaperiSakset.luo_peli(pelityyppi)
        peli.pelaa()

if __name__ == "__main__":
    main()
