# Ladányi Attila

# 1.

beker_betu = input("1. feladat Adjon meg egy betűt: ").upper()

szamok_betukhoz = { # kulcs: a lenyomandó gomb, érték: azon betűk listája, melyeket ezzel a gombbal lehet beírni
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"]
}

def kod(szoveg):
    # a paraméter szövek kódját adja vissza, pl.: ablak --> 22525
    visszateresi_ertek = ""

    for betu in szoveg:
        for szam, betuk_lista in szamok_betukhoz.items():
            if betu in betuk_lista:
                visszateresi_ertek += szam

    return visszateresi_ertek

print(f"A betű kódja: {kod(beker_betu)}")

# 2.

beker_szo = input("2. feladat Adjon meg egy szót: ").upper()
print(f"A következő számsorral lehet bevinni a szót: {kod(beker_szo)}")

# 3.

fajl = open("szavak.txt", "r", encoding="utf-8")
lista = []

for sor in fajl:
    sor = sor.strip()
    lista.append(sor)

# 4.

leghosszabb_szo = ""

for szo in lista:
    if len(szo) > len(leghosszabb_szo):
        leghosszabb_szo = szo

print(f"4. feladat A leghosszabb szó: {leghosszabb_szo}; Hossza: {len(leghosszabb_szo)} karakter")

# 5.

rovid_szavak_szama = 0

for szo in lista:
    if len(szo) <= 5:
        rovid_szavak_szama += 1

print(f"5. feladat {rovid_szavak_szama} rövid szó van az állományban.")

# 6.

kiir = open("kodok.txt", "w", encoding="utf-8")

for szo in lista:
    kiir.write(f"{kod(szo.upper())}\n")

# 7.

beker_szamsor = input("7. feladat Adjon meg egy számsort: ")

szamsorokhoz_szavak = {} # kulcs: számsor, érték: a számsorhoz tartozó szavak szóközzel elválasztva

for szo in lista:
    szamsorokhoz_szavak[kod(szo.upper())] = szamsorokhoz_szavak.get(kod(szo.upper()), "") + f"{szo} "

jo_szavak = ""

for szamsor, szavak in szamsorokhoz_szavak.items():
    if szamsor == beker_szamsor:
        jo_szavak = szavak

print(f"Megfelelő szavak: {jo_szavak}")

# 8.

print("8. feladat Azonos kódhoz több szó: ")

for szamsor, szavak in szamsorokhoz_szavak.items():
    szavak = szavak.split()
    if len(szavak) > 1: # ha több szó van benne, akkor
        for szo in szavak:
            print(f"{szo} : {szamsor};", end=" ")

# 9.

legtobb_kod = ""
legtobb_szavak = []

for szamsor, szavak in szamsorokhoz_szavak.items():
    szavak = szavak.split()

    if len(szavak) > len(legtobb_szavak):
        legtobb_kod = szamsor
        legtobb_szavak = szavak

print(f"\n9. feladat A(z) {legtobb_kod} kódú szavakból van a legtöbb, mely szavak: {' '.join(legtobb_szavak)}")
