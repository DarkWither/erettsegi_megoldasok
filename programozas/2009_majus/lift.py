# Ladányi Attila

# 1.

import random


class Igeny:
    def __init__(self, ora, perc, masodperc, csapat, induloszint, celszint):
        self.ora = int(ora)
        self.perc = int(perc)
        self.masodperc = int(masodperc)
        self.csapat = int(csapat)
        self.induloszint = int(induloszint)
        self.celszint = int(celszint)

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.masodperc} {self.csapat} {self.induloszint} {self.celszint}"

    def formatum(self): # utolsó feladathoz könnyítésképpen
        return f"{self.ora}:{self.perc}:{self.masodperc}"


lista = []
fajl = open("igeny.txt", "r", encoding="utf-8")

szintek_szama = int(fajl.readline().strip())
csapatok_szama = int(fajl.readline().strip())
igenyek_szama = int(fajl.readline().strip())

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Igeny(*sor))

# 2.

beker_szint = int(input("2. feladat\nAdja meg, melyik szinten áll a lift! "))

# 3.

utolso_keres = lista[-1]

print(f"3. feladat\nA lift a {utolso_keres.celszint}. szinten áll az utolsó igény teljesítése után.")

# 4.

erintett_szintek = [beker_szint] # a szintek, amelyeken volt a lift; a kiindulási szint alapból eleme

for igeny in lista:
    erintett_szintek.append(igeny.induloszint)
    erintett_szintek.append(igeny.celszint)

print(f"4. feladat\nLegalacsonyabb sorszámú szint: {min(erintett_szintek)}.\nLegmagasabb sorszámú szint: {max(erintett_szintek)}.")

# 5.

utassal_felfele = 0 # akkor megy fel, amikor az igénynél az induloszint < celszint

for igeny in lista:
    if igeny.induloszint < igeny.celszint:
        utassal_felfele += 1

utas_nelkul_felfele = 0 # akkor, amikor a jelenlegi igény indulása nagyobb, mint az előtte lévő igény celszint-je

if lista[0].induloszint > beker_szint: # ha a kezdetnél nagyobb az első igény indulása, akkor utas nélkül felfelé megy
    utas_nelkul_felfele += 1

for index in range(1, len(lista)): # azért egytől, mert 0 előtt nincs másik igény
    jelenlegi_igeny = lista[index]
    elotte_levo_igeny = lista[index - 1]

    if jelenlegi_igeny.induloszint > elotte_levo_igeny.celszint:
        utas_nelkul_felfele += 1

print(f"5. feladat\nUtassal felfelé: {utassal_felfele} db igény\nUtas nélkül felfelé: {utas_nelkul_felfele} db igény")

# 6.

# Megoldás fordítottan: az összes csapat sorszámából kiszedjük azokat, akik igénybe vették a liftet, így a maradék nem vette igénybe

osszes_csapat_sorszama = [str(szam) for szam in range(1, csapatok_szama + 1)] # str() a .join miatt

for igeny in lista:
    if str(igeny.csapat) in osszes_csapat_sorszama: # azért kell, mivel olyan elemet, ami nincs a listában, a .remove() nem tud kiszedni
        osszes_csapat_sorszama.remove(str(igeny.csapat))

print(f"6. feladat\nCsapatok, akik nem használták a liftet: {' '.join(osszes_csapat_sorszama)}")

# 7.

veletlen_csapatszam = random.randint(1, csapatok_szama)

csapathoz_tartozo_igenyek = [] # külön listába azokat az igényeket, amelyeknél a csapat sorszáma a véletlen sorszám

for igeny in lista:
    if igeny.csapat == veletlen_csapatszam:
        csapathoz_tartozo_igenyek.append(igeny)

szabalytalansagok = [] # kétdimenziós lista, elemei azok a szintek, melyek közötti távolságot gyalog tették meg, így: [[innen, ide], [innen, ide], ...]

for index in range(1, len(csapathoz_tartozo_igenyek)):
    jelenlegi_igeny = csapathoz_tartozo_igenyek[index]
    elotte_levo_igeny = csapathoz_tartozo_igenyek[index - 1]

    if jelenlegi_igeny.induloszint != elotte_levo_igeny.celszint: # ha nem onnan indulnak, ahova az előtte lévőnél érkeztek, akkor gyalogoltak, tehát szabályszegés
        szabalytalansagok.append([elotte_levo_igeny.celszint, jelenlegi_igeny.induloszint])

print("7. feladat")

if len(szabalytalansagok) == 0:
    print("Nem bizonyítható szabálytalanság")
else:
    print(f"Ezen két szint közötti utat tette meg a(z) {veletlen_csapatszam}. csapat gyalog: ")

    for szintek in szabalytalansagok:
        print(f"{szintek[0]}. és {szintek[1]}.")

# 8.

kiir = open("blokkol.txt", "w", encoding="utf-8")

print("8. feladat")

for igeny in csapathoz_tartozo_igenyek:
    beker_befejezett = input(f"Befejezés ideje: {igeny.formatum()}\nSikeresség: ")
    print(f"-----\nIndulási emelet: {igeny.induloszint}\nCélemelet: {igeny.celszint}")
    beker_feladatkod = input("Feladatkód: ")
    kiir.write(f"Befejezés ideje: {igeny.formatum()}\nSikeresség: {beker_befejezett}\n-----\nIndulási emelet: {igeny.induloszint}\nCélemelet: {igeny.celszint}\nFeladatkód: {beker_feladatkod}\n")
