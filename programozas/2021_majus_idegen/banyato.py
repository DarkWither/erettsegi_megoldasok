# Ladányi Attila

# 1.

lista = []
fajl = open("melyseg.txt", "r", encoding="utf-8")

sorok_szama = int(fajl.readline().strip())
oszlopok_szama = int(fajl.readline().strip()) # első két sor beolvasása

for sor in fajl: # a többi sor beolvasása, kétdimenziós listát csinálunk így
    sor = sor.strip().split() # ebben azonban csak szövegként szerepelnek a számok, alakítsuk ezeket számmá egy új listába
    szamokka_lista = [int(szam) for szam in sor] # ["1", "2", "3"] helyett lesz [1, 2, 3]

    lista.append(szamokka_lista)

# 2.

beker_sor = int(input("2. feladat\nA mérés sorának azonosítója="))
beker_oszlop = int(input("A mérés oszlopának azonosítója="))

bekert_helyen_melyseg = lista[beker_sor - 1][beker_oszlop - 1]

print(f"A mért mélység az adott helyen {bekert_helyen_melyseg} dm")

# 3.

felszin = 0 # minden olyan számnál +=1, ami nem nulla
melysegek_lista = [] # az összes mélységet hozzáadjuk és ebből átlagolunk majd

for sor in lista:
    for godor in sor:
        if godor != 0:
            felszin += 1
            melysegek_lista.append(godor / 10) # /10 hogy méterben szerepeljen benne

atlagos_melyseg = round(sum(melysegek_lista) / len(melysegek_lista), 2)

print(f"3. feladat\nA tó felszíne: {felszin} m2, átlagos mélysége: {atlagos_melyseg} m")

# 4.

legmelyebb_nagysag = 0 # milyen mély a legmélyebb

for sor_index in range(0, sorok_szama):
    for oszlop_index in range(0, oszlopok_szama):
        adott_helyen = lista[sor_index][oszlop_index]

        if adott_helyen > legmelyebb_nagysag:
            legmelyebb_nagysag = adott_helyen

legmelyebb_helyek = [] # koordináták, ahol ilyen mély a tó

for sor_index in range(0, sorok_szama):
    for oszlop_index in range(0, oszlopok_szama):
        adott_helyen = lista[sor_index][oszlop_index]

        if adott_helyen == legmelyebb_nagysag:
            legmelyebb_helyek.append([sor_index + 1, oszlop_index + 1])

print(f"4. feladat\nA tó legnagyobb mélysége: {legmelyebb_nagysag} dm")

print("A legmélyebb helyek sor-oszlop koordinátái:")

for koordinatak in legmelyebb_helyek:
    print(f"({koordinatak[0]}; {koordinatak[1]})", end="\t")

# 5.

partvonal_hossza = 0

for sor_index in range(0, sorok_szama):
    for oszlop_index in range(0, oszlopok_szama): # arra vagyunk kíváncsiak, hogy a jelenlegi helytől jobbra, balra, fel, le hány nulla van: a nullák számával növeljük a partvonalat
        adott_helyen = lista[sor_index][oszlop_index]

        if adott_helyen != 0: # ha van ott víz
            mellette_levok_koordinatai = [[sor_index - 1, oszlop_index], [sor_index + 1, oszlop_index], [sor_index, oszlop_index + 1], [sor_index, oszlop_index - 1]] # felette, alatta, jobbra, balra
            hanynulla = 0

            for koordinatak in mellette_levok_koordinatai:
                if koordinatak[0] == -1 or koordinatak[0] == sorok_szama: # ha nincs felette vagy alatta már sor, akkor automatikusan 0
                    hanynulla += 1
                elif koordinatak[1] == -1 or koordinatak[1] == oszlopok_szama: # ha előtte vagy utána nincs oszlop, akkor automatikusan 0
                    hanynulla += 1
                else: # minden más esetben létezik hely a koordinátán
                    mellette_hely = lista[koordinatak[0]][koordinatak[1]]

                    if mellette_hely == 0: # ha mellette szárazföld van, akkor
                        hanynulla += 1

            partvonal_hossza += hanynulla

print(f"\n5. feladat\nA tó partvonala {partvonal_hossza} m hosszú")

# 6.

beker_oszlop_indexe = int(input("6. feladat\nA vizsgált szelvény oszlopának azonosítója=")) - 1 # index miatt -1

oszlop_melysegei = []

for sor in lista:
    oszlop_melysegei.append(sor[beker_oszlop_indexe])

kiir = open("diagram.txt", "w", encoding="utf-8")

for sor_index in range(0, len(oszlop_melysegei)):
    melyseg = int(round(oszlop_melysegei[sor_index] / 10, 0))
    kiir.write(f"{(sor_index + 1):02d}{melyseg * '*'}\n")
