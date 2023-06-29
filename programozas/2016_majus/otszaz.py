# Ladányi Attila

# 1.

fajl = open("penztar.txt", "r", encoding="utf-8")

lista = []
seged = []

for sor in fajl:
    sor = sor.strip()

    if sor == "F":
        lista.append(seged)
        seged = []
    else:
        seged.append(sor)

# 2.

print(f"2. feladat\nA fizetések száma: {len(lista)}")

# 3.

print(f"\n3. feladat\nAz első vásárló {len(lista[0])} darab árucikket vásárolt.")

# 4.

beker_sorszam = int(input("\n4. feladat\nAdja meg egy vásárlás sorszámát! "))
beker_arucikk = input("Adja meg egy árucikk nevét! ")
beker_darabszam = int(input("Adja meg a vásárolt darabszámot! "))

# 5.

vettek_arucikket = [] # mikor vettek olyan árucikket
sorszam = 1

for vasarlas in lista:
    if beker_arucikk in vasarlas:
        vettek_arucikket.append(sorszam)

    sorszam += 1

print(f"\n5. feladat\nAz első vásárlás sorszáma: {vettek_arucikket[0]}")
print(f"Az utolsó vásárlás sorszáma: {vettek_arucikket[-1]}")
print(f"{len(vettek_arucikket)} vásárlás során vettek belőle.")

# 6.

def ertek(darabszam):
    fizetendo = 0

    if darabszam == 1:
        fizetendo = 500
    elif darabszam == 2:
        fizetendo = 500 + 450
    elif darabszam > 2:
        fizetendo = 500 + 450 + 400 * (darabszam - 2)

    return fizetendo

print(f"\n6. feladat\n{beker_darabszam} darab vételekor fizetendő: {ertek(beker_darabszam)}")

# 7.

beker_vasarlas = lista[beker_sorszam - 1]

mibol_mennyi = {} # kulcs: termék neve, érték: darabszám

for arucikk in beker_vasarlas:
    mibol_mennyi[arucikk] = mibol_mennyi.get(arucikk, 0) + 1

print("\n7. feladat")

for arucikk, darabszam in mibol_mennyi.items():
    print(f"{darabszam} {arucikk}")

# 8.

kiir = open("osszeg.txt", "w", encoding="utf-8")

sorszam = 1

for vasarlas in lista:
    osszeg = 0 # mennyit kell fizetni

    mibol_mennyi = {}

    for arucikk in vasarlas:
        mibol_mennyi[arucikk] = mibol_mennyi.get(arucikk, 0) + 1

    for darabszam in mibol_mennyi.values():
        osszeg += ertek(darabszam)

    kiir.write(f"{sorszam}: {osszeg}\n")

    sorszam += 1
