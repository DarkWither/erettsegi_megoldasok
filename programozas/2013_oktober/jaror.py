# Ladányi Attila

# 1.

class Athaladas:
    def __init__(self, ora, perc, masodperc, rendszam):
        self.ora = int(ora)
        self.perc = int(perc)
        self.masodperc = int(masodperc)
        self.rendszam = rendszam

        self.masodpercekben = self.ora * 3600 + self.perc * 60 + self.masodperc # hogy tudjunk az idővel számolni

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.masodperc} {self.rendszam}"

lista = []

fajl = open("jarmu.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip().split()

    lista.append(Athaladas(*sor))

# 2.

orak = set() # az összes órát belerakjuk

for athaladas in lista:
    orak.add(athaladas.ora)

hany_orat_dolgoztak = (max(orak) + 1) - min(orak) # +1 azért, mert ha mondjuk 12 a legnagyobb óra, akkor 13-ig dolgoztak

print(f"2. feladat Az ellenőrzést végzők {hany_orat_dolgoztak} órát dolgoztak.")

# 3.

elso_athaladok = {} # kulcs: elhaladás órája, érték: rendszám

for athaladas in lista:
    if athaladas.ora not in elso_athaladok.keys(): # ha a szótár kulcsai között nincs még ilyen óra, akkor megtaláltuk az elsőt, tehát
        elso_athaladok[athaladas.ora] = athaladas.rendszam

# kiírásnál növekvő sorrendbe legyenek az órák, mert így szebb (nem kötelező elem, egy sima for ... in elso_athaladok.items() is megfelel)

print("3. feladat Kiválasztott járművek:")

for ora in sorted(elso_athaladok.keys()):
    print(f"{ora} óra: {elso_athaladok[ora]}")

# 4.

jarmuvekbol_mennyi = {} # kulcs: jármű típusa, érték: darabszám

for athaladas in lista:
    elso_betu = athaladas.rendszam[0] # az első betűt külön változóba, nem szükséges, de kevesebbet kell gépelni utána

    if elso_betu == "B":
        jarmuvekbol_mennyi["autóbusz"] = jarmuvekbol_mennyi.get("autóbusz", 0) + 1
    elif elso_betu == "K":
        jarmuvekbol_mennyi["kamion"] = jarmuvekbol_mennyi.get("kamion", 0) + 1
    elif elso_betu == "M":
        jarmuvekbol_mennyi["motor"] = jarmuvekbol_mennyi.get("motor", 0) + 1
    else:
        jarmuvekbol_mennyi["személygépkocsi"] = jarmuvekbol_mennyi.get("személygépkocsi", 0) + 1

print("4. feladat Járművek száma típusonként:")

for tipus, darabszam in jarmuvekbol_mennyi.items():
    print(f"{tipus}: {darabszam} darab")

# 5.

# forgalommentes időszaknak két elhaladás közötti időszakot vesszük
# azaz melyik a leghosszabb időszak két elhaladás között

leghosszabb_idoszak_kezdet = 0 # leghosszabb időszak kezdete másodpercben
leghosszabb_idoszak_vege = 0 # leghosszabb időszak vége másodpercben
leghosszabb_idoszak_hossza = 0 # leghosszabb időszak hossza másodpercben

for index in range(1, len(lista)): # azért indul 1-ről és nem 0-ról, mert mindig a jelenlegiből vonjuk ki az előttit, és az első elem előtt már nincs másik, szóval az kimarad
    jelenlegi = lista[index]
    elotte_levo = lista[index - 1]

    kulonbseg = jelenlegi.masodpercekben - elotte_levo.masodpercekben # a köztük eltelt idő a kettő különbsége

    if kulonbseg > leghosszabb_idoszak_hossza:
        leghosszabb_idoszak_kezdet = elotte_levo.masodpercekben # a kezdet az előtte lévő, a vége a jelenlegi
        leghosszabb_idoszak_vege = jelenlegi.masodpercekben
        leghosszabb_idoszak_hossza = kulonbseg

def formatumba(masodperc):
    # másodpercből "óó:pp:mp" kinézetű stringet csinál

    # először átváltás

    ora = masodperc // 3600
    masodperc -= ora * 3600
    perc = masodperc // 60
    masodperc -= perc * 60

    return f"{ora}:{perc}:{masodperc}" # annyi nulla lesz előtte, hogy 2 karakter hosszú legyen pontosan

print(f"5. feladat Leghosszabb forgalommentes időszak: {formatumba(leghosszabb_idoszak_kezdet)} - {formatumba(leghosszabb_idoszak_vege)}")

# 6.

beker_rendszam = input("6. feladat Kérem adjon meg egy rendszámot: ")

# a rendszámokat a bekérttel betűnként fogjuk összehasonlítani

beker_betui = {} # kulcs: a betű indexe, érték: a betű

for index in range(0, len(beker_rendszam)):
    betu = beker_rendszam[index]

    if betu != "*": # ha nem csillag, akkor vagy betű, vagy - van ott
        beker_betui[index] = betu # például ha a második betű "A", akkor lesz egy ilyen elem: {1: "A"}

jo_rendszamok = [] # azoknak, melyek megfelelnek a bekértnek

for athaladas in lista:
    vizsgalt_rendszam = athaladas.rendszam # segédváltozó
    megfelelo = True # ha egy betű nem felelne meg, akkor hamis lesz

    for index, betu in beker_betui.items():
        if vizsgalt_rendszam[index] != betu: # ha az indexedik karakter nem olyan betű, akkor
            megfelelo = False

    if megfelelo == True: # ha nem lett hamis, akkor megfelel a rendszám
        jo_rendszamok.append(vizsgalt_rendszam)

print("Megfelelő rendszámok:")

for rendszam in jo_rendszamok:
    print(rendszam)

# 7.

kiir = open("vizsgalt.txt", "w", encoding="utf-8")

kiir.write(f"{lista[0].ora:02d} {lista[0].perc:02d} {lista[0].masodperc:02d} {lista[0].rendszam}\n") # az elsőt megállítják, így azt külön írjuk; 02d: bevezető nullák: annyi nullát rak a szöveg elé, amíg a szöveg hossza nem lesz 2
kovetkezo_ellenorzes_ideje = lista[0].masodpercekben + (5 * 60) # a következő ellenőrzést idő alapján fogjuk meghatározni, a kezdőérték a legelső ideje + 5perc, mivel az utána lévőt állítják csak meg

for athaladas in lista:
    if athaladas.masodpercekben >= kovetkezo_ellenorzes_ideje: # ha utána van vagy pont abban a pillanatban, akkor találtunk egy olyan járművet, amit megállítanak
        kiir.write(f"{athaladas.ora:02d} {athaladas.perc:02d} {athaladas.masodperc:02d} {athaladas.rendszam}\n")
        kovetkezo_ellenorzes_ideje = athaladas.masodpercekben + (5 * 60) # azért nem csak + 5perc, mivel bele kell számítani azt is, amikor nem jön éppen semmi
