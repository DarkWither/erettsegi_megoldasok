# Ladányi Attila

# 1.

beker_szo = input("1. feladat Adjon meg egy szót: ")

van_benne_maganhangzo = False

for betu in beker_szo:
    if betu in "aeiou":
        van_benne_maganhangzo = True

if van_benne_maganhangzo:
    print("Van benne magánhangzó.")
else:
    print("Nincs benne magánhangzó.")

# 2.

# Beolvasás

lista = []

fajl = open("szoveg.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip()

    lista.append(sor)

# Leghosszabb szó

leghosszabb = lista[0]

for szo in lista:
    if len(leghosszabb) < len(szo):
        leghosszabb = szo

print(f"2. feladat Leghosszabb szó: {leghosszabb}")

# 3.

def hany_maganhangzo(szo):
    # hány mgh van a szóban
    darab = 0

    for betu in szo:
        if betu in "aeiou":
            darab += 1

    return darab

tobb_maganhangzo = 0

for szo in lista:
    if hany_maganhangzo(szo) > (len(szo) - hany_maganhangzo(szo)): # len(szo) - hany_maganhangzo(szo) == egyéb karakterek
        tobb_maganhangzo += 1

print(f"3. feladat {tobb_maganhangzo} szóban van több magánhangzó, mint más karakter.")
print(f"Összesen {len(lista)} szó van az állományban.")
print("A talált szavak százaléka:")
print(f"{tobb_maganhangzo}/{len(lista)} : {round((tobb_maganhangzo / len(lista)) * 100, 2)}%")

# 4.

otkarakteres = []

for szo in lista:
    if len(szo) == 5:
        otkarakteres.append(szo)

beker_szoreszlet = input("4. feladat Adjon meg egy 3 karakteres szórészletet: ")

hozza_tartozo = []

for szo in otkarakteres:
    if beker_szoreszlet == szo[1:4]: # szo[1:4] == körte --> ört
        hozza_tartozo.append(szo)

print(f"Felhasználható szavak:\n{' '.join(hozza_tartozo)}")

# 5.

szotar = {} # kulcs: közepe a szónak, érték: szavak egymás alatt

for szo in otkarakteres:
    szotar[szo[1:4]] = szotar.get(szo[1:4], "") + szo + "\n"

kiir = open("letra.txt", "w", encoding="utf-8")

for kozep, szavak in szotar.items():
    if len(szavak) > 7: # a szó öt karakter, a "\n" pedig kettő, ezért 7
        kiir.write(f"{szavak}\n")
