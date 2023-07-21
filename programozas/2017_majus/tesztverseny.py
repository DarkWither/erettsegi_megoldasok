# Ladányi Attila

# 1.

class Valaszok:
    def __init__(self, azonosito, valaszok):
        self.azonosito = azonosito
        self.valaszok = valaszok

    def __repr__(self):
        return f"{self.azonosito} {self.valaszok}"

lista = []

fajl = open("valaszok.txt", "r", encoding="utf-8")

megoldas = fajl.readline().strip()

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Valaszok(*sor))

print("1. feladat: Az adatok beolvasása ")

# 2.

print(f"\n2. feladat: A vetélkedőn {len(lista)} versenyző indult.")

# 3.

beker_azonosito = input("\n3. feladat: A versenyző azonosítója = ")

beker_valasz = 0

for valasz in lista:
    if valasz.azonosito == beker_azonosito:
        beker_valasz = valasz

print(f"{beker_valasz.valaszok}\t(a versenyző válasza)")

# 4.

print(f"\n4. feladat:\n{megoldas}\t(a helyes megoldás)")

bekert_helyes_valaszok = "" # ha jó válasz, akkor += "+", ha nem, akkor += " "

for betuindex in range(len(beker_valasz.valaszok)):
    if beker_valasz.valaszok[betuindex] == megoldas[betuindex]:
        bekert_helyes_valaszok += "+"
    else:
        bekert_helyes_valaszok += " "

print(f"{bekert_helyes_valaszok}\t(a versenyző helyes válaszai)")

# 5.

beker_feladat_sorszam = int(input("\n5. feladat: A feladat sorszáma = "))

hany_helyes_valasz = 0

for valasz in lista:
    if valasz.valaszok[beker_feladat_sorszam - 1] == megoldas[beker_feladat_sorszam - 1]: # index miatt -1
        hany_helyes_valasz += 1

szazalek = round((hany_helyes_valasz / len(lista)) * 100, 2)

print(f"A feladatra {hany_helyes_valasz} fő, a versenyzők {szazalek}%-a adott helyes választ.")

# 6.

print("\n6. feladat: A versenyzők pontszámának meghatározása")

pontok_feladatonkent = {
    1: 3,
    2: 3,
    3: 3,
    4: 3,
    5: 3,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 4,
    11: 5,
    12: 5,
    13: 5,
    14: 6
} # melyik feladat mennyi pontot ér

azonositok_es_pontok = {} # kulcs: azonosító, érték: pontok száma; következő feladathoz

kiir = open("pontok.txt", "w", encoding="utf-8")

for valasz in lista:
    elert_pontok = 0

    for betuindex in range(len(beker_valasz.valaszok)):
        if valasz.valaszok[betuindex] == megoldas[betuindex]:
            elert_pontok += pontok_feladatonkent[betuindex + 1] # +1 index miatt

    kiir.write(f"{valasz.azonosito} {elert_pontok}\n")

    azonositok_es_pontok[valasz.azonosito] = elert_pontok

# 7.

print("\n7. feladat: A verseny legjobbjai:")

harom_legtobb_pont = [] # a három legnagyobb pontszám

for pont in sorted(set(azonositok_es_pontok.values()), reverse=True):
    if len(harom_legtobb_pont) != 3: # ha még nincs benne a három legnagyobb
        harom_legtobb_pont.append(pont)
    else: # ha már benne van
        break

pontokbol_hany = {} # kulcs: pontszám, érték: hány darab

for azonosito, pont in azonositok_es_pontok.items():
    if pont in harom_legtobb_pont:
        pontokbol_hany[pont] = pontokbol_hany.get(pont, 0) + 1

nem_jo_helyek = [] # azok a helyek indexei, amelyekből legalább 4 darab van
sorszam = 0

for pont in sorted(pontokbol_hany.keys()): # növekvő sorrend
    if pontokbol_hany[pont] > 3:
        nem_jo_helyek.append(sorszam)

    sorszam += 1

for pontszam_index in range(0, 3):
    if pontszam_index not in nem_jo_helyek: # ne legyen olyan hely, amit többen, mint 3-an nyertek el
        for azonosito, pont in azonositok_es_pontok.items():
            if pont == harom_legtobb_pont[pontszam_index]:
                print(f"{pontszam_index + 1}. díj ({pont} pont): {azonosito}") # pontszam_index + 1 == helyezés
