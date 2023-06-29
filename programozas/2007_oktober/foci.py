# Ladányi Attila

# 1.

class Meccsek:
    def __init__(self, fordulo, hazai_golok, vendeg_golok, hazai_felido_golok, vendeg_felido_golok, hazai_neve, vendeg_neve):
        self.fordulo = int(fordulo)
        self.hazai_golok = int(hazai_golok)
        self.vendeg_golok = int(vendeg_golok)
        self.hazai_felido_golok = int(hazai_felido_golok)
        self.vendeg_felido_golok = int(vendeg_felido_golok)
        self.hazai_neve = hazai_neve
        self.vendeg_neve = vendeg_neve

    def __repr__(self):
        return f"{self.fordulo} {self.hazai_golok} {self.vendeg_golok} {self.hazai_felido_golok} {self.vendeg_felido_golok} {self.hazai_neve} {self.vendeg_neve}"


fajl = open("meccs.txt", "r", encoding="utf-8")
lista = []

merkozesek_szama = int(fajl.readline().strip()) # első sor külön

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Meccsek(*sor))

# 2.

beker_fordulo = int(input("2. feladat\nKérem egy forduló számát: "))

print(f"A(z) {beker_fordulo}. forduló mérkőzései:")

for meccs in lista:
    if meccs.fordulo == beker_fordulo: # ha abban a fordulóban, akkor:
        print(f"{meccs.hazai_neve}-{meccs.vendeg_neve}: {meccs.hazai_golok}-{meccs.vendeg_golok} ({meccs.hazai_felido_golok}-{meccs.vendeg_felido_golok})")

# 3.

def gyoztes(hazainev, vendegnev, hazaigol, vendeggol):
    # visszatérési értéke a győztes neve vagy 'döntetlen'

    if hazaigol > vendeggol:
        return hazainev
    elif vendeggol > hazaigol:
        return vendegnev
    else:
        return "döntetlen"

sikerult_forditani = [] # kétdimenziós lista, elemek: [forduló, győztes_neve]

for meccs in lista:
    if gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_felido_golok, meccs.vendeg_felido_golok) != gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_golok, meccs.vendeg_golok):
        # ha a félidő győztese != a meccs győztesével
        if gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_golok, meccs.vendeg_golok) != "döntetlen" and gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_felido_golok, meccs.vendeg_felido_golok) != "döntetlen":
            # ha sem a végeredmény, sem a félidő eredménye nem 'döntetlen', akkor a győztes csapat fordított
            sikerult_forditani.append([meccs.fordulo, gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_golok, meccs.vendeg_golok)])

print("\n3. feladat\nFordulók sorszáma és csapatok neve, ahol a győztes félidő után fordított:")

for forditas in sikerult_forditani:
    print(f"{forditas[0]} {forditas[1]}") # forditas[0] == forduló, forditas[1] == győztes_neve

# 4.

beker_csapatnev = input("\n4. feladat\nAdja meg egy csapat nevét: ")

# 5.

lott = 0
kapott = 0

for meccs in lista:
    if meccs.hazai_neve == beker_csapatnev: # ha a hazai csapat, akkor:
        lott += meccs.hazai_golok
        kapott += meccs.vendeg_golok
    elif meccs.vendeg_neve == beker_csapatnev: # ha a vendég csapat, akkor:
        lott += meccs.vendeg_golok
        kapott += meccs.hazai_golok

print(f"\n5. feladat\nA bekért csapat góljai:\nlőtt: {lott} kapott: {kapott}")

# 6.

kikapott_otthon = [] # meccsek, ahol a bekért csapat otthon veszített

for meccs in lista:
    if meccs.hazai_neve == beker_csapatnev and gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_golok, meccs.vendeg_golok) == meccs.vendeg_neve:
        # a hazai csapat a bekért és a vendég nyert, akkor:
        kikapott_otthon.append(meccs)

print("\n6. feladat")

if len(kikapott_otthon) == 0:
    print("A csapat otthon veretlen maradt.")
else:
    fordulok_amikor_kikaptak = set()

    for meccs in kikapott_otthon:
        fordulok_amikor_kikaptak.add(meccs.fordulo)

    leghamarabbi_fordulo = min(fordulok_amikor_kikaptak)

    elso_akiktol_kikaptak = ""

    for meccs in kikapott_otthon:
        if meccs.fordulo == leghamarabbi_fordulo: # ha a leghamarabbi forduló, akkor:
            elso_akiktol_kikaptak = gyoztes(meccs.hazai_neve, meccs.vendeg_neve, meccs.hazai_golok, meccs.vendeg_golok)
            break # ha megvan az első ilyen név, akkor nem kell a többit vizsgálni

    print(f"A(z) {beker_csapatnev} először a(z) {leghamarabbi_fordulo}. fordulóban a(z) {elso_akiktol_kikaptak} csapattól kapott ki otthon.")

# 7.

def eredmeny(egyik, masik):
    # az eredményt mindig nagyobb-kisebb formában adja vissza

    if egyik > masik or egyik == masik:
        return f"{egyik}-{masik}"
    else:
        return f"{masik}-{egyik}"

eredmenyek = {} # kulcs: eredmény, érték: darabszám

for meccs in lista:
    eredmenyek[eredmeny(meccs.hazai_golok, meccs.vendeg_golok)] = eredmenyek.get(eredmeny(meccs.hazai_golok, meccs.vendeg_golok), 0) + 1

kiir = open("stat.txt", "w", encoding="utf-8")

for vege, darabszam in eredmenyek.items():
    kiir.write(f"{vege}: {darabszam} darab\n")
