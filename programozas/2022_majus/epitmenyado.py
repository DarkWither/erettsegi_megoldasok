# Ladányi Attila

# 1. feladat

class Telek:
    def __init__(self, adoszam, utcanev, hazszam, adosav, alapterulet):
        self.adoszam = int(adoszam)
        self.utcanev = utcanev
        self.hazszam = hazszam
        self.adosav = adosav
        self.alapterulet = int(alapterulet)

    def __repr__(self):
        return f"{self.adoszam} {self.utcanev} {self.hazszam} {self.adosav} {self.alapterulet}"

fajl = open("utca.txt", "r", encoding="utf-8")
lista = []

elso_sor = fajl.readline().strip().split()
a_sav = int(elso_sor[0])
b_sav = int(elso_sor[1])
c_sav = int(elso_sor[2])

for sor in fajl:
    sor = sor.strip().split()
    lista.append(Telek(*sor))

# 2. feladat

print(f"2. feladat. A mintában {len(lista)} telek szerepel.")

# 3. feladat

beker_adoszam = int(input("3. feladat. Egy tulajdonos adószáma: "))

beker_telkek = [] # melyik telkek tartoznak a bekért adószámhoz

for telek in lista:
    if telek.adoszam == beker_adoszam:
        beker_telkek.append(telek)

if len(beker_telkek) == 0: # ha üres lista, akkor nincs ilyen adószám
    print("Nem szerepel az adatállományban.")
else:
    for telek in beker_telkek:
        print(f"{telek.utcanev} utca {telek.hazszam}")

# 4. feladat

def ado(adosav, alapterulet):
    fizetendo = 0

    if adosav == "A":
        fizetendo = a_sav * alapterulet
    elif adosav == "B":
        fizetendo = b_sav * alapterulet
    elif adosav == "C":
        fizetendo = c_sav * alapterulet

    if fizetendo > 10000:
        return fizetendo
    else:
        return 0 # ha nincs 10000ft az adó, akkor nem kell fizetni a telek után

# 5. feladat

hany_telek = {} # kulcs: adósáv, érték: telkek száma

for telek in lista:
    hany_telek[telek.adosav] = hany_telek.get(telek.adosav, 0) + 1

mennyi_ado = {} # kulcs: adósáv, érték: összes adó

for telek in lista:
    mennyi_ado[telek.adosav] = mennyi_ado.get(telek.adosav, 0) + ado(telek.adosav, telek.alapterulet)

print("5. feladat")

for sav_betu in "ABC":
    print(f"{sav_betu} sávba {hany_telek[sav_betu]} telek esik, az adó {mennyi_ado[sav_betu]} Ft.")

# 6. feladat

utcak_savok = {} # kulcs: utcanév, érték: adósávok

for telek in lista:
    utcak_savok[telek.utcanev] = utcak_savok.get(telek.utcanev, "") + telek.adosav + " "

tobb_sav = [] # több sávba sorolt utcák nevei

for utcanev, adosavok in utcak_savok.items():
    alakitas = set(adosavok.split()) # halmazzá alakítás, minden betű egyszer szerepel maximum

    if len(alakitas) > 1: # ha több, mint egy betű
        tobb_sav.append(utcanev)

print("6. feladat. A több sávba sorolt utcák:")

for utcanev in tobb_sav:
    print(utcanev)

# 7. feladat

ado_tulajdonosonkent = {} # kulcs: adószám, érték: fizetendő adó

for telek in lista:
    ado_tulajdonosonkent[telek.adoszam] = ado_tulajdonosonkent.get(telek.adoszam, 0) + ado(telek.adosav, telek.alapterulet)

iras = open("fizetendo.txt", "w", encoding="utf-8")

for adoszam, fizetendo in ado_tulajdonosonkent.items():
    iras.write(f"{adoszam} {fizetendo}\n")
