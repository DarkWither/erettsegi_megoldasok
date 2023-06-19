# Ladányi Attila

import random

# 1.

valasztas = ["I", "F"] # a kettő közül az egyiket véletlenszerűen kiválasztjuk

print(f"1. feladat\nA pénzfeldobás eredménye: {random.choice(valasztas)}")

# 2.

tipp = input("2.feladat\nTippeljen! (F/I)= ")

erme_feldobas = random.choice(valasztas)

print(f"A tipp {tipp}, a dobás eredménye {erme_feldobas} volt.")

if tipp == erme_feldobas:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

# 3.

# MEGJEGYZÉS: a feladat megtiltja, hogy eltároljuk a "kiserlet.txt" fájl tartalmát, így a szokásos beolvasást
# mindegyik feladatnál meg kell csinálni, különben pontlevonás jár

dobasok_szama = 0

fajl = open("kiserlet.txt", "r", encoding="utf-8")

for dobas in fajl:
    dobas = dobas.strip()
    dobasok_szama += 1

print(f"3. feladat\nA kísérlet {dobasok_szama} dobásból állt.")

# 4. feladat

fejek_szama = 0

fajl = open("kiserlet.txt", "r", encoding="utf-8")

for dobas in fajl:
    dobas = dobas.strip()

    if dobas == "F":
        fejek_szama += 1

relativ_gyakorisag = round((fejek_szama / dobasok_szama) * 100, 2)

print(f"4. feladat\nA kísérlet során a fej relatív gyakorisága {relativ_gyakorisag}% volt.")

# 5. és 6.

# Következő feladatokat egyszerre oldjuk meg: készítünk egy olyan kétdimenziós listát, melyben az elemek tartalmazzák
# az egymás mellett lévő fejek helyét a fájlban, pl.: [[1, 2], [4, 5, 6]] --> "FFIFFF"

fejek_lista = []
seged_lista = []
sor_szama = 1

fajl = open("kiserlet.txt", "r", encoding="utf-8")

for dobas in fajl:
    dobas = dobas.strip()

    if dobas == "F":
        seged_lista.append(sor_szama)
    elif dobas == "I" and seged_lista != []: # üres listák esetén ne történjen semmi, ne legyen tele velük a lista
        fejek_lista.append(seged_lista)
        seged_lista = []

    sor_szama += 1

csak_ketto_fej = 0

for fejek in fejek_lista:
    if len(fejek) == 2:
        csak_ketto_fej += 1

print(f"5. feladat\nA kísérlet során {csak_ketto_fej} alkalommal dobtak pontosan két fejet egymás után.")

leghosszabb_erteke = 0
leghosszabb_kezdes = 0

for fejek in fejek_lista:
    if len(fejek) > leghosszabb_erteke:
        leghosszabb_erteke = len(fejek)
        leghosszabb_kezdes = fejek[0] # az első elem lesz a sorozat kezdete

print(f"6. feladat\nA leghosszabb tisztafej sorozat {leghosszabb_erteke} tagból áll, kezdete a(z) {leghosszabb_kezdes}. dobás.")

# 7.

negy_dobasok = []

for index in range(1000): # ciklusváltozó jelentéktelen, csak ezerszer ismétlődjön
    egy_dobas = "" # egy négyes dobás

    for j in range(4): # ciklusváltozó jelentéktelen, csak négyszer ismétlődjön
        egy_dobas += random.choice(valasztas)

    negy_dobasok.append(egy_dobas)

negy_fej = 0 # "FFFF"
harom_fej = 0 # "FFFI"

for dobas in negy_dobasok:
    if dobas == "FFFF":
        negy_fej += 1
    elif dobas == "FFFI":
        harom_fej += 1

kiir = open("dobasok.txt", "w", encoding="utf-8")

kiir.write(f"FFFF: {negy_fej}, FFFI: {harom_fej}\n")

kiir.write(' '.join(negy_dobasok))
