ukoly = []

try:
    soubor = open("ukoly.txt", "r")
    for radek in soubor:
        ukoly.append(radek.strip())

    soubor.close()

except:
    pass



a = True
while a:
    print()
    print("1 - Zadat ukol")
    print("2 - zobrazit ukoly")
    print("3 - smazat ukol")
    print("4 - konec programu")
    print()

    volba = int(input("Zadej moznost "))

    if volba == 1:
        ukol = input("Zadej ukol: ")
        ukoly.append(ukol)
        print()
    
    elif volba == 2:
        for i in range(len(ukoly)):
            print(i + 1, " - ", ukoly[i])
        print()

    elif volba == 3:
        smazat = int(input("Zadej cislo ukolu ktere chces smazat "))
        ukoly.pop(smazat - 1)
        print()

    elif volba == 4:
        soubor = open("ukoly.txt", "w")
        for i in range(len(ukoly)):
            soubor.write(ukoly[i] + "\n")
        soubor.close()
        print("konec programu")
        break


