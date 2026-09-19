def validate_pnr(nr_string):
    summa = 0

    # Beräkna summan för de nio första siffrorna
    for i in range(9):
        siffra = int(nr_string[i])

        if i % 2 == 0:
            produkt = siffra * 2
        else:
            produkt = siffra

        # Om produkten är tvåsiffrig summeras siffrorna
        if produkt >= 10:
            produkt = produkt // 10 + produkt % 10

        summa += produkt

    # Räkna ut kontrollsiffran
    kontrollsiffra = (10 - summa % 10) % 10

    return kontrollsiffra == int(nr_string[9])


if __name__ == "__main__":
    print('Välkommen till "Personnummer-kollen"')
    print("-------------------------------------")

    fortsatt = "J"

    while fortsatt == "J":
        personnummer = input("Ange ett personnummer med 10 siffror: ")

        if validate_pnr(personnummer):
            print("\nOK - Personnumret är giltigt")
        else:
            print("\nFEL - Personnumret är ogiltigt")

        fortsatt = input(
            "\nVill du kontrollera fler personnummer (J/N)? "
        ).upper()

    print("\nProgrammet avslutas ..")