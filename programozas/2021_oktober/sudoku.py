# Ladányi Attila

# 1.

bekerfajl = input("1. feladat\nAdja meg a bemeneti fájl nevét! ")
bekersor = int(input("Adja meg egy sor számát! ")) - 1
bekeroszlop = int(input("Adja meg egy oszlop számát! ")) - 1

# 2.

lista = [] # kétdimenziós, soronként a számok
lepeslista = [] # kétdimenziós, lépések listája, egy lépés: [ertek, sor, oszlop]

fajl = open(bekerfajl, "r", encoding="utf-8")

for index in range(9): # az első kilenc sorra
    sor = fajl.readline().strip().split()
    sor_szamokkent = [int(szam) for szam in sor]
    lista.append(sor_szamokkent)

for sor in fajl:
    sor = sor.strip().split()
    sor_szamokkent = [int(szam) for szam in sor]
    lepeslista.append(sor_szamokkent)

# 3.

print("\n3. feladat")

ott = lista[bekersor][bekeroszlop]

if ott == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {ott}")

resztablak = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def resztabla(sor, oszlop):
    return resztablak[sor // 3][oszlop // 3]

print(f"A hely a(z) {resztabla(bekersor, bekeroszlop)} résztáblázathoz tartozik.")

# 4.

nullak = 0

for sor in lista:
    for szam in sor:
        if szam == 0:
            nullak += 1

print(f"\n4. feladat\nAz üres helyek aránya: {round((nullak / (9 * 9)) * 100, 1)}%")

# 5.

print("\n5. feladat")

for lepes in lepeslista:
    ertek = lepes[0]
    sor = lepes[1] - 1
    oszlop = lepes[2] - 1

    print(f"A kiválasztott sor: {sor + 1} oszlop: {oszlop + 1} a szám: {ertek}")

    helyen_ertek = lista[sor][oszlop]

    azazoszlop = []

    for sor in fajl:
        azazoszlop.append(sor[oszlop])

    azaresztabla = []

    for sor_index in range(9):
        for oszlop_index in range(9):
            if resztabla(sor_index, oszlop_index) == resztabla(sor, oszlop):
                azaresztabla.append(lista[sor_index][oszlop_index])

    if helyen_ertek != 0:
        print("A helyet már kitöltötték.\n")
    elif ertek in lista[sor]:
        print("Az adott sorban már szerepel a szám.\n")
    elif ertek in azazoszlop:
        print("Az adott oszlopban már szerepel a szám.\n")
    elif ertek in azaresztabla:
        print("Az adott résztáblázatban már szerepel a szám.\n")
    else:
        print("A lépés megtehető.\n")
