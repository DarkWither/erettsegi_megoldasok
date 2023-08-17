# Ladányi Attila

# 1.

nyilt_szoveg = input("1. feladat Adjon meg egy szöveget: ")

# 2.

mit_mire = {  # mit mire kell átalakítani
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ö": "o",
    "ő": "o",
    "ú": "u",
    "ü": "u",
    "ű": "u"
}

for mit, mire in mit_mire.items():
    nyilt_szoveg = nyilt_szoveg.replace(mit, mire)

for mit in [" ", ",", ":", ".", ";", "?", "-", "_", "!"]: # kiszedjük az írásjeleket is
    nyilt_szoveg = nyilt_szoveg.replace(mit, "")

nyilt_szoveg = nyilt_szoveg.upper()

# 3.

print(f"3. feladat Átalakított nyílt szöveg: {nyilt_szoveg}")

# 4.

beker_kulcsszo = input("4. feladat Adjon meg egy kulcsszót: ").upper()

# 5.

kulcsszoveg = ""

while len(kulcsszoveg) != len(nyilt_szoveg):
    for betu in beker_kulcsszo:
        if len(kulcsszoveg) == len(nyilt_szoveg): # ha elérjük a szó közepén, akkor ciklustörés
            break
        else:
            kulcsszoveg += betu

print(f"5. feladat Kulcszöveg: {kulcsszoveg}")

# 6.

lista = []
fajl = open("vtabla.dat", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip()
    lista.append(sor)

kodolt_szoveg = ""

for index in range(0, len(nyilt_szoveg)):
    nyilt_szoveg_karaktere = nyilt_szoveg[index]
    kulcsszoveg_karaktere = kulcsszoveg[index]

    melyik_oszlop_kell = 0 # hanyadik sorban van az első oszlopban

    elso_oszlop_betui = []

    for sor in lista:
        elso_oszlop_betui.append(sor[0])

    for oszlop_index in range(0, len(elso_oszlop_betui)):
        if elso_oszlop_betui[oszlop_index] == nyilt_szoveg_karaktere:
            melyik_oszlop_kell = oszlop_index

    melyik_sor_kell = 0

    for sor_index in range(0, len(lista[0])): # az első sorban keressük
        if lista[0][sor_index] == kulcsszoveg_karaktere:
            melyik_sor_kell = sor_index

    kodolt_szoveg += lista[melyik_sor_kell][melyik_oszlop_kell]

# 7.

print(f"7. feladat Kódolt szöveg: {kodolt_szoveg}")

kiir = open("kodolt.dat", "w", encoding="utf-8")
kiir.write(f"{kodolt_szoveg}")
