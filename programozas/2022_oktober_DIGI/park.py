# Ladányi Attila

# 1. feladat

class Felajanlas:
    def __init__(self, elso_sorszam, utolso_sorszam, szin):
        self.elso_sorszam = int(elso_sorszam)
        self.utolso_sorszam = int(utolso_sorszam)
        self.szin = szin

    def __repr__(self):
        return f"{self.elso_sorszam} {self.utolso_sorszam} {self.szin}"

lista = []

fajl = open("felajanlas.txt", "r", encoding="utf-8")

felajanlasok = int(fajl.readline().strip()) # első sort külön be kell olvasni

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Felajanlas(*sor))

# 2. feladat

print(f"2. feladat\nA felajánlások száma: {felajanlasok}\n")

# 3. feladat

mindket_oldalon = [] # a bejárat minkét oldalát melyik felajánlások akarják beültetni
sorszam = 1 # külön változóval nézzük a sorszámot

for felajanlas in lista:
    if felajanlas.elso_sorszam > felajanlas.utolso_sorszam: # ha az első szám nagyobb, mint az utolsó, akkor ülteti be mindkét oldalt, lásd feladatleírás
        mindket_oldalon.append(str(sorszam)) # str() a kiírásban a .join() miatt, mert csak stringekkel működik

    sorszam += 1

print(f"3. feladat\nA bejárat mindkét oldalán ültetők: {' '.join(mindket_oldalon)}")

# 4. feladat

agyas = int(input("\n4. feladat\nAdja meg az ágyás sorszámát! "))

hany_felajanlasban = 0 # darabszám
viragagyas_szinek = [] # felajánlott színek

for felajanlas in lista:
    # két eset: vagy beületeti mindkét oldalát a bejáratnak, vagy nem
    if felajanlas.elso_sorszam > felajanlas.utolso_sorszam:
        if felajanlas.elso_sorszam <= agyas or felajanlas.utolso_sorszam >= agyas: # ha mindkét oldalon ültet, akkor elég az "or"
            viragagyas_szinek.append(felajanlas.szin)
            hany_felajanlasban += 1
    elif felajanlas.elso_sorszam <= agyas and felajanlas.utolso_sorszam >= agyas: # ha nem, kell az "and"
        viragagyas_szinek.append(felajanlas.szin)
        hany_felajanlasban += 1

print(f"A felajánlók száma: {hany_felajanlasban}")

if len(viragagyas_szinek) == 0: # ha nincs felajánlott szín, akkor értelemszerűen felajánlás sincs
    print("Ezt az ágyást nem ültetik be.")
else:
    print(f"A virágágyás színe, ha csak az első ültet: {viragagyas_szinek[0]}") # legelső szín a lista első eleme
    print(f"A virágágyás színei: {' '.join(set(viragagyas_szinek))}") # set(), hogy minden szín egyszer szerepeljen

# 5. feladat

mindegyikre = True # mindegyik ágyásra érkezett-e felajánlás

for agyasok in range(1, felajanlasok + 1):
    van = False # adott ágyásban (ciklusváltozó) van-e felajánlás

    for felajanlas in lista:
        if felajanlas.elso_sorszam > felajanlas.utolso_sorszam:
            if felajanlas.elso_sorszam <= agyasok or felajanlas.utolso_sorszam >= agyasok:
                van = True
        elif felajanlas.elso_sorszam <= agyasok and felajanlas.utolso_sorszam >= agyasok:
            van = True

    if not van: # ha nincs felajánlás akár már egyszer, akkor nem mindegyikre érkezett felajánlás
        mindegyikre = False
        break

print("\n5. feladat")

if not mindegyikre:
    osszes_agyas = 0 # hány ágyást akarnak beültetni összesen

    for felajanlas in lista:
        if felajanlas.elso_sorszam > felajanlas.utolso_sorszam:
            osszes_agyas += (felajanlasok - felajanlas.elso_sorszam) + 1 + felajanlas.utolso_sorszam # elsőtől a végéig + 1 és + felajánlás utolsó, hogy a jobb oldalon mennyi van beültetve
        else:
            osszes_agyas += (felajanlas.utolso_sorszam - felajanlas.elso_sorszam) + 1

    if osszes_agyas >= felajanlasok: # ha van elég felajánlás, akkor
        print("Átszervezéssel megoldható a beültetés.")
    else: # ha nincs:
        print("A beültetés nem oldható meg.")

else:
    print("Minden ágyás beültetésére van jelentkező.")

# 6. feladat

iras = open("szinek.txt", "w", encoding="utf-8")

for agyas_sorszam in range(1, felajanlasok + 1):
    szinek = [] # milyen színek érkeztek
    sorszam = 1 # viszgált felajánló sorszáma
    felajanlo = 0 # ki volt az első felajánló

    for felajanlas in lista:
        if felajanlas.elso_sorszam > felajanlas.utolso_sorszam:
            if felajanlas.elso_sorszam <= agyas_sorszam or felajanlas.utolso_sorszam >= agyas_sorszam:
                szinek.append(felajanlas.szin)
                if felajanlo == 0: # ha még nincs felajánló, akkor
                    felajanlo = sorszam

        elif felajanlas.elso_sorszam <= agyas_sorszam and felajanlas.utolso_sorszam >= agyas_sorszam:
            szinek.append(felajanlas.szin)
            if felajanlo == 0:
                felajanlo = sorszam

        sorszam += 1

    if felajanlo == 0: # ha nem talált felajánlót, akkor üres
        iras.write("# 0\n")
    else: # talált felajánlót, akkor az első szín és a felajanlo kerül a fájlba
        iras.write(f"{szinek[0]} {felajanlo}\n")
