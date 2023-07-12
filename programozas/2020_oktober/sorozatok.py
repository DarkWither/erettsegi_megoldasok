# Ladányi Attila

# 1.

class Sorozatok:
    def __init__(self, datum, nev, evad_epizod, hossz, latott):
        self.datum = datum # NI esetén nem ismert
        self.nev = nev
        self.evad_epizod = evad_epizod # evadxepizod
        self.hossz = int(hossz) # percben
        self.latott = int(latott) # 1:_már látta, 0: még nem látta

        if self.datum != "NI": # fontos, hogy legyen dátum
            szetszed = self.datum.split(".")

            self.ev = int(szetszed[0])
            self.honap = int(szetszed[1])
            self.nap = int(szetszed[2])

    def __repr__(self):
        return f"{self.datum} {self.nev} {self.evad_epizod} {self.hossz} {self.latott}"

lista = []

fajl = open("lista.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip() # első sor, a dátum
    sor_ketto = fajl.readline().strip() # a sorozat neve
    sor_harom = fajl.readline().strip() # évad és epizód
    sor_negy = fajl.readline().strip() # hossz
    sor_ot = fajl.readline().strip() # látta-e

    lista.append(Sorozatok(sor, sor_ketto, sor_harom, sor_negy, sor_ot))

# 2.

rendelkezik_datummal = 0

for sorozat in lista:
    if sorozat.datum != "NI": # ha nem ismert, akkor van dátum
        rendelkezik_datummal += 1

print(f"2. feladat\nA listában {rendelkezik_datummal} db vetítési dátummal rendelkező epizód van.")

# 3.

latott_sorozatok = 0

for sorozat in lista:
    if sorozat.latott == 1:
        latott_sorozatok += 1

print(f"\n3. feladat\nA listában lévő epizódok {round((latott_sorozatok / len(lista)) * 100, 2)}%-át látta.")

# 4.

def nap_ora_perc(perc):
    # percet átváltja nappá, órává és percé

    nap = perc // (60 * 24)
    perc -= nap * 60 * 24
    ora = perc // 60
    perc -= ora * 60

    return [nap, ora, perc]

sorozatnezessel_toltott_percek = 0

for sorozat in lista:
    if sorozat.latott == 1: # fontos, hogy látta-e a részt
        sorozatnezessel_toltott_percek += sorozat.hossz

megnezes = nap_ora_perc(sorozatnezessel_toltott_percek) # átváltás

print(f"\n4. feladat\nSorozatnézéssel {megnezes[0]} napot {megnezes[1]} órát és {megnezes[2]} percet töltött.")

# 5.

def datum_osszehasonlito(ev_egy, honap_egy, nap_egy, ev_ketto, honap_ketto, nap_ketto):
    # két dátumot összehasonlítja, visszatérési érték a nagyobb száma ("egy", vagy "ketto")
    # amíg óra:perc:másodperc formátumnál célszerű másodpercbe váltani és úgy számolni/összehasonlítani, dátumoknál nem javasolt,
    # mivel a hónapok nem ugyanannyi napokból állnak

    visszateres = ""

    if ev_egy > ev_ketto: # a nagyobb "mértékegységek" alapján, ha azok nem egyenlőek, egyértelműen eldönthető, melyik a nagyobb
        visszateres = "egy"
    elif ev_egy < ev_ketto:
        visszateres = "ketto"
    else: # ha nem dönthető el egyértelműen (azaz ev_egy == ev_ketto), vizsgáljuk a kisebb egységeket
        if honap_egy > honap_ketto:
            visszateres = "egy"
        elif honap_egy < honap_ketto:
            visszateres = "egy"
        else:
            if nap_egy > nap_ketto:
                visszateres = "egy"
            else: # ugyanazon dátum esetén is a második lesz a nagyobb
                visszateres = "ketto"

    return visszateres

beker_datum = input("\n5. feladat\nAdjon meg egy dátumot! Dátum= ").split(".") # [ev, honap, nap]

beker_datumig_nem_latott_sorozatok = []

for sorozat in lista:
    if sorozat.datum != "NI": # ismert a dátum
        if datum_osszehasonlito(sorozat.ev, sorozat.honap, sorozat.nap, int(beker_datum[0]), int(beker_datum[1]), int(beker_datum[2])) == "ketto": # a bekért legyen nagyobb vagy egyenlő
            if sorozat.latott == 0: # nem látta a részt
                beker_datumig_nem_latott_sorozatok.append(sorozat)

# nem látott sorozatok kiírása:

for sorozat in beker_datumig_nem_latott_sorozatok:
    print(f"{sorozat.evad_epizod}\t{sorozat.nev}")

# 6.

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if ho < 3:
        ev = ev - 1

    return napok[(ev + ev // 4 - ev // 100 +  ev // 400 + honapok[ho-1] + nap) % 7]


# 7.

beker_nap = input("\n7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ")

azon_a_napon_vetitik = set() # mindegyik sorozat neve csak egyszer jelenjen meg

for sorozat in lista:
    if sorozat.datum != "NI": # ismert legyen a dátum
        if hetnapja(sorozat.ev, sorozat.honap, sorozat.nap) == beker_nap:
            azon_a_napon_vetitik.add(sorozat.nev)

if len(azon_a_napon_vetitik) == 0: # nem vetítettek azon a napon, akkor:
    print("Az adott napon nem kerül adásba sorozat.")
else:
    for sorozat_nev in azon_a_napon_vetitik:
        print(sorozat_nev)

# 8.

vetitesi_ido = {} # kulcs: sorozat neve, érték: összesített vetítési idő
epizodok_szama = {} # kulcs: sorozat neve, érték: epizódok száma

for sorozat in lista:
    vetitesi_ido[sorozat.nev] = vetitesi_ido.get(sorozat.nev, 0) + sorozat.hossz
    epizodok_szama[sorozat.nev] = epizodok_szama.get(sorozat.nev, 0) + 1

kiir = open("summa.txt", "w", encoding="utf-8")

for nev, ido in vetitesi_ido.items():
    kiir.write(f"{nev} {ido} {epizodok_szama[nev]}\n") # "epizodok_szama[nev]" azért lehetséges, mert ugyanaz a kulcs a két szótárban
