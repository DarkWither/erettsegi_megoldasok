# Ladányi Attila

# 1.

class Athaladasok:
    def __init__(self, ora, perc, masodperc, megtetelhez_szukseges_ido, melyik_iranybol):
        self.ora = int(ora)
        self.perc = int(perc)
        self.masodperc = int(masodperc)
        self.megtetelhez_szukseges_ido = int(megtetelhez_szukseges_ido)
        self.melyik_iranybol = melyik_iranybol

        self.ido_masodpercekben = self.ora * 3600 + self.perc * 60 + self.masodperc

        self.athaladas_vege = self.ido_masodpercekben + self.megtetelhez_szukseges_ido # vége = kezdet + áthaladás_ideje

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.masodperc} {self.megtetelhez_szukseges_ido} {self.melyik_iranybol}"

    def sebesseg(self):
        # visszatérési értéke a jármű sebessége
        # az adott szakasz 1000 méter, melyet a jármű self.megtetelhez_szukseges_ido másodperc alatt tesz meg
        # a jármű sebessége pedig a kettő hányadosa (sebesseg = ut / ido)

        return round(1000 / self.megtetelhez_szukseges_ido, 1) # 1 tizedesjegyre kerekítve

lista = []

fajl = open("forgalom.txt", "r", encoding="utf-8")

athalado_jarmuvek_szama = int(fajl.readline().strip()) # az első sor beolvasása

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Athaladasok(*sor))

# 2.

n_dik_sorszam = int(input("2. feladat Adja meg a jármű sorszámát! "))

n_dik_athaladas = lista[n_dik_sorszam - 1] # index miatt -1

if n_dik_athaladas.melyik_iranybol == "A": # ha A felől jön, akkor F felé halad
    print("A jármű 'F' város felé haladt.")
elif n_dik_athaladas.melyik_iranybol == "F":
    print("A jármű 'A' város felé haladt.")

# 3.

f_varos_fele = [] # F város felé tartó járművek, azaz A felől jövők

for athaladas in lista:
    if athaladas.melyik_iranybol == "A":
        f_varos_fele.append(athaladas)

kulonbseg = f_varos_fele[-1].ido_masodpercekben - f_varos_fele[-2].ido_masodpercekben

print(f"3. feladat A két utolsó 'F' város felé tartó jármű {kulonbseg} másodperc különbséggel érte el a szakaszt.")

# 4.

also_felol = {} # kulcs: óra, érték: áthaladt járművek száma
felso_felol = {} # ua.

for athaladas in lista:
    if athaladas.melyik_iranybol == "A":
        also_felol[athaladas.ora] = also_felol.get(athaladas.ora, 0) + 1
    elif athaladas.melyik_iranybol == "F":
        felso_felol[athaladas.ora] = felso_felol.get(athaladas.ora, 0) + 1

print("4. feladat Áthaladó járművek óránként:")

for ora in sorted(also_felol.keys()): # sorted() azért, hogy időrendben jelenjenek meg (nem kérte a feladat, csak esztétikailag így néz ki jól :D)
    print(f"Óra: {ora} A: {also_felol[ora]} F: {felso_felol[ora]}")

# 5.

sebesseg_alapjan_rendezve = sorted(lista, key = lambda athaladas: athaladas.sebesseg(), reverse=True) # minden elemhez hozzárendelem a sebességét és az alapján rakom csökkenő sorrendbe

print("5. feladat A tíz leggyorsabb jármű:")

for index in range(0, 10): # 0-9-ig az indexekhez tartozó elemeket kiíratom
    athaladas = sebesseg_alapjan_rendezve[index]

    if athaladas.melyik_iranybol == "A":
        print(f"{athaladas.ora} {athaladas.perc} {athaladas.masodperc} Alsó {athaladas.sebesseg()} m/s") # a mértékegységet nem kell szerintem odaírni, bár ez minta hiányában nem megállapítható, illetve nem írja a feladat sem
    elif athaladas.melyik_iranybol == "F":
        print(f"{athaladas.ora} {athaladas.perc} {athaladas.masodperc} Felső {athaladas.sebesseg()} m/s") # a feladatmegoldásban szerepel a mértékegység is, így odaírom

# 6.

def masodpercbol_formatumba(masodperc):
    # masodperc --> [ora, perc, masodperc]
    ora = masodperc // 3600
    masodperc -= ora * 3600
    perc = masodperc // 60
    masodperc -= perc * 60

    return [str(ora), str(perc), str(masodperc)] # str() majd a .join() miatt


a_varos_fele = [] # A felé (azaz F felől érkező) haladó járművek

for athaladas in lista:
    if athaladas.melyik_iranybol == "F":
        a_varos_fele.append(athaladas)

athaladasok_vegei = [] # másodpercben mikor lett vége az áthaladásnak

for athaladas in a_varos_fele:
    athaladasok_vegei.append(athaladas.athaladas_vege)

# végigmegyünk az összes időn, ha utólér egy járművet, akkor az előtte lévő idő nagyobb lesz, mint a jelenlegi
# ekkor megnézzük a nagyobb időt, és az lesz a jelenlegi is, mivel a nagyobb lesz a lassabb

for index in range(0, len(athaladasok_vegei)):
    jelenlegi_ido = athaladasok_vegei[index] # amit most vizsgálunk

    for masik_index in range(0, index): # végigmegyünk a jelenlegi elemig
        elotte_levo = athaladasok_vegei[masik_index]

        if jelenlegi_ido < elotte_levo: # az előtte lévő lassabb, akkor
            jelenlegi_ido = elotte_levo

    athaladasok_vegei[index] = jelenlegi_ido # a jelenlegi értékét módosítom a listában is

kiir = open("also.txt", "w", encoding="utf-8")

for idopontok in athaladasok_vegei:
    kiir.write(f"{' '.join(masodpercbol_formatumba(idopontok))}\n")
