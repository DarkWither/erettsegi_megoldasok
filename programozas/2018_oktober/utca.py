# Ladányi Attila

# 1.

class Kerites:
    def __init__(self, oldal, szelesseg, szin, hazszam): # a házszámot nem tartalmazza a fájl, ezt külön adjuk meg neki!
        self.oldal = int(oldal)
        self.szelesseg = int(szelesseg)
        self.szin = szin
        self.hazszam = int(hazszam)

    def __repr__(self):
        return f"{self.oldal} {self.szelesseg} {self.szin} {self.hazszam}"

lista = []

fajl = open("kerites.txt", "r", encoding="utf-8")

paros_hazszam = 2 # az első páros házszám a kettő
paratlan_hazszam = 1

for sor in fajl:
    sor = sor.strip().split() # [oldal, szelesseg, szin]

    if sor[0] == "0": # akkor páros oldal; azért "0", mert stringként olvassa be a python
        lista.append(Kerites(*sor, paros_hazszam))
        paros_hazszam += 2 # += 2, mert 4 lesz a következő páros szám
    elif sor[0] == "1": # akkor páratlan oldal
        lista.append(Kerites(*sor, paratlan_hazszam))
        paratlan_hazszam += 2

# 2.

print(f"2. feladat\nAz eladott telkek száma: {len(lista)}")

# 3.

print("\n3. feladat")

if lista[-1].oldal == 0:
    print("A páros oldalon adták el az utolsó telket.")
elif lista[-1].oldal == 1:
    print("A páratlan oldalon adták el az utolsó telket.")

print(f"Az utolsó telek házszáma: {lista[-1].hazszam}")

# 4.

paratlan_maximum = 0 # melyik a legnagyobb házszám; azért kell, hogy utána lévőt ne vizsgálhassunk, mert nem létezik

for kerites in lista:
    if paratlan_maximum < kerites.hazszam and kerites.oldal == 1:
        paratlan_maximum = kerites.hazszam

egyezik = 0 # az egyező telek házszáma

for kerites in lista:
    if kerites.oldal == 1:
        mellette_levo = "" # megkeressük a mellette lévőt

        for telek in lista:
            if telek.hazszam + 2 <= paratlan_maximum:
                if telek.hazszam + 2 == kerites.hazszam:
                    mellette_levo = telek

        if mellette_levo != "": # van mellette telek
            if kerites.szin == mellette_levo.szin and kerites.szin not in [":", "#"]: # megegyezik a színe a mellette lévővel és van színe a kerítésnek
                egyezik = kerites.hazszam

print(f"\n4. feladat\nA szomszédossal egyezik a kerítés színe: {egyezik}")

# 5.

# a.

beker_hazszam = int(input("\n5. feladat\nAdjon meg egy házszámot! "))

bekert_kerites = 0

for kerites in lista:
    if kerites.hazszam == beker_hazszam:
        bekert_kerites = kerites

print(f"A kerítés színe / állapota: {bekert_kerites.szin}")

# b.

paros_maximum = 0

for kerites in lista:
    if paros_maximum < kerites.hazszam and kerites.oldal == 0:
        paros_maximum = kerites.hazszam

szinek = set()

for kerites in lista:
    if kerites.szin not in [":", "#"]:
        szinek.add(kerites.szin)

szinek = list(szinek) # listává alakítás, hogy elemekre lehessen hivatkozni

beker_kerites_mellettiek = [] # külön listába a mellette lévő kerítéseket

for kerites in lista:
    if kerites.hazszam - 2 == beker_hazszam or kerites.hazszam + 2 == beker_hazszam: # ha mellette van
        beker_kerites_mellettiek.append(kerites)

szinek.remove(bekert_kerites.szin) # kiszedjük a jelenlegi színt, mivel az nem lehetséges választás

for kerites in beker_kerites_mellettiek:
    szinek.remove(kerites.szin) # kiszedjük a szomszédok színét is

print(f"Egy lehetséges festési szín: {szinek[0]}") # mindegy, melyik elemét iratod ki, lényeg az, hogy biztosan létezzen az elem

# 6.

paratlan_oldal = [] # a páratlan oldal kerítései

for kerites in lista:
    if kerites.oldal == 1:
        paratlan_oldal.append(kerites)

felso_sor = "" # az "utcakep.txt" felső sora
also_sor = "" # -||- alsó sora

for kerites in paratlan_oldal:
    # először a felső sor:

    felso_sor += kerites.szin * kerites.szelesseg # annyiszor ismétli a színt, amennyi széles a kerités

    # alsó sor:

    # először a számot adjuk hozzá, majd (kerites.szelesseg - len(str(kerites.hazszam))) darab szóközt, hogy meglegyen a hossz

    also_sor += str(kerites.hazszam)
    also_sor += " " * (kerites.szelesseg - len(str(kerites.hazszam)))

kiir = open("utcakep.txt", "w", encoding="utf-8")

kiir.write(f"{felso_sor}\n{also_sor}")
