# Ladányi Attila

# 1.

class Felosztas:
    def __init__(self, nev, targy, osztaly, heti_oraszam):
        self.nev = nev
        self.targy = targy
        self.osztaly = osztaly
        self.heti_oraszam = int(heti_oraszam)

    def __repr__(self):
        return f"{self.nev} {self.targy} {self.osztaly} {self.heti_oraszam}"

lista = []
fajl = open("beosztas.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip() # a nevet tartalmazza
    sor_ketto = fajl.readline().strip() # tantárgy
    sor_harom = fajl.readline().strip() # osztály
    sor_negy = fajl.readline().strip() # heti óraszám

    lista.append(Felosztas(sor, sor_ketto, sor_harom, sor_negy))

# 2.

print(f"2. feladat\nA fájlban {len(lista)} bejegyzés van.")

# 3.

heti_osszoraszam = 0

for felosztas in lista:
    heti_osszoraszam += felosztas.heti_oraszam

print(f"3. feladat\nAz iskolában a heti összóraszám: {heti_osszoraszam}")

# 4.

beker_tanar_neve = input("4. feladat\nEgy tanár neve= ")

heti_orak = 0

for felosztas in lista:
    if felosztas.nev == beker_tanar_neve:
        heti_orak += felosztas.heti_oraszam

print(f"A tanár heti óraszáma: {heti_orak}")

# 5.

szotar = {} # kulcs: osztály, érték: of. neve

for felosztas in lista:
    if felosztas.targy == "osztalyfonoki":
        szotar[felosztas.osztaly] = szotar.get(felosztas.osztaly, "") + felosztas.nev

kiir = open("of.txt", "w", encoding="utf-8")

for osztaly, nev in szotar.items():
    kiir.write(f"{osztaly} - {nev}\n")

# 6.

beker_osztaly = input("6. feladat\nOsztály= ")
beker_tantargy = input("Tantárgy= ")

beker_felosztasok = [] # azok a felosztások, amelyek osztálya és tantárgya a bekért értékek

for felosztas in lista:
    if felosztas.osztaly == beker_osztaly and felosztas.targy == beker_tantargy:
        beker_felosztasok.append(felosztas)

if len(beker_felosztasok) == 1:
    print("Osztályszinten tanulják.")
else:
    print("Csoportbontásban tanulják.")

# 7.

tanarok_neve = set()

for felosztas in lista:
    tanarok_neve.add(felosztas.nev)

print(f"Az iskolában {len(tanarok_neve)} tanár tanít.")
